# Cluster

Documentation for `structix ops init cluster` command.

Initialize cluster provider configuration using an interactive selector.

## Usage

```bash
ops init cluster
```

## Options

This command currently has no options.

## Examples

To initialize a cluster provider configuration, simply run the command:

```bash
ops init cluster
```

Follow the prompts to select a cluster provider (either `minikube` or `kubeconfig`). If you choose `kubeconfig`, you will be asked how to provide the kubeconfig file, either by entering a path to an existing file or pasting the content directly. After providing the necessary information, the configuration will be saved.