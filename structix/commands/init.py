import click
import questionary

from structix.utils.config import load_config, save_config


@click.command()  # type: ignore
def init() -> None:
    """Initialize a new Structix project configuration."""
    print("🔧 Welcome to Structix CLI!")

    previous = load_config()
    if previous:
        use_previous = questionary.confirm(
            "💾 Found saved preferences. Do you want to reuse them?"
        ).ask()
        if use_previous:
            click.echo("✅ Using saved preferences...")
            click.echo(previous)
            return

    stack = questionary.select(
        "🧪 Which tech stack are you using?",
        choices=["NestJS"],
    ).ask()

    architecture = questionary.select(
        "📦 What kind of architecture do you want to generate?",
        choices=["Monolith", "Microservices"],
    ).ask()

    ddd = questionary.confirm("🧠 Apply Domain-Driven Design (DDD)?").ask()
    hex_arch = questionary.confirm("🧩 Apply Hexagonal Architecture?").ask()
    cqrs = questionary.confirm("⚡ Apply CQRS?").ask()

    preferences = {
        "stack": stack,
        "architecture": architecture,
        "ddd": ddd,
        "hexagonal": hex_arch,
        "cqrs": cqrs,
    }

    save_config(preferences)
    click.echo("✅ Preferences saved to structix.config.json")
