import os
import pytest

# Assuming you have a config module with URL_PRODUCTS defined
from config import Config,TestConfig
from main import get_config

@pytest.fixture
def mock_environment(monkeypatch):
    """
    Fixture to mock os.environ.get method to simulate different environments.
    """
    def mock_get(key):
        if key == 'ENVIRONMENT':
            return 'test'  # Set the environment to 'test' for testing
        return None  # Default value when key is not found
    monkeypatch.setattr(os.environ, 'get', mock_get)


def test_get_config_url(mock_environment):
    """
    Test URL construction based on environment.
    """
    ano = "2024"

    # Call get_config function
    config = get_config()
    

    if os.environ.get('ENVIRONMENT') == 'production':
        url = config.URL_PRODUCTS + ano
    else:
        url = config.URL_PRODUCTS

    # Assert URL based on environment
    assert url == config.URL_PRODUCTS


def test_ENVIRONMENT_value():

     # Call get_config function
    config = get_config()

    if os.environ.get('ENVIRONMENT') == 'production':
        url = config.URL_PRODUCTS + "2024"
        print(url)
    else:
        url = config.URL_PRODUCTS
        print(url)

    assert url == config.URL_PRODUCTS
