import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *

link = "https://petfriends.skillfactory.ru/"


@pytest.fixture
def browser():
    print("\nstart Chrome browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    # Неявное ожидание
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture
def authorization(browser):
    # Фикстура для авторизации
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, registryButton).click()
    browser.find_element(By.CSS_SELECTOR, haveAccount).click()
    browser.find_element(By.CSS_SELECTOR, emailField).send_keys(email)
    browser.find_element(By.CSS_SELECTOR, passwordField).send_keys(password)
    browser.find_element(By.CSS_SELECTOR, enterButton).click()
    # Явное ожидание
    WebDriverWait(browser, 5).until(
        EC.title_contains("PetFriends: My Pets"))


class TestPetFriends:
    def test_my_pets(self, browser, authorization):
        browser.find_element(By.CSS_SELECTOR, myPets).click()
        # Проверяем, что мы на странице с нашими питомцами
        assert browser.find_element(By.CSS_SELECTOR, userName).text == name,\
            'Неправильный юзернейм, ошибка авторизации'

        all_pets = browser.find_element(By.CSS_SELECTOR, petsQuantity).text
        all_pets = int(all_pets.strip().split()[-5])
        pets_names = browser.find_elements(By.XPATH, cardNames)
        # 1. Присутствуют все питомцы
        assert all_pets == len(pets_names), 'Количество питомцев не совпадает'

        pets_images = browser.find_elements(By.XPATH, cardImages)
        pets_breed = browser.find_elements(By.XPATH, cardBreed)
        pets_age = browser.find_elements(By.XPATH, cardAge)
        pets_with_images = 0
        unique_names = []
        for i in range(len(pets_names)):
            if pets_images[i].get_attribute('src'):
                pets_with_images += 1
            if pets_names[i].text not in unique_names:
                unique_names.append(pets_names[i].text)
        # 2. Хотя бы у половины питомцев есть фото
        assert pets_with_images >= all_pets / 2, 'Меньше половины питомцев имеют фото'
        # 3. У всех питомцев есть имя, возраст и порода
        assert len(pets_names) == all_pets, 'Не у всех питомцев есть имя'
        assert len(pets_breed) == all_pets, 'Не у всех питомцев есть порода'
        assert len(pets_age) == all_pets, 'Не у всех питомцев есть возраст'
        # 4. У всех питомцев разные имена
        assert len(unique_names) == len(pets_names), 'Не у всех питомцев уникальное имя'

        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, petsCard))
        )
        pets_cards = browser.find_elements(By.CSS_SELECTOR, petsCard)
        all_pets_info = []
        for i in pets_cards:
            all_pets_info.append(i.text)
        # 5. В списке нет повторяющихся питомцев
        assert len(set(all_pets_info)) == all_pets, 'В списке есть повторяющиеся питомцы'
