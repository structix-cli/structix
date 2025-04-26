# Cluster

Documentation for `structix ops destroy cluster` command.

Destroys a cluster based on the selected provider.

## Usage

```bash
structix ops destroy cluster
```

## Options

This command currently has no options.

## Examples

To destroy a cluster using the configured provider, run the following command:

```bash
structix ops destroy cluster
``` 

This command will prompt the destruction of the cluster if a valid provider is configured. If no provider is configured or if the provider does not support the destroy operation, an error message will be displayed.