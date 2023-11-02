# cmdutil 

This is a command line utility written in Python that performs os functions

## Usage

To use this utility, run the following command:

Uninstalled

```bash
python -m cmdutil.cli checkport 80
```

Installed

```bash
pip install -U git+https://github.com/adjscent/cmdutil@master
cmdutil checkport 80
```

Uninstall

```bash
pip uninstall cmdutil
```

## Supported commands

- checkport [port] (checks for a local process listening to the port)