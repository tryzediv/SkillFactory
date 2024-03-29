from api import PetFriends
from settings import *
from datetime import *
import pytest
import os

pf = PetFriends()


@pytest.fixture(autouse=True)
def time_delta():
    status, auth_key = PetFriends().get_api_key(valid_email, valid_password)
    if status == 200:
        print('API ключ получен')

    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(f"\nТест шел: {end_time - start_time}")


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200, f'Статус код - {status}'
    assert 'key' in result, 'Нет ключа в ответе'


def test_get_api_key_for_invalid_email(email=invalid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 при невалидном email"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403, f'Статус код - {status}'
    assert 'key' not in result, 'Есть ключ в ответе'


def test_get_api_key_for_invalid_password(email=valid_email, password=invalid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 при невалидном пароле"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403, f'Статус код - {status}'
    assert 'key' not in result, 'Есть ключ в ответе'


def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200, f'Статус код - {status}'
    assert len(result['pets']) > 0, 'Список питомцев пуст'


def test_get_all_pets_with_invalid_key(filter=''):
    """ Проверяем что запрос всех питомцев невозможен без ключа.
    Доступное значение параметра filter - 'my_pets' либо '' """

    auth_key = {'key': ''}
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 403, f'Статус код - {status}'
    assert 'Please provide &#x27;auth_key&#x27' in result, 'Нет сообщения об ошибке'


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/7723.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200, f'Статус код - {status}'
    assert result['name'] == name, 'Имя питомца не совпадает'


def test_add_new_pet_invalid_key(name='Я добавлен по ошибке', animal_type='Ошибка',
                                 age='1', pet_photo='images/7723.jpg'):
    """Проверяем что нельзя добавить питомца с пустым ключом, имя питомца в этом тесте не менять!"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    auth_key = {'key': ''}

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Получаем имя последнего успешно добавленного питомца
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "")
    last_pet_name = my_pets['pets'][0]['name']

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403, f'Статус код - {status}'
    assert 'Please provide &#x27;auth_key&#x27' in result, 'Нет сообщения об ошибке'
    assert name != last_pet_name, 'Получилось добавить питомца без ключа'


def test_add_new_pet_invalid_data_age(name='Меня добавили с неправильным возрастом', animal_type='двортерьер',
                                     age='qweert', pet_photo='images/7723.jpg'):
    """Проверяем что нельзя добавить питомца с некорректными данными (текст в возрасте)"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Получаем имя последнего успешно добавленного питомца
    _, my_pets = pf.get_list_of_pets(auth_key, "")
    last_pet_name = my_pets['pets'][0]['name']

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 403, f'Статус код - {status}, Получилось добавить питомца с невалидным возрастом'
    assert 'Please provide &#x27;auth_key&#x27' in result, 'Нет сообщения об ошибке'
    assert name != last_pet_name, 'Получилось добавить питомца с невалидным возрастом'


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200, f'Статус код - {status}'
        assert result['name'] == name, 'Имя питомца не совпадает'
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_update_alien_pet_info(name='Мурзик', animal_type='Котэ', age='99'):
    """Проверяем возможность обновления информации чужого питомца"""
    # Добавляем питомца со второго аккаунта
    _, alien_auth_key = pf.get_api_key(alien_email, alien_password)
    _, alien_pet = pf.new_pet_without_photo(alien_auth_key, name='Саня', animal_type='Рысь', age='4')
    alien_pet_id = alien_pet['id']

    # Получаем свой ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Пробуем обновить имя, тип и возраст чужого питомца
    status, result = pf.update_pet_info(auth_key, alien_pet_id, name, animal_type, age)

    # Получаем список всех питомцев
    _, all_pets = pf.get_list_of_pets(auth_key, filter='')

    # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
    assert status == 403, f'Статус код - {status}, возможно обновить данные чужого питомца'
    assert all_pets['pets'][0]['name'] != name, 'Чужой питомец имеет имя нашего питомца'


def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/7723.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200, f'Статус код - {status}'
    assert pet_id not in my_pets.values(), 'Питомец не удален'


def test_delete_alien_pet():
    """Проверяем возможность удаления чужого питомца"""

    # Добавляем питомца со второго аккаунта
    _, alien_auth_key = pf.get_api_key(alien_email, alien_password)
    _, alien_pet = pf.new_pet_without_photo(alien_auth_key, name='Мурка', animal_type='Корова', age='6')
    alien_pet_id = alien_pet['id']

    # Получаем наш ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Пытаемся удалить чужого питомца
    status, _ = pf.delete_pet(auth_key, alien_pet_id)

    # Получаем список всех питомцев
    _, all_pets = pf.get_list_of_pets(auth_key, filter='')

    # Проверяем что статус ответа = 403 и чужой питомец не удален
    assert status == 403, f'Статус код - {status}, возможно удалить чужого питомца'
    assert all_pets['pets'][0]['id'] == alien_pet_id, 'Чужой питомец удален'


def test_add_new_pet_without_photo_valid_data(name='Мурлок', animal_type='Кот', age='5'):
    """Проверяем что можно добавить питомца без фото с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200, f'Статус код - {status}'
    assert result['name'] == name, 'Имя питомца не совпадает'


def test_add_pet_photo(pet_photo='images/cat.jpg'):
    """Проверяем возможность добавления фото питомцу"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем имя и ID последнего добавленного питомца
    pet_id, name = my_pets['pets'][0]['id'], my_pets['pets'][0]['name']

    # Если список не пустой, то пробуем обновить фото
    if len(my_pets['pets']) > 0:
        status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200, f'Статус код - {status}'
        assert result['name'] == name, 'Имя питомца не совпадает'
    else:
        # если список питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")


def test_add_pet_photo_without_key(pet_photo='images/cat.jpg'):
    """Проверяем возможность добавления фото чужому питомцу"""

    # Получаем ключ auth_key, чтобы получить список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Сздаем пустой ключ
    auth_key = {'key': ''}

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Пробуем добавить фото с пустым ключом
    status, result = pf.add_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

    # Проверяем что статус ответа = 403
    assert status == 403, f'Статус код - {status}, возможно изменить фото с пустым ключом'
    assert 'Please provide &#x27;auth_key&#x27' in result, 'Нет сообщения об ошибке'