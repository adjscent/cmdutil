# cmdutil 
[![Python Package CI](https://github.com/adjscent/cmdutil/actions/workflows/python-package-ci.yml/badge.svg)](https://github.com/adjscent/cmdutil/actions/workflows/python-package-ci.yml)

This is a command line utility written in Python that performs os functions

## Usage

To use this utility, run the following command:

Uninstalled

```bash
python -m cmdutil.cli checkport 80
```

Installed

```bash
pip install -U -e git+https://github.com/adjscent/cmdutil@master
cmdutil checkport 80
```

Update

```bash
pip uninstall cmdutil
pip install -U -e git+https://github.com/adjscent/cmdutil@master
```

Uninstall

```bash
pip uninstall cmdutil
```

## Supported commands

- checkport [port] (checks for a local process listening to the port)
- memory (checks for memory usage)
- process (checks for current processes)


## Development

To develop this utility, run the following command to install dependencies:

```bash
make install-dev
```

To lint this utility, run the following command:

```bash
make lint
```