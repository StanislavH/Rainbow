# объектно-ориентированное программирование
class Transport:
    def trans_method(self):
        print('это родительский метод')


class Auto(Transport):  # Класс Auto наследует атрибуты и методы класса Transport
    auto_name = 'GTR'  # атрибуты
    auto_model = '34'
    auto_year = 2020
    auto_count = 0

    def __init__(self):  # методы
        Auto.auto_name = 'вишневая семерка'
        Auto.auto_count = 1
        print(Auto.auto_count)

    def __method(self):  # __-знак инкапсуляции
        print('это приватный метод')

    def start_auto(self, auto_name, auto_model, auto_year):
        print('заводимся')
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        auto_count = 1
        if auto_name == 'GTR':
            print('заведем')
        else:
            print('взрыв атомной ракетной установки')

    def finish_auto(self):
        print('заглушили')

    def trans_method(self):  # переопределение метода-полиморфизм
        print('метод из класса авто')


A = Auto()  # объект(экземпляр)
print(A)
print(A.auto_name)
A.start_auto('GTR', '34', 2020)
A.trans_method()
print(A.auto_name)
