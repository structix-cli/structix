# Context

Documentation for `structix proj add context` command.

Scaffold a new Domain-Driven Design (DDD) context within a project.

## Usage

```bash
proj add context <name>
```

## Options

This command currently has no options.

## Examples

To create a new DDD context named `UserManagement`, you would run:

```bash
proj add context UserManagement
``` 

This command will create the necessary folder structure for the `UserManagement` context in the current working directory, provided the project's architecture is set to "Monolith" and DDD is enabled.