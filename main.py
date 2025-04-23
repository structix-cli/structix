import json
import questionary
from pathlib import Path

CONFIG_FILE = Path.cwd() / "structix.config.json"


def save_preferences(preferences: dict):
    with open(CONFIG_FILE, "w") as f:
        json.dump(preferences, f, indent=2)


def load_preferences():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return None


def ask_questions():
    architecture = questionary.select(
        "📦 What kind of architecture do you want to generate?",
        choices=["Monolith", "Microservices"],
    ).ask()

    ddd = questionary.confirm("🧠 Apply Domain-Driven Design (DDD)?").ask()
    hex_arch = questionary.confirm(
        "🧩 Apply Hexagonal Architecture (Ports and Adapters)?"
    ).ask()
    cqrs = questionary.confirm(
        "⚡ Apply CQRS (Command Query Responsibility Segregation)?"
    ).ask()

    return {
        "architecture": architecture,
        "ddd": ddd,
        "hexagonal": hex_arch,
        "cqrs": cqrs,
    }


def main():
    print("🔧 Welcome to Structix CLI!")

    previous = load_preferences()
    if previous:
        use_previous = questionary.confirm(
            "💾 Found saved preferences. Do you want to reuse them?"
        ).ask()
        if use_previous:
            print("✅ Using saved preferences...")
            print(json.dumps(previous, indent=2))
            return

    preferences = ask_questions()
    save_preferences(preferences)
    print("✅ Preferences saved to structix.config.json:")
    print(json.dumps(preferences, indent=2))


if __name__ == "__main__":
    main()
