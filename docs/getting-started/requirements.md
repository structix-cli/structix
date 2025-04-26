# Requirements

## Before You Start

Before installing and using Structix, make sure your environment meets the necessary prerequisites. Structix depends on several key tools and platforms that must be installed and properly configured on your machine.

Having a properly set up development environment ensures that Structix can scaffold, deploy, and manage your projects smoothly, whether locally or in the cloud.

## Software Requirements

You must have the following installed:

### 1. Python 3.12

Structix is written in Python and requires **Python 3.12** or later to work correctly.  
If you don't have it installed yet, you can download it from the official Python website:

-   [Download Python 3.12](https://www.python.org/downloads/release/python-3120/)

Make sure your `pip` tool is also updated to the latest version.

---

### 2. kubectl

[kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) is the official Kubernetes command-line tool. Structix relies on `kubectl` to interact with local or remote Kubernetes clusters.

You can install kubectl by following the instructions for your operating system:

-   [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

---

### 3. Minikube

[Minikube](https://minikube.sigs.k8s.io/docs/start/) lets you run a Kubernetes cluster locally. It is a lightweight option that allows you to test Kubernetes deployments without needing a full cloud setup.

Structix uses Minikube to create local development clusters easily.

-   [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)

---

### 4. Helm

[Helm](https://helm.sh/docs/intro/install/) is a package manager for Kubernetes applications. Structix leverages Helm to deploy services into Kubernetes clusters quickly and manage application lifecycles.

Installing Helm ensures that Structix can scaffold not just infrastructure, but also application deployments efficiently.

-   [Install Helm](https://helm.sh/docs/intro/install/)

---

## Optional Tools

While not strictly required, having these tools can improve your development workflow with Structix:

-   **Docker and Docker Compose** — for building and running containerized applications.
-   **Terraform** — for managing cloud infrastructure (Structix can generate Terraform templates).

---

By ensuring you have all these requirements set up properly, you will be able to unlock the full potential of Structix for backend and DevOps development.

---
