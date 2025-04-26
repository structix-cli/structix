import os
from typing import List, Set

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "your-default-api-key-here")
COMMANDS_DIR: str = "structix/commands"
DOCS_DIR: str = "docs/cli-commands"


client = OpenAI(api_key=OPENAI_API_KEY)


def list_command_files(base_dir: str) -> List[str]:
    """List all .py command files except __init__.py."""
    command_files: List[str] = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                relative_path = os.path.relpath(
                    os.path.join(root, file), base_dir
                )
                command_files.append(relative_path)
    return command_files


def build_prompt(command_path: str) -> str:
    """Build the prompt to send to OpenAI, including file content."""
    base_command: str = (
        command_path.replace(".py", "").replace("/", " ").replace("\\", " ")
    )
    full_command: str = f"structix {base_command}"

    full_path: str = os.path.join(COMMANDS_DIR, command_path)
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            file_content: str = f.read()
    except Exception as e:
        print(f"⚠️ Warning: Failed to read {full_path}: {e}")
        file_content = ""

    return f"""
You are writing professional CLI documentation.

Command: `{full_command}`

Below is the source code of the command:

```
{file_content}
```

When writing usage examples or showing how to use the command, always:
- Start the example with a bash code block using triple backticks and the language "bash", like this: ```bash
- Write the command exactly as `{full_command}`.
- Then close the code block correctly with triple backticks.
- Never omit the `bash` annotation.

Please generate a documentation page in Markdown with:

- A short description (what it does).
- A Usage section showing how the command would be used.
- An Options section (say "This command currently has no options." if none are available).
- An Examples section with at least one realistic usage example.

Do not include a title or 'Documentation for' at the beginning; that will be handled externally.

Return only pure markdown content.
"""


def generate_markdown(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a professional technical writer for CLI documentation.",
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.5,
    )
    return str(response.choices[0].message.content)


def format_title(command_path: str) -> str:
    """Format the title based on the command path."""
    parts: List[str] = command_path.replace(".py", "").split(os.sep)
    last_part: str = parts[-1]
    title: str = last_part.replace("_", " ").capitalize()
    return title


def main() -> None:
    """Main execution function."""
    commands: List[str] = list_command_files(COMMANDS_DIR)

    existing_docs: Set[str] = set()
    for root, dirs, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                relative_path: str = os.path.relpath(
                    os.path.join(root, file), DOCS_DIR
                )
                existing_docs.add(relative_path.replace(".md", ".py"))

    for command in commands:
        doc_path: str = os.path.join(DOCS_DIR, command.replace(".py", ".md"))

        if command not in existing_docs:
            os.makedirs(os.path.dirname(doc_path), exist_ok=True)

            print(f"📄 Generating documentation for {command}...")
            prompt: str = build_prompt(command)
            markdown_content: str = generate_markdown(prompt)

            title: str = format_title(command)
            first_lines: str = (
                f"# {title}\n\n"
                f"Documentation for `structix {command.replace('.py', '').replace(os.sep, ' ')}` command.\n\n"
            )

            with open(doc_path, "w", encoding="utf-8") as f:
                f.write(first_lines)
                f.write(markdown_content)
        else:
            print(f"✅ Documentation already exists for {command}")

    for existing_doc in existing_docs:
        if existing_doc not in commands:
            doc_md_path: str = os.path.join(
                DOCS_DIR, existing_doc.replace(".py", ".md")
            )
            print(f"🗑 Removing orphan documentation {doc_md_path}...")
            os.remove(doc_md_path)


if __name__ == "__main__":
    main()
