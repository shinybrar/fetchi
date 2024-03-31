# Fetchi

Fetchi is a simple and lightweight HTTP Web Server written in Python to serve static files.

## Installation

**Note:** Fetchi requires Python 3.9+ to run. Make sure you have the correct version of Python installed on your system.

### From `zip` file

Download the `fetchi.zip` file from the [latest release](https://github.com/shinybrar/fetchi/releases). Extract the contents of the zip file and run the following command to install the package.

```bash
# Assuming MacOS or Linux Unzip the contents of the zip file
$ unzip fetchi.zip
```

### From `git` repository

Alternatively, you can also clone the respository using the `git`,

```bash
git clone https://github.com/shinybrar/fetchi.git
```

### Install the package

To install the package using `pip`, you can run the following command:

```bash
cd fetchi
pip install .
```

## Starting the Server

Once you have installed the package, you can start the server using one of the following methods,

### Command Line Interface

In order to start the server, you can use the `sanic` command from your terminal. After installation the package dependencies, the following command will start the server on port `8000` and serve the files from the `./fetchi/static/` folder.

```bash
cd /path/to/fetchi
sanic fetchi.server:app
```

### Docker Compose

If you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed on your machine, you can also use the `docker compose` to build and run the server in a containerized environment. The following command will start the server on port `8000` and serve the files from the `./fetchi/static/` folder.

```bash
cd /path/to/fetchi
docker-compose up
```

This will build the docker and start the server on port `8000`. You can change the port mapping in the `docker-compose.yml` file if you want to run the server on a different port

### Features

Once the server is running, you can access the following features,

- [x] [Download the contents of `data.csv`](http://0.0.0.0:8000/v1/fetch/data.csv)
- [x] [Directory Listing](http://0.0.0.0:8000/static/)
- [x] [System Health Check (GET /__health__)](http://0.0.0.0:8000/__health__)
- [x] [Server Ping (GET /ping)]  [http://0.0.0.0:8000/ping](http://0.0.0.0:8000/ping)
- [x] HTTP Endpoint Documentation
  - [x] [OpenAPI Documentation](http://0.0.0.0:8000/docs)
  - [x] [Swagger Documentation](http://0.0.0.0:8000/docs/swagger)

#### Future Work

- Harden the filename parameters checks to avoid directory traversal attacks by asserting that the filename is within the base directory.
- CORS Support
- HTTPS/TLS Support
- Implement fast Caching & Cache-Control
- Implement GZIP Compression
- Implement Authentication, e.g. Basic Auth, JWT, OAuth2 etc.
- Proxy Support
- Add more tests for the server

### Developer Setup

In order to setup the development environment, you need to have [Python 3.9+](https://www.python.org/downloads/release/python-3110/) or higher installed on your system. Additionally, this project uses [Poetry](https://python-poetry.org/) for dependency management, packaging, publishing and management of local development environments. To install `poetry` you find the instructions [here](https://python-poetry.org/docs/#installation).

Once you have `poetry` installed, you can clone the repository and install the dependencies using the following commands:


```bash
git clone https://github.com/shinybrar/fetchi.git
cd fetchi
poetry install --with dev
```

This will install the dependencies required for development and testing. You can run the tests using the following command:

```bash
poetry run pytest -v
```

Currently, we have tests to check the `ping` and `fetch` endpoints already implemented.