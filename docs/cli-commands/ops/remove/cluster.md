# Cluster

Documentation for `structix ops remove cluster` command.

Remove cluster configuration without destroying the cluster.

## Usage

```
ops remove cluster
```

## Options

This command currently has no options.

## Examples

To remove the cluster configuration for the currently configured provider, simply run:

```
ops remove cluster
``` 

If the provider is configured correctly, you will see a confirmation message indicating that the cluster config is being removed. If there is no provider configured or if the provider does not support the removal command, an appropriate error message will be displayed.