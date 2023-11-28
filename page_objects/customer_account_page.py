from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from support.get_driver import GetDriver


class CustomerAccountPage(BasePage):
    def __init__(self):
        self.driver = GetDriver().get_driver()

    @property
    def page_url(self):
        return f'{BasePage().base_url}/account'

    # TODO - add property for welcome + name

    @property
    def transactions(self):
        return 'button.btn[ng-click="transactions()"]'

    @property
    def deposit(self):
        return 'button.btn[ng-click="deposit()"]'

    @property
    def withdrawal(self):
        return 'button.btn[ng-click="withdrawl()"]'

    @property
    def amount(self):
        return 'input[ng-model="amount"]'

    @property
    def submit_button(self):
        return 'button.btn[type="submit"]'

    # TODO - add success messages properties

    def account_deposit(self, amount):
        self.driver.find_element(By.CSS_SELECTOR, self.deposit).click()
        wait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.amount)))
        self.driver.find_element(By.CSS_SELECTOR, self.amount).send_keys(amount)
        self.driver.find_element(By.CSS_SELECTOR, self.submit_button).click()
        # TODO - verify success message

    def account_withdrawal(self, amount):
        self.driver.find_element(By.CSS_SELECTOR, self.withdrawal).click()
        wait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.amount)))
        self.driver.find_element(By.CSS_SELECTOR, self.amount).send_keys(amount)
        self.driver.find_element(By.CSS_SELECTOR, self.submit_button).click()
        # TODO - verify success message

    def is_loaded(self):
        wait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.deposit)))

    # TODO - add properties for the account_number, balance and currency labels
    # TODO - add property for the account_number selector
