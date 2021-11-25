
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_backet_click(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    try:
        click = browser.find_element(By.CLASS_NAME,'btn-add-to-basket')
    except NoSuchElementException:
        click = None
    assert click is not None, 'element not found'

