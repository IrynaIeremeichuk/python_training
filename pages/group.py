from selenium.webdriver.firefox.webdriver import WebDriver


class Group:

    driver = WebDriver()

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer
