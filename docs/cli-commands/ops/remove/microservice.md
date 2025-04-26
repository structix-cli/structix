# Microservice

Documentation for `structix ops remove microservice` command.

Remove an existing Helm chart microservice.

## Usage

```bash
structix ops remove microservice <name> [--purge]
```

## Options

- `--purge`: Also uninstall the Helm release associated with this microservice.

## Examples

1. To remove a microservice named `user-service` without purging the Helm release:

   ```bash
   structix ops remove microservice user-service
   ```

2. To remove a microservice named `payment-service` and also uninstall its associated Helm release:

   ```bash
   structix ops remove microservice payment-service --purge
   ```