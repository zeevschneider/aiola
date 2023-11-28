from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from support.get_driver import GetDriver


class TransactionsPage(BasePage):
    @property
    def page_url(self):
        return f'{BasePage().base_url}/listTx'

    @property
    def back_btn(self):
        return 'button.btn[ng-click="back()"]'

    @property
    def reset_btn(self):
        return 'button.btn[ng-click="reset()"]'

    @property
    def from_date(self):
        return 'input#start'

    @property
    def to_date(self):
        return 'input#end'

    @property
    def date_time_column(self):
        return "table.a[href='#']"

    @property
    def amount_column(self):
        return "ng-binding:nth-child(2)"

    @property
    def transaction_type_column(self):
        return "ng-binding:nth-child(3)"


    @property
    def transaction_record(self):
        return 'table > tbody > tr > td'
    def is_loaded(self):
        driver = GetDriver().get_driver()
        wait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.reset_btn)))
