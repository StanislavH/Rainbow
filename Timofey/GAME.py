import random


class Human:
    def hum_method(self):
        print()
        max_human_health = 100
        max_human_mana = 100
        tec_human_health = 100
        tec_human_mana = 100


class Magic(Human):
    def mag_method(self):
        print('это родительский метод')

    def __init__(self):
        pass


class Destruction(Magic):
    destruction_mana = 8
    destruction_damage = 40
    destruction_name = 'пламя'

    def __method(self):
        pass

    def destroy_destruction(self, mana, damage):
        def __hit_desruction():
            a = random.randint(0, 100)
            if a > 50:
                return 1
            else:
                return 0

        if __hit_desruction():
            print('сработало, потрачено' + mana + 'маны')
            print('нанесено' + damage + 'урона')

    def mag_method(self):
        pass


class Healing(Magic):
    Healing_mana = 8
    Healing_heal = 10
    Healing_name = 'лечение'

    def __init__(self, name, heal, mana):
        self.Healing_name = name
        self.Healing_heal = heal
        self.Healing_mana = mana

    def __method(self):
        pass

    def protection_healing(self, mana, heal):
        if self.tec_human_mana >= mana:
            if self.tec_human_health == self.max_human_health:
                print('у вас и так максимальное здоровье')
            elif self.tec_human_health + heal > self.max_human_health:
                self.tec_human_health = self.max_human_health
                self.tec_human_mana -= mana
                print('здоровье восстановлено, у вас 100 хп,потрачено'+ mana +'маны')
            else:
                self.tec_human_health += heal
                self.tec_human_mana -= mana
                print('здоровье восстановлено на' + heal + 'потрачено' + mana + 'маны')


    def mag_method(self):
        pass


class Illision(Magic):
    A = 'Драугр,Дракон'
    Illusion_mana = 70
    Illusion_name = 'страх'

    def __method(self):
        pass

    def change_illusion(self, mana):
        if self.tec_human_mana < mana:
            print('недостаточно маны')
        elif self.tec_human_mana == self.max_human_mana:
            print('цель убежала от вас в страхе')

    def mag_method(self):
        pass


A = Healing("лечение", 30, 8)
print(A.Healing_name)
print(A.Healing_heal)
print(A.Healing_mana)
