# Microservice

Documentation for `structix ops remove microservice` command.

Remove an existing Helm chart microservice.

## Usage

```bash
structix ops remove microservice <name>
```

## Arguments

-   `name`: The name of the microservice to be removed.

## Options

-   `--purge`: Also uninstall the Helm release associated with this microservice.

## Examples

```bash
structix ops remove microservice my-service --purge
```