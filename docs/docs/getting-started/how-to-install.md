# How to Install

## Installing Structix CLI

Structix is distributed via a GitHub repository. You can easily install it using `pip`, the Python package manager.

To install Structix globally on your system, run the following command:

```bash
pip install git+https://github.com/structix-cli/structix.git
```

If your system uses multiple versions of Python, you may want to use `pip3` to ensure that Python 3.12 is used:

```bash
pip3 install git+https://github.com/structix-cli/structix.git
```

After the installation is complete, the `structix` command should be available globally in your terminal.

You can verify the installation by checking the version:

```bash
structix --version
```

If the command returns the current version of Structix, the installation was successful.

---

## Upgrading Structix

If a new version of Structix is released, you can upgrade your local installation easily by re-running the install command with the `--upgrade` flag:

```bash
pip install --upgrade git+https://github.com/structix-cli/structix.git
```

Keeping Structix updated ensures that you always have access to the latest features, performance improvements, and security patches.

It is recommended to periodically check for updates if you are using Structix in production environments.

---

## Troubleshooting Installation

If you encounter issues during installation, here are a few tips:

-   **Ensure Python 3.12 is installed and properly configured.**  
    You can verify this with:

    ```bash
    python3 --version
    ```

-   **Update pip to the latest version.**  
    Older versions of pip may not correctly handle Git-based installations:

    ```bash
    pip install --upgrade pip
    ```

-   **Ensure Git is installed.**  
    Since Structix is installed directly from a GitHub repository, you need Git installed and available in your system path.

-   **Use a Virtual Environment (Optional but Recommended).**  
    Setting up a Python virtual environment avoids conflicts between project dependencies:

    ```bash
    python3 -m venv structix-env
    source structix-env/bin/activate
    pip install git+https://github.com/structix-cli/structix.git
    ```

Using a virtual environment is highly recommended if you are managing multiple Python projects on the same machine.
