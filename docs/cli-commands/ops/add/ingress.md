# Ingress

Documentation for `structix ops add ingress` command.

Add an Ingress resource to an existing microservice.

## Usage

```bash
ops add ingress <name>
```

## Options

This command currently has no options.

## Examples

To add an Ingress resource for a microservice named `user-service`, you would run:

```bash
ops add ingress user-service
``` 

This command will create an Ingress resource file at `ops/microservices/user-service/templates/ingress.yaml` if the microservice exists and the template is available.