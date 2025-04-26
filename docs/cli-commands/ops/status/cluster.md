# Cluster

Documentation for `structix ops status cluster` command.

Show cluster status across nodes, pods, deployments, etc.

## Usage

```bash
ops status cluster
```

## Options

This command currently has no options.

## Examples

To check the status of your cluster, simply run:

```bash
ops status cluster
```

This will fetch and display the current status of your cluster, including information about nodes, pods, and deployments, based on the configured provider. If no provider is configured or if the provider does not support the status command, appropriate error messages will be displayed.