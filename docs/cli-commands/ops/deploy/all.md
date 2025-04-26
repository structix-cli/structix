# All

Documentation for `structix ops deploy all` command.

Deploy all microservices found in the `ops/microservices` directory.

## Usage

```bash
ops deploy all
```

## Options

This command currently has no options.

## Examples

To deploy all microservices, navigate to your project directory and run:

```bash
ops deploy all
```

This command will search for all Helm charts in the `ops/microservices` directory and deploy each one found. If no microservices directory or Helm charts are found, appropriate messages will be displayed.