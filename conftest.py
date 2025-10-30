import pytest
from playwright.sync_api import Page, Playwright
from unittest.mock import patch


@pytest.fixture
def board():
    """Provides a clean Tic-Tac-Toe board for each test."""
    # index 0 is not used as the player chooses positions 1-9
    return [' '] * 10


@pytest.fixture(scope="session", autouse=True)
def setup_session_data():
    """Creates a global library in pytest to share data between steps."""
    pytest.test_session_data = {}


@pytest.fixture
def mock_inputs_list():
    """Creates a placeholder for the list of strings to feed to the mocked input() function."""
    return []


@pytest.fixture(scope="function", autouse=True)
def patch_input(mock_inputs_list):
    """
    Temporarily replaces the built-in input() function with a mock object
    that returns values from mock_inputs_list.
    """
    # The 'side_effect' receives the list of inputs for the test
    with patch('builtins.input', side_effect=mock_inputs_list) as mock_obj:
        yield mock_obj
