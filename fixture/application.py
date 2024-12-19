from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.ui import Select
#from selenium.webdriver import Chrome


class Application:
    def __init__(self):
        self.app = Application
        self.wd = WebDriver()#webdriver.Chrome()
        self.Select = Select
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

