# Microservice

Documentation for `structix ops add microservice` command.

Add a new Helm chart microservice.

## Usage

```bash
structix ops add microservice <name> <image>
```

## Options

- `--db`: Optional database (choices: postgres, mysql, mongo, redis).
- `--port`: Port the service will expose (default: 80).
- `--replicas`: Number of replicas for the deployment (default: 1).
- `--deploy`: Deploy the Helm chart into your current K8s cluster.
- `--with-ingress`: Include an Ingress resource for the microservice.

## Examples

```bash
structix ops add microservice my-service my-image:latest --db postgres --port 8080 --replicas 3 --deploy --with-ingress
```