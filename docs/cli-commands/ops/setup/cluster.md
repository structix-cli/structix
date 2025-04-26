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

To set up a cluster provider configuration, run the command:

```bash
structix ops setup cluster
```

You will be prompted to select a cluster provider (either "minikube" or "kubeconfig"). If you choose "kubeconfig", you will have the option to either enter a path to an existing kubeconfig file or paste the kubeconfig content directly. Follow the prompts to complete the setup.