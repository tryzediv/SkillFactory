from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x, y):
    return x + y


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#num1').text
    y_element = browser.find_element(By.CSS_SELECTOR, '#num2').text
    result = calc(int(x_element), int(y_element))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))
    button = browser.find_element(By.CSS_SELECTOR, '.btn').click()
finally:
    time.sleep(5)
    browser.quit()
