# Ingress

Documentation for `structix ops deploy ingress` command.

Deploys an Ingress resource for a specified microservice. If the Ingress controller is not already installed, it will install it using Helm.

## Usage

```
ops deploy ingress <name>
```

## Options

This command currently has no options.

## Examples

To deploy an Ingress resource for a microservice named `my-service`, use the following command:

```
ops deploy ingress my-service
```