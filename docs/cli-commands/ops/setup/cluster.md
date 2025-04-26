# Cluster

Documentation for `structix ops setup cluster` command.

Setup cluster provider configuration using an interactive selector.

## Usage

```bash
structix ops setup cluster
```

## Options

This command currently has no options.

## Examples

1. **Setting up a cluster with kubeconfig**:
   - Run the command:
     ```bash
     structix ops setup cluster
     ```
   - Select "kubeconfig" when prompted for the cluster provider.
   - Choose to either enter a path to an existing kubeconfig file or paste the kubeconfig content directly.
   - Follow the prompts to complete the setup.

2. **Setting up a cluster with minikube**:
   - Execute the command:
     ```bash
     structix ops setup cluster
     ```
   - Choose "minikube" as the cluster provider when prompted.
   - The configuration will be saved automatically.