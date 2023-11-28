from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

from support.get_driver import GetDriver
from page_objects.login_page import LoginPage
from page_objects.select_customer_page import SelectCustomer
from page_objects.customer_account_page import CustomerAccountPage
from page_objects.transactions_page import TransactionsPage


def check_transactions(customer_name='Harry Potter', deposit='200', withdrawal='100'):
    """
        This method tests the following scenario:
            * Login to the app using the Harry Potter customer
            * Create two transactions:
                deposit 200 USD
                withdrawal 100 USD
            * Verify both transactions

    :return:
    """
    driver = GetDriver()
    lp = LoginPage()
    driver.driver.get(lp.page_url)
    lp.is_loaded()
    driver.driver.find_element(By.CSS_SELECTOR, lp.customer_login_btn).click()

    sc = SelectCustomer(customer_name)
    sc.is_loaded()
    sc.login_customer()
    ca = CustomerAccountPage()
    ca.is_loaded()
    driver.driver.find_element(By.CSS_SELECTOR, ca.transactions).click()
    ta = TransactionsPage()
    ta.is_loaded()
    # TODO - better assertion for empty transactions table
    try:
        driver.driver.find_element(By.CSS_SELECTOR, ta.transaction_record)
    except NoSuchElementException as e:
        print('Transactions table is empty')

    driver.driver.find_element(By.CSS_SELECTOR, ta.back_btn).click()
    ca.is_loaded()
    ca.account_deposit(deposit)
    # in order for the transaction to be recorded and shown in UI
    time.sleep(2)
    ca.account_withdrawal(withdrawal)
    time.sleep(2)
    driver.driver.find_element(By.CSS_SELECTOR, ca.transactions).click()
    ta.is_loaded()
    # assert transactions
    # TODO - create better assertion
    driver.driver.find_element(By.XPATH, f"//*[(text()= {deposit})]/following-sibling::td[text()='Credit']")
    driver.driver.find_element(By.XPATH, f"//*[(text()= {withdrawal})]/following-sibling::td[text()='Debit']")
    # TODO - can also check the balance after all transactions

    # TODO - think of a better solution for driver destruction
    driver.driver.quit()


check_transactions()



