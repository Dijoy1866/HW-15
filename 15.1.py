#Задание 16
# Необходимо создать класс Human с атрибутами:
# name
# surname
# age
# phone
# address
# Атрибуты должны заполняться в методе __init__
#
# Так-же нужно написать методы:
# get_info() - который возвращает словарь в котором находится информация о человеке
# call(phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
# Нужно создать 3 обьекта класса Human и вызвать у них метод get_info

class Human:
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        result = {'name': f'{self.name}', 'surname': f'{self.surname}', 'age': f'{self.age}',
                  'phone': f'{self.phone}','address': f'{self.address}'}

        return result

    def call(self, phone_number):
        print(f'{self.phone} is calling {phone_number}')


petrov = Human('Petya', 'Petrov', 20, '+380930000000', 'Odessa, Ak. Korolova str., 15')
ivanov = Human('Vasya', 'Ivanov', 28, '+380631111111', 'Odessa, Komarova, str., 4')
zolotov = Human('Sahsa', 'Zolotov', 34, '+380952222222', 'Odessa, Levitana str., 35')

print(petrov.get_info())
print(ivanov.get_info())
print(zolotov.get_info())
