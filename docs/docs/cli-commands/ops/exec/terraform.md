# Terraform

Documentation for `structix ops exec terraform` command.

# Terraform Execution

Execute terraform commands with the same arguments.

## Usage

```bash
structix ops exec terraform <args>
```

## Arguments

-   `args`: The arguments to pass to the terraform command. This can include any valid terraform subcommands and options.

## Options

This command currently has no options.

## Examples

```bash
structix ops exec terraform init
``` 

```bash
structix ops exec terraform apply -auto-approve
``` 

```bash
structix ops exec terraform plan
```