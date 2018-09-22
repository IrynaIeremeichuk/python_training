from selenium import webdriver
from pytest import mark
from selenium.webdriver.common.by import By

@mark.multi
def test_button_text_verification():
    base_url = "https://www.multitran.ru/"
    wd = webdriver.Chrome()
    wd.get(base_url)
    element = wd.find_element(By.CSS_SELECTOR, 'input#s')
    result = element.get_attribute("type")
    assert result == "text"

