from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from support.get_driver import GetDriver
from selenium.webdriver.support.select import Select


class SelectCustomer(BasePage):
    def __init__(self, customer_name):
        self.driver = GetDriver().get_driver()
        self.customer_name = customer_name

    @property
    def page_url(self):
        return f'{BasePage().base_url}/customer'

    @property
    def customers_selector(self):
        return 'userSelect'

    def is_loaded(self):
        wait(self.driver, 2).until(EC.presence_of_element_located((By.ID, self.customers_selector)))

    @property
    def login_btn(self):
        return 'button.btn[type="submit"]'

    def select_customer(self):
        customer = Select(self.driver.find_element(By.ID, self.customers_selector))
        customer.select_by_visible_text(self.customer_name)

    def login_customer(self):
        self.select_customer()
        self.driver.find_element(By.CSS_SELECTOR, self.login_btn).click()


