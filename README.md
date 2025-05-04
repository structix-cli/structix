# Structix v0.1.0

---

## 📦 Installation

### 🔧 Prerequisites

Before installing, ensure you have the following tools installed on your system:

-   [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) - Kubernetes command-line tool.
-   [Minikube](https://minikube.sigs.k8s.io/docs/start/) - Local Kubernetes cluster.
-   [Helm](https://helm.sh/docs/intro/install/) - Kubernetes package manager.

Make sure these tools are properly configured and accessible from your terminal.

### 🔧 With `pip`

Install directly from GitHub (recommended for now):

```bash
pip install git+https://github.com/structix-cli/structix.git
```

### 🔧 Install for local development

```bash
pip install -e .
```

### Example usage

```bash
structix ops init cluster

structix ops add microservice example-simple brayand/microservice-example-simple:0.1.0 --with-ingress --deploy --port=3000 --replicas=3

structix ops add microservice example-persistence brayand/microservice-example-persistence:0.1.0 --with-ingress --deploy --port=3000 --replicas=3 --db=mysql

structix ops add microservice example-prometheus brayand/microservice-example-prometheus:0.1.0 --with-ingress --deploy --port=3000 --replicas=3 --with-prometheus --metrics-port=3000 --metrics-path=/metrics

structix ops add microservice example-jaeger brayand/microservice-example-jaeger:0.1.0 --with-ingress --deploy --port=3000 --replicas=3
```
