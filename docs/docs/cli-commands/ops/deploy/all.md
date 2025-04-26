# All

Documentation for `structix ops deploy all` command.

Deploy all microservices found in the `ops/microservices` directory.

## Usage

```bash
structix ops deploy all
```

## Options

This command currently has no options.

## Examples

To deploy all microservices defined in the `ops/microservices` directory, run the following command:

```bash
structix ops deploy all
``` 

If the deployment is successful, the command will process each microservice that contains a `Chart.yaml` file. If no microservices directory is found or no Helm charts are present, appropriate messages will be displayed.