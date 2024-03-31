# Fetchi `フェッチ`

Fetchi is a simple and lightweight HTTP Web Server written in Python to serve static files.

## Features

- [x] Serve Static Files
- [x] Directory Listing: [http://0.0.0.0:8000/static/](http://0.0.0.0:8000/static/)
- [x] Health Check (GET/__health__) [http://0.0.0.0:8000/__health__](http://0.0.0.0:8000/__health__)
- [x] Server Ping (GET /ping) [http://0.0.0.0:8000/ping](http://0.0.0.0:8000/ping)
- [x] HTTP Endpoint Documentation
  - [x] [OpenAPI Documentation](http://0.0.0.0:8000/docs)
  - [x] [Swagger Documentation](http://0.0.0.0:8000/docs/swagger)
- [x] Docker Support

## Installation

**Note:** Fetchi requires Python 3.9+ to run. Make sure you have the correct version of Python installed on your system.

### From `pip`

```bash
pip install --user fetchi
```

### From `zip` file

Download the `fetchi.zip` file from the [latest release](https://github.com/shinybrar/fetchi/releases). Extract the contents of the zip file and run the following command to install the package.

```bash
# Assuming MacOS or Linux Unzip the contents of the zip file
$ unzip fetchi.zip
```

Install the package using `pip`:

```bash
cd fetchi
pip install .
```

## Starting the Server

### Command Line Interface

In order to start the server, you can use the `sanic` command. After installation the package dependencies, the following command will start the server on port `8000` and serve the files from the `./fetchi/static/` folder.

```bash
cd /path/to/fetchi
sanic fetchi.server:app
```

### Docker Compose

If you have `Docker for Desktop` installed on your system, you can use the `docker compose` to start the server.

```bash
cd /path/to/fetchi
docker-compose up
```

This will build the docker and start the server on port `8000`.

## Technical Details


### Future Features

- Harden the filename parameters checks to avoid directory traversal attacks by asserting that the filename is within the base directory.
- CORS Support
- HTTPS/TLS Support
- Implement fast Caching & Cache-Control
- Implement GZIP Compression
- Implement Authentication, e.g. Basic Auth, JWT, OAuth2 etc.

### Developer Setup

In order to setup the development environment, you need to have [Python 3.9+](https://www.python.org/downloads/release/python-3110/) or higher installed on your system. Additionally, this project uses [Poetry](https://python-poetry.org/) for dependency management, packaging, publishing and management of local development environments. To install `poetry` you find the instructions [here](https://python-poetry.org/docs/#installation).
