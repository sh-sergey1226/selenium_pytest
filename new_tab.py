import math

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element_by_class_name('btn-primary')
    submit.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    text = browser.find_element_by_id('answer')
    text.send_keys(y)

    submit = browser.find_element_by_class_name('btn-primary')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()