from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # Ожидаем пока цена будет ровна 100
    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
        )
    # Находим и нажимаем кнопку Book
    book = browser.find_element(By.ID, 'book')
    book.click()
    # Находим Х, решаем уравнение
    x_elem = browser.find_element(By.ID, 'input_value').text
    # Вводим результат в поле
    field = browser.find_element(By.ID, 'answer')
    field.send_keys(calc(int(x_elem)))
    # Находим и нажимаем кнопку Submit
    submit = browser.find_element(By.ID, 'solve')
    submit.click()
    # Выводим результат в консоль
    print(browser.switch_to.alert.text)

finally:
    browser.quit()
