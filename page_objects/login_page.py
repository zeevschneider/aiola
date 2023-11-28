from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from support.get_driver import GetDriver


class LoginPage(BasePage):

    @property
    def page_url(self):
        return f'{BasePage().base_url}/login'

    @property
    def customer_login_btn(self):
        return 'button.btn[ng-click="customer()"]'

    @property
    def manager_login_btn(self):
        return 'button.btn[ng-click="manager()"]'

    def is_loaded(self):
        driver = GetDriver().get_driver()
        wait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.customer_login_btn)))
