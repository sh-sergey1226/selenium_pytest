import math
from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)



    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    text = browser.find_element_by_class_name('form-control')
    text.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")

    checkbox.click()

    browser.execute_script("window.scrollBy(0, 200);")

    radiobuttons= browser.find_element_by_id("robotsRule")

    radiobuttons.click()

    submit = browser.find_element_by_class_name('btn-primary')

    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
