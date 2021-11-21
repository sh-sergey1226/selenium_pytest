import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id('treasure')
    x = treasure.get_attribute('valuex')
    y = calc(x)

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobuttons= browser.find_element_by_id("robotsRule")
    radiobuttons.click()

    submit = browser.find_element_by_class_name('btn-default')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()