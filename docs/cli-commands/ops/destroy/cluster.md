# Cluster

Documentation for `structix ops destroy cluster` command.

## Short Description

The `ops destroy cluster` command is used to destroy a cluster based on the selected provider. It checks the configuration for the specified provider and executes the appropriate command to remove the cluster.

## Usage

```bash
ops destroy cluster
```

## Options

This command currently has no options.

## Examples

To destroy a cluster configured with a supported provider, simply run the command:

```bash
ops destroy cluster
```

If the provider is properly configured, the command will proceed to destroy the cluster. If no provider is configured or if the provider does not support the destroy operation, an appropriate error message will be displayed.