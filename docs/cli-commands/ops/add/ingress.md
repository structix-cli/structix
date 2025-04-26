# Ingress

Documentation for `structix ops add ingress` command.

Add an Ingress resource to an existing microservice.

## Usage

```bash
structix ops add ingress <name>
```

## Options

This command currently has no options.

## Examples

To add an Ingress resource for a microservice named `my-service`, you would use the following command:

```bash
structix ops add ingress my-service
``` 

This command will create an `ingress.yaml` file in the `ops/microservices/my-service/templates` directory, provided that the microservice exists and the ingress template is available.