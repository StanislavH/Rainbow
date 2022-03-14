# объектно-ориентированное программирование
class Transport:
    def trans_method(self):
        print('это родительский метод')


class Auto(Transport):  # класс Auto наследует атрибуты и методы класса Transport
    auto_count = 0  # атрибуты
    auto_name = 'BMW'
    auto_model = 'M3 GTR'
    auto_year = 2008

    def __init__(self):  # методы
        auto_count = 0
        auto_name = 'ЗАПОРОЖЕЦ'
        print(Auto.auto_count)

    def __method(self):  # __ - знак инкапсуляции
        print('это приватный метод!')

    def start_auto(self, auto_name, auto_model, auto_year):
        print('ЗАВОДИ')
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        auto_count = 1
        if auto_name == 'BMW':
            print('завести')
        else:
            print('КБУМ!!!')

    def finish_auto(self):
        print('откис')
        print(A.auto_name)

    def trans_method(self):  # переопределение метода-полиморфизм
        print("метод из класса авто")


A = Auto()  # объект(экземпляры)
print(A)
print(A.auto_name)
A.start_auto('BMW', 'M3 GTR', 2008)
A.trans_method()
print(A.auto_name)
