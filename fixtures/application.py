from selenium.webdriver.firefox.webdriver import WebDriver
from fixtures.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook")

    def quit_browser(self):
        self.wd.quit()
