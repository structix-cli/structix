# structix/core/providers.py
import os
import queue
import subprocess
import threading
import time
from typing import Callable, Dict, List

import click
import psutil  # type: ignore[import]

from structix.utils.config import force_save_config, get_config, load_config

PROVIDER_ACTIONS: Dict[str, List[str]] = {
    "minikube": [
        "init",
        "create",
        "start",
        "stop",
        "destroy",
        "remove",
        "status",
        "expose",
    ],
    "kubeconfig": ["init", "remove", "status"],
}


def is_action_supported(provider: str, action: str) -> bool:
    return action in PROVIDER_ACTIONS.get(provider, [])


def remove_cluster() -> None:
    config = get_config()
    if not config.cluster:
        click.echo("⚠️ No cluster configuration found.")
        return

    raw_config = load_config()
    raw_config.pop("cluster", None)
    force_save_config(raw_config)
    click.echo("🗑️ Cluster config removed from structix.config.json")


def status_cluster() -> None:
    config = get_config()

    if not config.cluster or not config.cluster.provider:
        click.echo("❌ Cluster not configured. Run: structix ops init cluster")
        raise SystemExit(1)

    provider = config.cluster.provider
    env = os.environ.copy()
    if config.cluster.kubeconfig:
        env["KUBECONFIG"] = config.cluster.kubeconfig

    click.echo(f"🔍 Cluster Provider: {provider}")

    try:
        click.echo("🔍 Retrieving full cluster status...")
        click.echo("Nodes:\n")
        subprocess.run(["kubectl", "get", "nodes"], check=True, env=env)
        click.echo("\n\n")
        click.echo("Pods:\n")
        subprocess.run(["kubectl", "get", "pods", "-A"], check=True, env=env)
        click.echo("\n\n")
        click.echo("Deployments:\n")
        subprocess.run(
            ["kubectl", "get", "deployments", "-A"], check=True, env=env
        )
        click.echo("\n\n")
        click.echo("StatefulSets:\n")
        subprocess.run(
            ["kubectl", "get", "statefulsets", "-A"], check=True, env=env
        )
        click.echo("\n\n")
        click.echo("Ingresses:\n")
        subprocess.run(
            ["kubectl", "get", "ingress", "-A"], check=True, env=env
        )
        click.echo("\n\n")
        subprocess.run(["helm", "list", "-A"], check=True, env=env)
    except subprocess.CalledProcessError as e:
        click.echo("❌ Could not retrieve full cluster status.")
        click.echo(f"🔍 Error: {e}")


def wait_for_output_and_log(
    process: subprocess.Popen[bytes],
    ready_event: threading.Event,
    output_queue: queue.Queue[str],
) -> None:
    if process.stdout is None:
        return

    for line in iter(process.stdout.readline, b""):
        if not line:
            break

        decoded_line = line.decode()
        output_queue.put(decoded_line)
        click.echo(decoded_line)

        if not ready_event.is_set():
            ready_event.set()


def port_forward_service(
    namespace: str, service_name: str, local_port: int, remote_port: int
) -> None:
    click.echo(f"🔌 Exposing {service_name} on localhost:{local_port}")
    subprocess.Popen(
        [
            "kubectl",
            "port-forward",
            f"svc/{service_name}",
            f"{local_port}:{remote_port}",
            "-n",
            namespace,
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def start_minikube_tunnel_blocking_on_output() -> None:
    try:
        click.echo("🔌 Starting 'minikube tunnel' and waiting for output...")

        process = subprocess.Popen(
            ["minikube", "tunnel"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )

        ready_event = threading.Event()
        output_queue: queue.Queue[str] = queue.Queue()

        thread = threading.Thread(
            target=wait_for_output_and_log,
            args=(process, ready_event, output_queue),
            daemon=True,
        )
        thread.start()

        if ready_event.wait(timeout=100):
            time.sleep(1)
            click.echo("✅ Tunnel seems to have started.")
        else:
            click.echo("⚠️ No output detected yet, continuing anyway...")

    except Exception as e:
        click.echo("❌ Failed to start minikube tunnel.")
        click.echo(f"🔍 Error: {e}")


def expose_cluster() -> None:
    HOSTS_FILE = "/etc/hosts"
    STRUCTIX_MARKER_BEGIN = "# structix-managed-hosts-BEGIN"
    STRUCTIX_MARKER_END = "# structix-managed-hosts-END"

    config = get_config()

    if not config.cluster or config.cluster.provider != "minikube":
        click.echo("⚠️  Expose is only supported for Minikube right now.")
        return

    try:
        click.echo(
            "🔑 Requesting sudo access for upcoming privileged operations..."
        )
        subprocess.run(["sudo", "-v"], check=True)
    except subprocess.CalledProcessError:
        click.echo("❌ Sudo access is required to expose the cluster.")
        return

    for proc in psutil.process_iter(attrs=["pid", "cmdline"]):
        try:
            cmdline = proc.info["cmdline"]
            if cmdline and "minikube" in cmdline and "tunnel" in cmdline:
                click.echo(
                    "🛑 Existing minikube tunnel found. Terminating it..."
                )
                proc.terminate()
                proc.wait(timeout=5)
                click.echo("✅ Previous minikube tunnel terminated.")
        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.TimeoutExpired,
        ):
            continue

    start_minikube_tunnel_blocking_on_output()

    ip = None
    for attempt in range(100):
        result = subprocess.run(
            [
                "kubectl",
                "get",
                "svc",
                "ingress-nginx-controller",
                "-n",
                "ingress-nginx",
                "-o=jsonpath={.status.loadBalancer.ingress[0].ip}",
            ],
            stdout=subprocess.PIPE,
            text=True,
        )
        ip = result.stdout.strip()
        if ip:
            click.echo(f"✅ Ingress IP found: {ip}")
            break
        click.echo(f"⏳ Waiting for ingress IP... (attempt {attempt + 1})")
        time.sleep(2)

    if not ip:
        click.echo("⚠️  Could not determine external IP of ingress controller.")
        return

    try:
        result = subprocess.run(
            [
                "kubectl",
                "get",
                "ingress",
                "-A",
                '-o=jsonpath={range .items[*].spec.rules[*]}{.host}{"\\n"}{end}',
            ],
            stdout=subprocess.PIPE,
            text=True,
            check=True,
        )

        hosts = [
            line.strip() for line in result.stdout.splitlines() if line.strip()
        ]

        if not hosts:
            click.echo("⚠️  No ingress hosts found.")
            return

        click.echo("📝 Registering the following hostnames:")
        for host in hosts:
            click.echo(f"   • http://{host} → {ip}")

        try:
            with open(HOSTS_FILE, "r") as f:
                original_hosts = f.read()
        except PermissionError:
            click.echo("❌ Permission denied: need sudo to edit /etc/hosts.")
            return

        before = original_hosts.split(STRUCTIX_MARKER_BEGIN)[0]
        after = ""
        if STRUCTIX_MARKER_END in original_hosts:
            after = original_hosts.split(STRUCTIX_MARKER_END)[1]

        new_block = f"{STRUCTIX_MARKER_BEGIN}\n"
        for host in hosts:
            new_block += f"{ip} {host}\n"
        new_block += f"{STRUCTIX_MARKER_END}\n"

        final_hosts = before.rstrip() + "\n\n" + new_block + after.lstrip()

        subprocess.run(
            ["sudo", "cp", HOSTS_FILE, HOSTS_FILE + ".bak"], check=True
        )

        with open("/tmp/structix-hosts", "w") as tmp:
            tmp.write(final_hosts)
        subprocess.run(
            ["sudo", "cp", "/tmp/structix-hosts", HOSTS_FILE], check=True
        )
        click.echo("✅ /etc/hosts updated with Structix managed entries.")

    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to retrieve ingress hosts or IP.")
        click.echo(f"🔍 Error: {e}")

    try:
        click.echo("🔌 Exposing services on localhost...")

        services_to_expose = [
            ("default", "grafana", 9731, 80),
            ("default", "prometheus-server", 9732, 80),
            ("default", "alertmanager", 9733, 9093),
            ("default", "jaeger-query", 16686, 80),
        ]

        for namespace, service, local_port, remote_port in services_to_expose:
            port_forward_service(namespace, service, local_port, remote_port)

        click.echo("✅ Services exposed on localhost.")
    except subprocess.CalledProcessError as e:
        click.echo("❌ Failed to expose services.")
        click.echo(f"🔍 Error: {e}")


PROVIDER_COMMANDS: Dict[str, Dict[str, Callable[[], None]]] = {
    "minikube": {
        "create": lambda: (
            subprocess.run(["minikube", "start"], check=True),
            None,
        )[1],
        "start": lambda: (
            subprocess.run(["minikube", "start"], check=True),
            None,
        )[1],
        "stop": lambda: (
            subprocess.run(["minikube", "stop"], check=True),
            None,
        )[1],
        "destroy": lambda: (
            subprocess.run(["minikube", "delete"], check=True),
            None,
        )[1],
        "remove": remove_cluster,
        "status": status_cluster,
        "expose": expose_cluster,
    },
    "kubeconfig": {
        "remove": remove_cluster,
        "status": status_cluster,
    },
}


def get_provider_command(
    provider: str, action: str
) -> Callable[[], None] | None:
    return PROVIDER_COMMANDS.get(provider, {}).get(action)
