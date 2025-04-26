# Microservice

Documentation for `structix ops remove microservice` command.

Remove an existing Helm chart microservice.

## Usage

```bash
ops remove microservice <name> [--purge]
```

## Options

This command currently has no options.

## Examples

To remove a microservice named `user-service` without uninstalling the associated Helm release:

```bash
ops remove microservice user-service
```

To remove a microservice named `payment-service` and also uninstall the associated Helm release:

```bash
ops remove microservice payment-service --purge
```