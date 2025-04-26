# Microservice

Documentation for `structix ops remove microservice` command.

Remove an existing Helm chart microservice.

## Usage

```bash
structix ops remove microservice <name>
```

## Options

This command currently has no options.

## Examples

To remove a microservice named `my-service` without purging its Helm release, you would use:

```bash
structix ops remove microservice my-service
```

To remove a microservice named `my-service` and also uninstall its associated Helm release, you would use:

```bash
structix ops remove microservice my-service --purge
```