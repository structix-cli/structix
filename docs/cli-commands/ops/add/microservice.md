# Microservice

Documentation for `structix ops add microservice` command.

Add a new Helm chart microservice.

## Usage

```bash
structix ops add microservice <name> <image> [OPTIONS]
```

## Options

- `--db`: Optional database to use (choices: `postgres`, `mysql`, `mongo`, `redis`).
- `--port`: Port the service will expose (default: `80`).
- `--replicas`: Number of replicas for the deployment (default: `1`).
- `--deploy`: Deploy the Helm chart into your current K8s cluster.
- `--with-ingress`: Include an Ingress resource for the microservice.

## Examples

To create a new microservice named `my-service` with the Docker image `my-image:latest`, run:

```bash
structix ops add microservice my-service my-image:latest
```

To create a microservice with a PostgreSQL database, exposing port `8080`, and with 3 replicas, run:

```bash
structix ops add microservice my-service my-image:latest --db postgres --port 8080 --replicas 3
```

To create a microservice and deploy it immediately, run:

```bash
structix ops add microservice my-service my-image:latest --deploy
```

To create a microservice with an Ingress resource, run:

```bash
structix ops add microservice my-service my-image:latest --with-ingress
```