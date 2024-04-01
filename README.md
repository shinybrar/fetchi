[![Continous Deployment](https://github.com/shinybrar/fetchi/actions/workflows/deployment.yml/badge.svg)](https://github.com/shinybrar/fetchi/actions/workflows/deployment.yml) [![Continous Integration](https://github.com/shinybrar/fetchi/actions/workflows/integration.yml/badge.svg)](https://github.com/shinybrar/fetchi/actions/workflows/integration.yml)

# Fetchi

Fetchi is a simple and lightweight HTTP Web Server written in Python to serve static files.

- [Fetchi](#fetchi)
  - [Installation](#installation)
    - [From `zip` file](#from-zip-file)
    - [From `git` repository](#from-git-repository)
    - [Install the package](#install-the-package)
  - [Starting the Server](#starting-the-server)
    - [Command Line Interface](#command-line-interface)
    - [Docker Compose](#docker-compose)
  - [Detailed Explanations](#detailed-explanations)
    - [Technologies Used](#technologies-used)
    - [Future Work](#future-work)
  - [Developer Setup](#developer-setup)
  - [Testing Deployed Server](#testing-deployed-server)

## Installation

**Note:** Fetchi requires Python 3.9+ to run. Make sure you have the correct version of Python installed on your system.

### From `zip` file

Download the `zipfile` file from the [latest releases](https://github.com/shinybrar/fetchi/releases). Extract the contents of the zip file and run the following command to install the package.

```bash
# Assuming MacOS or Linux Unzip the contents of the zip file
$ unzip vX.X.X.zip
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
sanic fetchi.server:app --host 0.0.0.0 --port 8000
```

You can also change the port number and the host address to run the server on a different port or IP address.

### Docker Compose

If you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed on your machine, you can also use the `docker compose` to build and run the server in a containerized environment. The following command will start the server on port `8000` and serve the files from the `./fetchi/static/` folder.

```bash
cd /path/to/fetchi
docker compose up
```

This will build the docker and start the server on port `8000`. You can change the port mapping in the `docker-compose.yml` file if you want to run the server on a different port

## Detailed Explanations

This codebase uses the Python `Sanic` framework to create a simple HTTP server that serves static files. The server is asynchronous and can be scaled very easily by running multiple workers to handle the incoming requests concurrently by appending a `--workers 4` flag to the `sanic` command. The server by default provides support for HTTP/1.1 protocol defined in RFC 9110, with features such as content negotiation, disposition, range and cache control for files. Though, in this implementation, we have not implemented caching and compression, but it can be easily added to the server.

By default, all files under the `./fetchi/static/` directory are served by the server. The server exposes a single endpoint `/v1/fetch/<filename>` that allows users to download the contents of the file specified by the `<filename>` parameter. If the file is not found, the server returns a `404 Not Found` error, and if the file is found, but is not readable, the server returns a `403 Forbidden` error. Finally if the file is found and is readable, the server returns the contents of the file with a `200 OK` status code.

The server also exposes a `/ping` endpoint that returns a `200 OK` status code to indicate that the server is running. Additionally, the server also exposes a `/__health__` endpoint that returns a `200 OK` status code with a JSON response to indicate that the server is healthy.

The server provides directory listing of all files in the `./fetchi/static/` directory. The directory listing is accessible at the `/static/` endpoint and provides a simple HTML page with links to the files in the directory.

![image](https://github.com/shinybrar/fetchi/assets/4196481/c916f109-85a4-4d18-89e6-7ba078e86497)


The server also provides OpenAPI and Swagger documentation for the HTTP endpoints. The OpenAPI documentation is accessible at the `/docs` endpoint, and the Swagger documentation is accessible at the `/docs/swagger` endpoint.

![image](https://github.com/shinybrar/fetchi/assets/4196481/397b8413-7d7b-4449-929e-621a3b2760ec)


Once the server is running, you can access the following all the endpoints using the following URLs (assuming the server is running on `http://0.0.0.0:8000`):

- [x] [Download the contents of `data.csv`](http://0.0.0.0:8000/v1/fetch/data.csv)
- [x] [Directory Listing](http://0.0.0.0:8000/static/)
- [x] [System Health Check (GET /__health__)](http://0.0.0.0:8000/__health__)
- [x] [Server Ping (GET /ping)](http://0.0.0.0:8000/ping)
- [x] HTTP Endpoint Documentation
  - [x] [OpenAPI Documentation](http://0.0.0.0:8000/docs)
  - [x] [Swagger Documentation](http://0.0.0.0:8000/docs/swagger)

### Technologies Used

- [Sanic](https://sanicframework.org/) - Sanic is a Python 3.8+ web server and web framework. It allows the usage of the async/await syntax which makes it non-blocking and speedy.
- [Poetry](https://python-poetry.org/) - Poetry is a tool for dependency management and packaging in Python. It manages project dependencies as well virtual environments for development and testing.
- Docker (Dockerfile + compose.yml) - This repository uses Docker to containerize the server and run it in a containerized environment. The `Dockerfile` contains the instructions to build the server image, and the `compose.yml` file contains the configuration to run the server in a containerized environment.
- Pre Commit Hooks- A framework for managing and maintaining multi-language pre-commit hooks. This repository uses `black`, `isort`, `flake8`, `mypy`, `committizen`, etc. as pre-commit hooks to ensure code quality and consistency.
- GitHub Actions Support - This repository uses GitHub Actions for Continuous Integration and Continuous Deployment. There are two workflows defined in the `.github/workflows` directory: `deployment.yml` and `integration.yml`. The `deployment.yml` workflow is triggered when a new commit is pushed to the `main` branch and it checks previous commit messages to determine the version bump. The `integration.yml` workflow is triggered when either a pull request is opened or updated against the `main` branch or when a new commit is pushed to the `main` branch. It runs the tests included with this repository to ensure the code quality and consistency.

### Future Work

- Harden the filename parameters checks to avoid directory traversal attacks by asserting that the filename is within the base directory.
- CORS Support
- HTTPS/TLS Support
- Implement Cache-Control
- Implement GZIP Compression
- Implement Authentication, e.g. Basic Auth, JWT, OAuth2 etc.
- Add more tests for the server

## Developer Setup

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

## Testing Deployed Server

Even though we have included offline tests for the server to run locally and during CI/CD, you can also test the deployed server using various tools like `curl`, `httpie`, `postman`, `insomnia` etc. While most of these tools accelerate deployment testing for teams, the simplest way to test the server is using `curl` and validating if the `data.csv` file is being served correctly and matches the expected content.

Assuming that the server is running on `http://0.0.0.0:8000`, you can run the following command to test the server:

```bash
curl -O http://0.0.0.0:8000/v1/fetch/data.csv
```

This will download the `data.csv` file from the server and save it in the current directory. You can then compare the contents of the file with the expected content. To compare the contents, the simplest way is to compare the `md5` hash of the file with the expected hash. You can run the following command to get the `md5` hash of the file:

```bash
md5 data.csv
MD5 (data.csv) = 66e1f14667b77ef1b358bb8dedbd3990
```

Additionally, there is also a commandline tools included with this repository that allows you to verify the contents of the file served by the server. You can run the following command to verify the contents of the file:

```bash
fetchi-md5check
```

This script will ping the server, then verify that its healthy and finally download the `data.csv` file and compare its md5checksum with the expected checksum of the files in the `./fetchi/static/data.csv` directory. Upon running the script, you should see the following output:

```bash
$ fetchi-md5check
[20:58:25] INFO     Starting the data integrity check...                                                                                                    datacheck.py:29
           INFO     Pinging the server...                                                                                                                   datacheck.py:31
           INFO     Recv: {'message': 'pong'}                                                                                                               datacheck.py:34
           INFO     Server is up, ✅                                                                                                                        datacheck.py:35
           INFO     Checking the server health...                                                                                                           datacheck.py:37
           INFO     Recv: {'Sanic-Main': {'pid': 5145}, 'Sanic-Server-0-0': {'server': True, 'state': 'ACKED', 'pid': 5152, 'start_at':                     datacheck.py:40
                    '2024-04-01T00:45:48.234100+00:00', 'starts': 1, 'serving': True}, 'Sanic-HealthMonitor-0': {'server': False, 'state': 'STARTED',
                    'pid': 5153, 'start_at': '2024-04-01T00:45:48.236527+00:00', 'starts': 1}}
           INFO     Server is healthy, ✅                                                                                                                   datacheck.py:41
           INFO     Fetching data.csv file...                                                                                                               datacheck.py:43
           INFO     data.csv file recieved, ✅                                                                                                              datacheck.py:46
           INFO     Calculating md5 checksum...                                                                                                             datacheck.py:50
           INFO     Checksum: 66e1f14667b77ef1b358bb8dedbd3990                                                                                              datacheck.py:52
           INFO     Checksum matched, ✅                                                                                                                    datacheck.py:55
           INFO     Data integrity check verified.
```
