from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BankingApp:
    def __init__(self, driver):
        self.driver = driver

    def login(self, base_url, username, password):
        self.driver.get(base_url)
        self.driver.find_element(By.ID, 'username').send_keys(username)
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-btn').click()

    def navigate_to_transactions(self):
        # Navigate to the transactions page
        transactions_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'transactions-link'))
        )
        transactions_link.click()

    def perform_transaction(self, amount):
        # Example: Perform a fund transfer
        transaction_amount_input = self.driver.find_element(By.ID, 'transaction-amount')
        transaction_amount_input.clear()  # Clear any pre-existing value
        transaction_amount_input.send_keys(str(amount))
        self.driver.find_element(By.ID, 'confirm-transaction-btn').click()

    def is_transaction_successful(self):
        try:
            success_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'transaction-success-message'))
            )
            return success_message.is_displayed()
        except:
            return False

    def is_insufficient_funds_error_displayed(self):
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'insufficient-funds-error'))
            )
            return error_message.is_displayed()
        except:
            return False
