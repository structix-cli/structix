# Microservice

Documentation for `structix ops add microservice` command.

Add a new Helm chart microservice.

## Usage

```bash
structix ops add microservice <name> <image>
```

## Arguments

-   `name`: The name of the microservice to be created.
-   `image`: The Docker image for the microservice.

## Options

-   `--db`: Optional database to be used with the microservice. Choices are `postgres`, `mysql`, `mongo`, or `redis`.
-   `--port`: Port the service will expose. Default is `80`.
-   `--replicas`: Number of replicas for the deployment. Default is `1`.
-   `--deploy`: Deploy the Helm chart into your current Kubernetes cluster. This is a flag option.
-   `--with-ingress`: Include an Ingress resource for the microservice. This is a flag option.

## Examples

```bash
structix ops add microservice my-service my-image:latest --db postgres --port 8080 --replicas 3 --deploy --with-ingress
```