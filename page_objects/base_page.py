class BasePage:
    @property
    def base_url(self):
        return 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#'

    @property
    def home_button(self):
        return 'btn home'

    @property
    def logout_button(self):
        return 'btn logout'

    def is_loaded(self):
        pass
