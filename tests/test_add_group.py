from selenium.webdriver.firefox.webdriver import WebDriver
from application import Application
import pytest
from pages.group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.quit_browser())
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    group = Group(name="Group 1", header="Header 1", footer="Footer 1")
    group.create_group()
    app.logout()
