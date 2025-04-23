import click
from core.config import load_config, save_config


@click.group()
def config():
    """Manage Structix configuration."""
    pass


@config.command("set")
@click.argument("key")
@click.argument("value")
def config_set(key, value):
    config_data = load_config()
    if value.lower() == "true":
        value = True
    elif value.lower() == "false":
        value = False

    config_data[key] = value
    save_config(config_data)
    click.echo(f"🔧 Set '{key}' to '{value}'")


@config.command("show")
def config_show():
    config_data = load_config()
    click.echo("📋 Current configuration:")
    for k, v in config_data.items():
        click.echo(f"  {k}: {v}")
