import pytest
from playwright.sync_api import Page, Playwright
from unittest.mock import patch

@pytest.fixture
def board():
    """Proporciona un tablero de Tic-Tac-Toe limpio ([' ']*10) para cada prueba."""
    # Nota: Es crucial que el índice 0 no se use.
    return [' '] * 10

@pytest.fixture(scope="session", autouse=True)
def setup_session_data():
    """Crea un diccionario global en el módulo pytest para compartir datos entre steps."""
    # Pytest nos permite añadir atributos al módulo 'pytest'
    pytest.test_session_data = {}



# Fixture to hold the sequence of inputs for the mock
@pytest.fixture
def mock_inputs_list():
    """Placeholder for the list of strings to feed to the mocked input() function."""
    return []

# Fixture that handles the mocking of the built-in input() function
@pytest.fixture(scope="function", autouse=True)
def patch_input(mock_inputs_list):
    """
    Temporarily replaces the built-in input() function with a mock object
    that returns values from mock_inputs_list.
    """
    # The 'side_effect' receives the list of inputs for the test
    with patch('builtins.input', side_effect=mock_inputs_list) as mock_obj:
        yield mock_obj
