# объектно-ориентированное программирование
class Transport:
    def trans_method(self):
        print('это родительский метод')


class Auto(Transport):  # класс Auto наследует атрибуты и методы класса Transport
    auto_count = 0  # атрибуты
    auto_name = 'автобот'
    auto_model = 'оптимус прайм'
    auto_year = 10

    def __init__(self):  # методы
        Auto.auto_name = 'человек паук'
        Auto.auto_count += 1
        print(Auto.auto_count)

    def __method(self):  # __ - знак инкапсуляции
        print('это приватный метод!')

    def start_auto(self, auto_name, auto_model, auto_year):
        print("стартуем")
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        auto_count = 1
        if auto_name == 'человек паук':
            print('человек паук выходи гулять')
        else:
            print('аллах акбар')

    def finish_auto(self):
        print('откис')

    def trans_method(self):  # переопределение метода-полиморфизм
        print("метод из класса авто")


A = Auto()  # объект(экземпляр)
print(A)
print(A.auto_name)
A.start_auto('человек паук', 'оптимус прайм', 10)
A.trans_method()
print(A.auto_name)