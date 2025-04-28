# Microservice

Documentation for `structix ops scale microservice` command.

Scale a deployed microservice to the desired number of replicas.

## Usage

```bash
structix ops scale microservice <name> --replicas <number>
```

## Arguments

-   `name`: The name of the microservice to be scaled.

## Options

-   `--replicas`: Number of replicas to scale to. This option is required.

## Examples

```bash
structix ops scale microservice my-service --replicas 5
```