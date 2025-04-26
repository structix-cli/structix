# Db

Documentation for `structix ops add db` command.

Add a database resource to an existing microservice.

## Usage

```bash
structix ops add db <name> [--db <database>]
```

## Options

This command currently has no options.

## Examples

To add a PostgreSQL database resource to a microservice named `user-service`, you would use the following command:

```bash
structix ops add db user-service --db postgres
``` 

If you want to add a database resource without specifying a database type, you can simply omit the `--db` option:

```bash
structix ops add db user-service
``` 

Make sure that the microservice exists in the specified path before running the command.