# Init

Documentation for `structix ops init` command.

Initialize infrastructure (Kubernetes, Terraform, etc.)

## Usage

```bash
ops init
```

## Options

This command currently has no options.

## Examples

To initialize your infrastructure setup, simply run the following command:

```bash
ops init
```

During the execution, you will be prompted to confirm whether to overwrite the existing 'ops' folder (if it exists) and to select which components to include in your setup, such as Kubernetes manifests, Helm charts, Terraform configurations, and GitHub Actions workflows.