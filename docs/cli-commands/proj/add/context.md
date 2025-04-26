# Context

Documentation for `structix proj add context` command.

Scaffold a new Domain-Driven Design (DDD) context within a Monolith architecture.

## Usage

```bash
structix proj add context <name>
```

## Options

This command currently has no options.

## Examples

To create a new DDD context named `UserManagement`, you would run:

```bash
structix proj add context UserManagement
``` 

If the project architecture is set to "Monolith" and the context does not already exist, this command will create the necessary folder structure for the context.