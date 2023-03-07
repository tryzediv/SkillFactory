from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

file = open('file.txt', 'w')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    name_f = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]')
    name_f.send_keys('Oleg')
    lastname_f = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]')
    lastname_f.send_keys('Gazmanov')
    email_f = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]')
    email_f.send_keys('gaz@gazov.ru')
    add_file = browser.find_element(By.XPATH, '//*[@id="file"]')
    add_file.send_keys(file_path)
    button = browser.find_element(By.XPATH, '/html/body/div/form/button')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
    file.close()
