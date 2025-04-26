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

If there are microservices with Helm charts present, they will be deployed accordingly. If no microservices directory or Helm charts are found, appropriate messages will be displayed.