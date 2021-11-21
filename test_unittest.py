import unittest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):

    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.first_block > div.form-group.first_class > input')
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR,
            'body > div > form > div.first_block > div.form-group.second_class > input')
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR,
            'body > div > form > div.first_block > div.form-group.third_class > input')
        input3.send_keys("IvanPetrov@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, '')


    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, 'body > div > form > div.first_block > div.form-group.first_class > input')
        input1.send_keys("Ivan")

        input2 = browser.find_element(By.CSS_SELECTOR,
            'body > div > form > div.first_block > div.form-group.second_class > input')
        input2.send_keys("Petrov")

        input3 = browser.find_element(By.CSS_SELECTOR,
            'body > div > form > div.first_block > div.form-group.third_class > input')
        input3.send_keys("IvanPetrov@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, '')

if __name__ == "__main__":
    unittest.main()