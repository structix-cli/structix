# Cluster

Documentation for `structix ops expose cluster` command.

Expose the cluster using the configured provider (e.g., minikube tunnel).

## Usage

```bash
ops expose cluster
```

## Options

This command currently has no options.

## Examples

To expose a cluster using the configured provider:

```bash
ops expose cluster
```

This command will check the configuration for the cluster provider and attempt to expose the cluster accordingly. If no provider is configured or if the provider does not support the expose operation, appropriate error messages will be displayed.