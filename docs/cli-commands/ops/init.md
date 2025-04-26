# Init

Documentation for `structix ops init` command.

## Description

The `structix ops init` command initializes the infrastructure setup for your project, allowing you to scaffold configurations for Kubernetes, Helm, Terraform, and GitHub Actions workflows. It checks for the existence of an `ops` directory and prompts the user for confirmation before proceeding with the setup.

## Usage

```bash
structix ops init
```

## Options

This command currently has no options.

## Examples

To initialize your infrastructure setup, simply run the command:

```bash
structix ops init
```

During execution, you will be prompted to confirm whether to include Kubernetes manifests, Helm charts, Terraform configurations, and GitHub Actions workflows. If the `ops` directory already exists, you will be asked if you want to overwrite it.