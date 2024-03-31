# Fetchi [フェッチ]

Fetchi is a simple and lightweight HTTP Web Server written in Python to serve static files.

## Installation

**Note:** Fetchi requires Python 3.9 or higher.

### From `pip`

```bash
pip install --user fetchi
```

### From `zip` file

Download the `fetchi.zip` file from the [latest release](). Extract the contents of the zip file and run the following command to install the package.

```bash
# Assuming MacOS or Linux

# Unzip the contents of the zip file
$ unzip fetchi.zip
```

Install the package using `pip`:

```bash
cd fetchi
pip install .
```

## Technical Details

### Tools and Libraries

### Future Features

- Harden the filename parameters checks to avoid directory traversal attacks by asserting that the filename is within the base directory.
- ADD CORS support
- ADD HTTPS/TLS support

### Developer Setup

In order to setup the development environment, you need to have [Python 3.9+](https://www.python.org/downloads/release/python-3110/) or higher installed on your system. Additionally, this project uses [Poetry](https://python-poetry.org/) for dependency management, packaging, publishing and management of local development environments. To install `poetry` you find the instructions [here](https://python-poetry.org/docs/#installation).
