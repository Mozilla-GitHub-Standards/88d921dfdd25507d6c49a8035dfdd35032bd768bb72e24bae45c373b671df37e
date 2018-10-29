# Configuration file for running post-deployment tests for Megaphone
import os
import pytest
import ssl

# Hack because of how SSL certificates are verified by default in Python
if hasattr(ssl, "_create_unverified_context"):
    ssl._create_default_https_context = ssl._create_unverified_context


@pytest.fixture(scope="module")
def endpoint():
    return os.environ["ENDPOINT"]


@pytest.fixture(scope="module")
def bearer_token():
    return os.environ["BEARER_TOKEN"]


@pytest.fixture(scope="module")
def ws_endpoint():
    return os.environ["WS_ENDPOINT"]
