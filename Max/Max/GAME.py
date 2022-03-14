class Tank:
    def tank_method(self):
        print('это родительский метод')


class Gun(Tank):
    ##gun_reload_time = 25
    ##gun_accuracy = 2.5
    ##gun_max_capacity = 3
    ##gun_number_of_clips = 13
    ##gun_tek_capacity = 0
    ##gun_tek_number_of_clips = 0

    def __init__(self, a, b, c, d):
        self.cur_gun_reload_time = a
        self.cur_gun_accuracy = b
        self.gun_max_capacity = c  # количество снарядов в текущем
        self.gun_number_of_clips = d  # количество барабанов в текущем
        self.cur_gun_max_capacity = c
        self.cur_gun_number_of_clips = d

    def __method(self):
        pass

    def gun_shot(self):
        if self.cur_gun_max_capacity > 0:
            print('Выстрел')
            # self.cur_gun_max_capacity -= 1
            self.reload_gun()

    def reload_gun(self):
        # print('Снаряды в барабане закончились,перезарежаюсь')
        if self.cur_gun_max_capacity > 0:
            self.cur_gun_max_capacity -= 1
            print("Перезарядка прошла успешно")
        if (self.cur_gun_max_capacity == 0) & (self.cur_gun_number_of_clips > 0):
            self.cur_gun_number_of_clips -= 1
            self.cur_gun_max_capacity = self.gun_max_capacity
            print("Барабан поменяли")
        elif (self.cur_gun_max_capacity == 0) & (self.cur_gun_number_of_clips == 0):
            print('Тикац с городу')

    def point_gun(self):
        print('Наводимся')


class Chassis(Tank):
    chassis_turn = 30
    chassis_load = 48

    def __init__(self):
        pass

    def __method(self):
        pass

    def run_chassis(self):
        print('Едем вперед')

    def turn_chassis(self, degree, direction):
        print('Поварачиваю налево')


class Armor(Tank):
    armor_thickness = 225

    def __init__(self):
        pass

    def __method(self):
        pass

    def hold_armor(self):
        print('Броня не побрита')


A = Gun(1, 2, 3, 4)
for i in range(0, 100):
    A.gun_shot()
