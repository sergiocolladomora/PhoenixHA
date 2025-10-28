import pytest
from playwright.sync_api import Page, Playwright

class ScenarioContext:
    """Simple class to store shared data during a scenario."""
    def __init__(self):
        self.idPedidos: list[str] = [] 
        self.featureFilePath: str = "" 

@pytest.fixture
def scenario_context() -> ScenarioContext:
    """Fixture that provides a clean context for each function/scenario."""
    return ScenarioContext()

@pytest.fixture
def order_factory():
    """
    Fixture that simulates the order creation function (orderFactory).
    Used as a mock or a default implementation.
    """
    def factory_function(status: str) -> str:
        raise NotImplementedError(f"The 'order_factory' has not been implemented for this project. Requested status: {status}")
    
    return factory_function