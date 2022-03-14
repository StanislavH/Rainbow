class Warface:
    def wf_method(self):
        print('Оружие')


class Cold(Warface):
    Cold_count = 0
    Cold_name = 'Бабочка'
    Cold_model = 'Золотая'
    Cold_year = '2018'

    def __init__(self):
        Cold_count = 0
        Cold_name = 'Керамбит'
        print(Cold.Cold_count)

    def __method(self):
        print('Нож')

    def start_wf(self, Cold_name, Cold_model, Cold_year):
        print('Удар')
        self.Cold_name = Cold_name
        self.Cold_model = Cold_model
        self.Cold_year = Cold_year
        Cold_count = 1
        if Cold_name == 'Бабочка':
            print('Попадание')
        else:
            print('Промах')

    def finish_Cold(self):
        print('Трюки')
        print(Warface.Cold_name)


class Dopl(Warface):
    Dopl_count = 0
    Dopl_name = 'CZ-Auto'
    Dopl_model = 'Обычная'
    Dopl_year = '2015'

    def __init__(self):
        Dopl_count = 0
        Dopl_name = 'Degle'
        print(Dopl.Dopl_count)

    def __metod(self):
        print('Дополнительное')

    def start_Dopl(self, Dopl_name, Dopl_model, Dopl_year):
        print('Выстрел')
        self.Dopl_name = Dopl_name
        self.Dopl_model = Dopl_model
        self.Dopl_year = Dopl_year
        Dopl_count = 1
        if Dopl_name == 'CZ-Auto':
            print('Попадание')
        else:
            print('Ранение')

    def finish_Dopl(self):
        print('Осмотреть')
        print(Dopl.Dopl_name)


class Osn(Warface):
    def __init__(self, name, a1, a2):
        self.Osn_name = name
        self.__Osn_max_cap = a1
        self.__Osn_max_kol_clips = a2
        self.Osn_tek_cap = a1
        self.Osn_tek_kol_clips = a2

    def __metod(self):
        print('Основное')

    def shoot(self):
        if self.Osn_tek_cap > 0:
            self.Osn_tek_cap -= 2
            print("Выстрел сделан, осталось " + str(self.Osn_tek_cap))
        else:
            self.reload()

    def reload(self):
        if self.Osn_tek_kol_clips > 0:
            self.Osn_tek_kol_clips -= 1
            self.Osn_tek_cap = self.__Osn_max_cap
            print("Перезарядка прошла успешно")
        else:
            print("Патронов нет БЕГИИИИ")


#Osn = Osn("DP-12", 14, 20)
#print(Osn.Osn_name)
