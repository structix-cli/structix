from setuptools import find_packages, setup  # type: ignore[import]

setup(
    name="structix",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["click", "questionary", "jinja2"],
    entry_points={
        "console_scripts": [
            "structix=structix.cli:cli",
        ],
    },
)
