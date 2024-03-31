# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Set the working directory
# Setup Environment Variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=true \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    DEBIAN_FRONTEND=noninteractive

# Setup Shell for the Docker Image
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

COPY . /fetchi
WORKDIR /fetchi

# Install the required packages
RUN pip install .

EXPOSE 8000

CMD ["sanic", "fetchi.server:app"]
