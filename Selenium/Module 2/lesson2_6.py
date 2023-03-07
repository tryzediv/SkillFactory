from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x_elem = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    field = browser.find_element(By.CSS_SELECTOR, '.form-control')
    field.send_keys(calc(int(x_elem)))
    check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(5)
    browser.quit()
