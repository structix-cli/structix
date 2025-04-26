# Cluster

Documentation for `structix ops stop cluster` command.

## Description

The `ops stop cluster` command is used to stop a cluster based on the selected provider. It checks the configuration for the cluster provider and invokes the appropriate command to stop the cluster.

## Usage

```bash
ops stop cluster
```

## Options

This command currently has no options.

## Examples

To stop a cluster with the configured provider, simply run:

```bash
ops stop cluster
```

If there is no provider configured or if the provider does not support the stop operation, appropriate error messages will be displayed.