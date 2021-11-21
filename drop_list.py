import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    num1 = num1.text
    num2 = browser.find_element_by_id('num2')
    num2 = num2.text


    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(sum([int(num1),int(num2)])))  # ищем элемент с текстом "Python"


    submit = browser.find_element_by_class_name('btn-default')
    submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()