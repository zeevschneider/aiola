from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


@singleton
class GetDriver:
    """
        Creates one and only instance of web_driver to be used across a test
    """
    def __init__(self, driver_name='chrome'):
        if driver_name == 'chrome':
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def get_driver(self):
        return self.driver
