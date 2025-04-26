# Ingress

Documentation for `structix ops deploy ingress` command.

Deploys an Ingress resource for a specified microservice in a Kubernetes cluster. This command ensures that the necessary Ingress controller is installed and configured before deploying the Ingress resource.

## Usage

```bash
structix ops deploy ingress <name>
```

## Options

This command currently has no options.

## Examples

To deploy an Ingress resource for a microservice named `my-microservice`, you would run the following command:

```bash
structix ops deploy ingress my-microservice
```