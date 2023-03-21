class Animals:
    def __init__(self, type_animal, name):
        self.type_animal = type_animal
        self.name = name

    def info_name(self):
        print(f'Я {self.type_animal}, по имени {self.name}')


class Cats(Animals):
    def __init__(self, name, age):
        super().__init__('кошка', name)
        self.name = name
        self.age = age

    def info(self):
        print(f'Я кошка по имени {self.name}, мне {self.age} лет')

    def sound(self):
        print('Мяу')


class Dogs(Animals):
    def __init__(self, name, age):
        super().__init__('собака', name)
        self.name = name
        self.age = age

    def info(self):
        print(f'Я собака по имени {self.name}, мне {self.age} лет')

    def sound(self):
        print('Гав')
