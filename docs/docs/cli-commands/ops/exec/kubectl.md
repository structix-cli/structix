# Kubectl

Documentation for `structix ops exec kubectl` command.

# kubectl

Execute kubectl commands with the same arguments.

## Usage

```bash
structix ops exec kubectl <args>
```

## Arguments

-   `args`: The arguments to pass to the `kubectl` command. This can include any valid `kubectl` subcommand and its options.

## Options

This command currently has no options.

## Examples

```bash
structix ops exec kubectl get pods --namespace my-namespace
```