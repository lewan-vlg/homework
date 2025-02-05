from threading import Thread
import time


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.start_power=100

    def start_battle(self):
        print(f'\33[31m{self.name}, на нас напали!')

    def end_battle(self):
        print(f'\33[34m{self.name} одержал победу спустя {self.days} дней(дня)!')

    def battle(self):
        print(f'\33[33m{self.name} сражается {self.days} день(дня)..., осталось {self.start_power} войнов.')

    def run(self):
        self.start_battle()
        while self.start_power > 0:
            self.start_power -= self.power
            self.days += 1
            self.battle()
            time.sleep(1)
        self.end_battle()



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'\33[32mВсе битвы закончились!')
