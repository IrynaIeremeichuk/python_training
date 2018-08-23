from selenium.webdriver.firefox.webdriver import WebDriver


class Group:

    driver = WebDriver()

    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer

    groups = driver.find_element_by_link_text("groups")
    group_page = driver.find_element_by_link_text("group page")
    new_group_button = driver.find_element_by_name("new")
    group_name = driver.find_element_by_name("group_name")
    group_header = driver.find_element_by_name("group_header")
    group_footer = driver.find_element_by_name("group_footer")
    submit_button = driver.find_element_by_name("submit")

    def go_to_groups_page(self):
        self.groups.click()

    def return_to_groups_page(self):
        self.group_page.click()

    def create_group(self):
        self.go_to_groups_page()
        self.new_group_button.click()
        self.group_name.click()
        self.group_name.click().clear()
        self.group_name.click().send_keys(self.name)
        self.group_header.click()
        self.group_header.clear()
        self.group_header.send_keys(self.header)
        self. group_footer.click()
        self.group_footer.clear()
        self.group_footer.send_keys(self.footer)
        self.submit_button.click()
        self.return_to_groups_page()
