# Ingress

Documentation for `structix ops deploy ingress` command.

Deploys an Ingress resource for a specified microservice. This command checks if the microservice and its corresponding Ingress resource exist, installs the Ingress controller if it is not already installed, and then deploys the Ingress configuration.

## Usage

```
structix ops deploy ingress <name>
```

## Options

This command currently has no options.

## Examples

To deploy an Ingress resource for a microservice named `my-microservice`, use the following command:

```
structix ops deploy ingress my-microservice
```