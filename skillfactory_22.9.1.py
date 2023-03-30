# Функция для сортировки
def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array


# Функция для бинарного поиска
def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


try:
    # Вводим числа для списка и число для поиска в списке
    numbers = input('Введите целые числа через пробел\n').replace(' ', '')
    digit = int(input('Введите любое целое число\n'))
    # Приводим строку к списку с числами
    numbers = list(map(int, numbers))
    # Сортируем список
    numbers = qsort(numbers, 0, len(numbers) - 1)
    # Проверяем, что искомое число находится в списке
    if digit not in numbers:
        print("Указанное число не входит в диапазон списка")
    else:
        # С помощью алгоритма поиска находим индекс числа
        digit_index = binary_search(numbers, digit, 0, len(numbers))
        print(f'Индекс числа {digit} - {digit_index}')
    print(numbers)
except ValueError:
    print('Введите целое число')
