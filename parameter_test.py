from selenium import webdriver
import time
import pytest
import math
from selenium.webdriver.common.by import By


def ans():
    return math.log(int(time.time()))


url_list = [
'https://stepik.org/lesson/236895/step/1',
'https://stepik.org/lesson/236896/step/1',
'https://stepik.org/lesson/236897/step/1',
'https://stepik.org/lesson/236898/step/1',
'https://stepik.org/lesson/236899/step/1',
'https://stepik.org/lesson/236903/step/1',
'https://stepik.org/lesson/236904/step/1',
'https://stepik.org/lesson/236905/step/1',
]

text_msg = ''

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('url_list', url_list)
def test_link(browser, url_list):
    browser.get(url_list)
    input1 = browser.find_element(By.TAG_NAME, 'textarea')
    input1.send_keys(ans())
    click = browser.find_element(By.CLASS_NAME,'submit-submission')
    click.click()
    element_text = (browser.find_element(By.CLASS_NAME, 'smart-hints__hint')).text
    if element_text == 'Correct!':
        pass
    else:
        global text_msg
        text_msg += element_text
        print(text_msg)
    assert element_text == 'Correct!'

# def test_link(browser):
#     browser.get(url_list[0])
#     input1 = browser.find_element(By.TAG_NAME, 'textarea')
#     input1.send_keys(ans())
#     click = browser.find_element(By.CLASS_NAME,'submit-submission')
#     click.click()