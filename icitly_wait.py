import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    # browser.implicitly_wait(5)
    browser.get(link)

    button = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    submit = browser.find_element_by_id('book')
    submit.click()

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    text = browser.find_element_by_id('answer')
    text.send_keys(y)

    submit = browser.find_element_by_id('solve')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()