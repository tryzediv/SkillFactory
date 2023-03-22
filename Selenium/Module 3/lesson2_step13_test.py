import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class RegistrationTest(unittest.TestCase):

    def test_page_1(self):
        # Ссылка на первую страницу
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)
        # Ищем поля и вставляем в них значения
        name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        name.send_keys('Bill')
        last_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        last_name.send_keys('Klinton')
        email = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        email.send_keys('qwe@qwe.qwe')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем соответствие ожидаемого и фактического результатов
        expected_text = "Congratulations! You have successfully registered!"
        fact_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(expected_text,
                         fact_text, "Should be equals registration text")

    def test_page_2(self):
        # Ссылка на вторую страницу
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        browser.implicitly_wait(5)
        # Ищем поля и вставляем в них значения
        name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[1]/input')
        name.send_keys('Bill')
        last_name = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[2]/input')
        last_name.send_keys('Klinton')
        email = browser.find_element(By.XPATH, '/html/body/div/form/div[1]/div[3]/input')
        email.send_keys('qwe@qwe.qwe')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем соответствие ожидаемого и фактического результатов
        expected_text = "Congratulations! You have successfully registered!"
        fact_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(expected_text,
                         fact_text, "Should be equals registration text")


if __name__ == "__main__":
    pytest.main()
