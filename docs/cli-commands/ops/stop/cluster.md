# Cluster

Documentation for `structix ops stop cluster` command.

## Short Description

The `structix ops stop cluster` command stops a cluster based on the selected provider. It checks the configured provider and invokes the appropriate stop command if supported.

## Usage

```bash
structix ops stop cluster
```

## Options

This command currently has no options.

## Examples

To stop a cluster using the configured provider, run the following command:

```bash
structix ops stop cluster
```

If no provider is configured, the command will output an error message indicating that no cluster provider is set. If the configured provider does not support the stop operation, it will also inform you accordingly.