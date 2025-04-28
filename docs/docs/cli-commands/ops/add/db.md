# Db

Documentation for `structix ops add db` command.

Add a database resource to an existing microservice.

## Usage

```bash
structix ops add db <name> --db <database_type>
```

## Arguments

-   `name`: The name of the microservice to which the database resource will be added.

## Options

-   `--db`: The type of database to be used. Choices are `postgres`, `mysql`, `mongo`, or `redis`. This option is required.

## Examples

```bash
structix ops add db my-service --db postgres
```