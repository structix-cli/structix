# Microservice

Documentation for `structix ops add microservice` command.

Add a new Helm chart microservice.

## Usage

```bash
ops add microservice <name> <image> [OPTIONS]
```

## Options

- `--db`: Optional database type (choices: postgres, mysql, mongo, redis).
- `--port`: Port the service will expose (default: 80).
- `--replicas`: Number of replicas for the deployment (default: 1).
- `--deploy`: Deploy the Helm chart into your current K8s cluster.
- `--with-ingress`: Include an Ingress resource for the microservice.

## Examples

To add a new microservice named `my-service` with the image `my-image:latest`, you can run:

```bash
ops add microservice my-service my-image:latest
```

To add a microservice with a PostgreSQL database, exposing port 8080, and deploying it immediately, use:

```bash
ops add microservice my-service my-image:latest --db postgres --port 8080 --deploy
```