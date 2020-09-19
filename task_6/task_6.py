import time


class TrafficLight:
    color = 'Black'

    def _on(self):
        color = 'Red'
        print(color)
        time.sleep(7)
        color = 'Yellow'
        print(color)
        time.sleep(2)
        color = 'Green'
        print(color)
        time.sleep(5)
        color = 'TrafficLight Off'
        print(color)


class Road:
    def __init__(self, w, l):
        self._width = w
        self._length = l
        self._weight = 25

    def wt_asphalt(self, depth=0.05):
        return self._width * self._length * self._weight * depth


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


class Car:

    def __init__(self):
        self.speed = 60
        self.color = 'white'
        self.name = 'car'
        self.is_police = False

    def go(self):
        print(f'\n{self.name}')
        print('start')

    def stop(self):
        self.speed = 0
        print('stop')

    def turn(self, direction):
        print(f'turn on the {direction}')

    def show_speed(self):
        print(f'current speed = {self.speed}')


class TownCar(Car):
    def __init__(self):
        self.name = 'Ford'
        self.speed = 80

    def show_speed(self):
        print(f'current speed = {self.speed}')
        if self.speed > 60:
            print(f'Warning current speed > 60 !!!')


class WorkCar(Car):
    def __init__(self):
        self.name = 'Man'
        self.speed = 50

    def show_speed(self):
        print(f'current speed = {self.speed}')
        if self.speed > 40:
            print(f'Warning current speed > 40 !!!')


class SportCar(Car):
    def __init__(self):
        self.name = 'Lamborghini'
        self.speed = 250


class PoliceCar(Car):
    def __init__(self):
        self.name = 'Police car'
        self.speed = 60
        self.is_police = True


class Stationery:

    def __init__(self):
        self.title = 'Stationery'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Pen.')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки Pencil.')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки Handle. ')


class MyTask:

    @staticmethod
    def task_1():
        tl = TrafficLight()
        tl._on()

    @staticmethod
    def task_2():
        road = Road(20, 5000)
        print(f'wt_asphalt = {road.wt_asphalt()} kg')

    @staticmethod
    def task_3():
        p1 = Position('Henry', 'Ford', 'Manager', 1000000, 10000000)
        print(f'full name = {p1.get_full_name()} ')
        print(f'total income  = {p1.get_total_income()} ')

    @staticmethod
    def task_4():
        cars = [TownCar(), WorkCar(), SportCar(), PoliceCar()]

        for i in cars:
            i.go()
            i.show_speed()
            i.turn('left')
        print('\n')
        for i in cars:
            print(i.name)
            i.stop()

    @staticmethod
    def task_5():
        pencil_box = [Pen(), Pencil(), Handle()]

        for i in pencil_box:
            i.draw()


if __name__ == '__main__':
    MyTask.task_5()
