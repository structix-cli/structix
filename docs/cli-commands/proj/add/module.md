# Module

Documentation for `structix proj add module` command.

Scaffold a new module within a project that follows a Monolith architecture. This command checks for existing modules and the project's architecture constraints before creating the new module.

## Usage

```bash
proj add module <name>
```

## Options

This command currently has no options.

## Examples

To create a new module named `user`, run the following command:

```bash
proj add module user
```

If the module already exists, you will receive a warning message:

```
⚠️ Module 'user' already exists.
```

If the project architecture is not set to Monolith, you will see:

```
⚠️ Modules are only supported in Monolith architecture.
```

If the project is set up with DDD or Hexagonal architecture, you will receive:

```
⚠️ Modules are only supported in simple architecture without DDD or Hexagonal.
```

Upon successful creation of the module, you will see:

```
📦 Creating module 'user'...
✅ Context created successfully.
```