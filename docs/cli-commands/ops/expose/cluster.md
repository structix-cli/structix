# Cluster

Documentation for `structix ops expose cluster` command.

Expose the cluster using the configured provider (e.g., minikube tunnel).

## Usage

```bash
structix ops expose cluster
```

## Options

This command currently has no options.

## Examples

To expose the cluster using the configured provider, run the following command:

```bash
structix ops expose cluster
```

If the provider is correctly configured (e.g., minikube), you will see a message indicating that the cluster is being exposed. If no provider is configured or if the provider does not support the 'expose' command, appropriate error messages will be displayed.