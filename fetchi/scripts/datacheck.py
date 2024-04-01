"""Checksum Script."""

import logging
from hashlib import md5

import requests
from rich.logging import RichHandler

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

log = logging.getLogger("rich")


def perform(
    baseurl: str = "http://0.0.0.0:8000",
    expectation: str = "66e1f14667b77ef1b358bb8dedbd3990",
) -> None:
    """Perform the data integrity check.

    Args:
        baseurl (str, optional): Defaults to "http://0.0.0.0:8000".
        expectation (str, optional): MD5 Checksum.
            Defaults to "66e1f14667b77ef1b358bb8dedbd3990".
    """
    log.info("Starting the data integrity check...")
    try:
        log.info("Pinging the server...")
        response = requests.get(f"{baseurl}/ping", timeout=1)
        response.raise_for_status()
        log.info(f"Recv: {response.json()}")
        log.info("Server is up, ✅")
        # Check server health
        log.info("Checking the server health...")
        response = requests.get(f"{baseurl}/__health__", timeout=1)
        response.raise_for_status()
        log.info(f"Recv: {response.json()}")
        log.info("Server is healthy, ✅")
        # GET the data.csv file
        log.info("Fetching data.csv file...")
        response = requests.get(f"{baseurl}/v1/fetch/data.csv", timeout=1)
        response.raise_for_status()
        log.info("data.csv file recieved, ✅")

        data = response.content
        # Calculate checksum of the data object
        log.info("Calculating md5 checksum...")
        checksum = md5(data, usedforsecurity=False).hexdigest()
        log.info(f"Checksum: {checksum}")

        if checksum == expectation:
            log.info("Checksum matched, ✅")
            log.info("Data integrity check verified.")
        else:
            log.error("Checksum mismatch, ❌")

    except requests.exceptions.RequestException as error:
        log.exception(error)


if __name__ == "__main__":
    perform()
