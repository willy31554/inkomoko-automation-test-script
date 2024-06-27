import pytest
from pages.banking_app import BankingApp
from utils.selenium_utils import setup_driver
from data.test_data import valid_transaction_data, invalid_transaction_data
from utils.config import get_base_url

@pytest.fixture(scope="module")
def driver():
    driver = setup_driver()
    yield driver
    driver.quit()

base_url = get_base_url()

@pytest.mark.parametrize("transaction_data", valid_transaction_data)
def test_successful_transaction(driver, transaction_data):
    app = BankingApp(driver)
    app.login(base_url, "username", "password")  # Replace with actual credentials from environment variables
    app.navigate_to_transactions()
    
    # Perform transaction with valid data
    app.perform_transaction(transaction_data['amount'])

    # Validate transaction success
    assert app.is_transaction_successful()

@pytest.mark.parametrize("transaction_data", invalid_transaction_data)
def test_invalid_transaction(driver, transaction_data):
    app = BankingApp(driver)
    app.login(base_url, "username", "password")  # Replace with actual credentials from environment variables
    app.navigate_to_transactions()
    
    # Perform transaction with invalid data
    app.perform_transaction(transaction_data['amount'])

    # Validate insufficient funds error
    assert app.is_insufficient_funds_error_displayed()

if __name__ == "__main__":
    pytest.main()
