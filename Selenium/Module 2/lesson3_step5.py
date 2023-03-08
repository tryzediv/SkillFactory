from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x_elem = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    field = browser.find_element(By.CSS_SELECTOR, '#answer')
    field.send_keys(calc(int(x_elem)))
    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit.click()
    print(browser.switch_to.alert.text)

finally:
    browser.quit()
