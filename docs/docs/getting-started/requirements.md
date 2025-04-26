# Requirements

## Before You Start

Before installing and using Structix, it is essential to ensure that your environment meets the necessary prerequisites. Structix depends on several critical tools and platforms that must be installed and properly configured on your machine.

Setting up your environment correctly ensures that Structix can scaffold, deploy, and manage your projects smoothly, whether you are working locally or deploying to production-grade infrastructure.

This page will guide you through the essential software you must have installed to fully benefit from Structix.

## Software Requirements

You **must** have the following installed on your system:

---

### 1. Python 3.12

Structix is built with Python and requires **Python 3.12** or later to function correctly.  
Without the correct Python version, the CLI will not operate properly.

You can download Python 3.12 directly from the official website:

-   [Download Python 3.12](https://www.python.org/downloads/release/python-3120/)

After installing Python, ensure that `pip` (Python's package manager) is updated to the latest version:

```bash
pip install --upgrade pip
```

> Note: In environments where multiple Python versions are installed, it may be necessary to use `python3` and `pip3` explicitly.

---

### 2. kubectl

[kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) is the command-line tool used to interact with Kubernetes clusters. Structix relies heavily on `kubectl` for deploying services, managing clusters, and applying configurations.

Install kubectl by following the official guide for your operating system:

-   [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

Once installed, you can verify the installation by running:

```bash
kubectl version --client
```

---

### 3. Minikube

[Minikube](https://minikube.sigs.k8s.io/docs/start/) is a tool that allows you to run a local Kubernetes cluster. It is lightweight and ideal for local development and testing before deploying to cloud providers.

Structix uses Minikube to create local environments where projects can be developed and tested under real Kubernetes conditions.

Installation instructions:

-   [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)

Start a local cluster easily with:

```bash
minikube start
```

---

### 4. Helm

[Helm](https://helm.sh/docs/intro/install/) is the de facto package manager for Kubernetes applications. Structix uses Helm to manage deployments, upgrades, and rollbacks of Kubernetes applications efficiently.

Installing Helm ensures that Structix can:

-   Deploy services quickly.
-   Manage Kubernetes application lifecycles.
-   Apply version-controlled deployment templates.

Installation link:

-   [Install Helm](https://helm.sh/docs/intro/install/)

Check the installation by running:

```bash
helm version
```

---

### 5. Terraform

[Terraform](https://developer.hashicorp.com/terraform/downloads) is a tool for building, changing, and versioning infrastructure safely and efficiently. Structix integrates Terraform to provision and manage cloud infrastructure directly from your project setup.

Having Terraform installed allows Structix to:

-   Generate Infrastructure as Code (IaC) templates.
-   Create cloud resources such as Kubernetes clusters, databases, and more.
-   Manage the full lifecycle of cloud environments.

Install Terraform from the official site:

-   [Install Terraform](https://developer.hashicorp.com/terraform/downloads)

Verify Terraform installation:

```bash
terraform version
```

---

## Optional Tools

While not mandatory, having these tools can further enhance your Structix development experience:

-   **Docker and Docker Compose** — Useful for building, testing, and running containerized applications locally.
-   **Virtualenv (Python Virtual Environments)** — Recommended for isolating your Python dependencies when working on multiple projects.

---

## Summary

To recap, you must install the following to work effectively with Structix:

| Tool        | Purpose                              |
| ----------- | ------------------------------------ |
| Python 3.12 | Run Structix CLI.                    |
| kubectl     | Manage Kubernetes clusters.          |
| Minikube    | Create a local Kubernetes cluster.   |
| Helm        | Deploy applications to Kubernetes.   |
| Terraform   | Manage cloud infrastructure as code. |

Setting up these requirements ensures that you can unlock the full power of Structix, streamline your backend projects, and automate your DevOps workflows right from the start.
