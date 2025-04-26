# Init

Documentation for `structix ops init` command.

Initialize infrastructure (Kubernetes, Terraform, etc.) in the current directory. This command sets up the necessary directories and files for managing your infrastructure.

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

During the execution, you will be prompted to confirm whether to include Kubernetes manifests, Helm charts, Terraform configurations, and GitHub Actions workflows. If the `ops` directory already exists, you will be asked if you want to overwrite it.