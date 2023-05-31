import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.etagi.com/"
min_price = 1000000
max_price = 3000000


@pytest.fixture
def browser():
    print("\nstart Chrome browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage:
    def test_smoke(self, browser):
        # Запоминаем главную страницу
        first_window = browser.window_handles[0]
        browser.get(link)
        # Выбираем в фильтре количество комнат - 1
        room_button = browser.find_element(
            By.XPATH, '//*[@id="wARPj2Cdgv"]/div[2]/div/div/div[1]/div[2]/div/div/button[2]'
        )
        room_button.click()
        # Вводим цену от
        price_ot = browser.find_element(
            By.XPATH, '//*[@id="wARPj2Cdgv"]/div[2]/div/div/div[1]/div[3]/div/div[2]/div[1]/div/input'
        )
        price_ot.send_keys(min_price)
        # Вводим цену до
        price_do = browser.find_element(
            By.XPATH, '//*[@id="wARPj2Cdgv"]/div[2]/div/div/div[1]/div[3]/div/div[2]/div[2]/div/input'
        )
        price_do.send_keys(max_price)
        # Нажимаем на кнопку "Найти"
        find_button = browser.find_element(
            By.XPATH, '//*[@id="wARPj2Cdgv"]/div[2]/div/div/div[2]/div[3]/a'
        )
        time.sleep(.5)
        find_button.click()
        time.sleep(2)

        first_flat = browser.find_element(
            By.XPATH, '//*[@id="object-list"]/div/div/div[1]/a/div/div[1]/div[1]'
        )
        second_flat = browser.find_element(
            By.XPATH, '//*[@id="object-list"]/div/div/div[2]/a/div/div[1]'
        )
        third_flat = browser.find_element(
            By.XPATH, '//*[@id="object-list"]/div/div/div[3]/a/div/div[1]/div[1]'
        )

        pages = [first_flat, second_flat, third_flat]
        page_counter = 1
        for page in pages:
            page.click()
            # Переходим на новую страницу
            new_window = browser.window_handles[page_counter]
            browser.switch_to.window(new_window)
            # Находим количество комнат
            room_text = browser.find_element(
                By.XPATH, '//*[@id="about"]/div[1]/div/div/div[2]/div/div/div/div[1]/span'
            )
            # Находим цену
            price = browser.find_element(
                By.XPATH, '//*[@id="about"]/div[1]/div/div/div[1]/div[1]/div[1]/span'
            ).text.replace(' ', '')
            # Сравниваем данные с условиями
            print(f'Старт теста {page_counter} квартиры')
            assert '1-комн. квартира' in room_text.text, f'{page_counter} Квартира. Не совпадает количество комнат'
            assert min_price <= int(price) <= max_price, f'{page_counter} Квартира. Не совпадает цена'
            print(f'Тест {page_counter} квартиры завершен')
            page_counter += 1
            browser.switch_to.window(first_window)
