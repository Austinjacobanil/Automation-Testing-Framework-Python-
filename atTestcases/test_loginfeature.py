import pytest

from atPages.LoginPage import LoginPage
from conftest import *


@pytest.mark.usefixtures("browser_setup")
class Test_login:

    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)


    def test_valid_login(self):
        self.login_page.login(Username, Password)

    def teardown_class(self):
        self.driver.quit()
