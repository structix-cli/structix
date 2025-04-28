# Microservice

Documentation for `structix ops rolling microservice` command.

Perform a rolling update on a microservice with a new image.

## Usage

```bash
structix ops rolling microservice <name> --image <repository:tag>
```

## Arguments

-   `name`: The name of the microservice to be updated.

## Options

This command currently has no options.

## Examples

```bash
structix ops rolling microservice my-service --image my-repo/my-image:latest
```