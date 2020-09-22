import datetime


class MyData:

    def __init__(self, strData):
        self.strData = strData

    @classmethod
    def strToListNum(cls, _str):
        my_list = list(map(int, _str.split('-')))
        return my_list

    @staticmethod
    def checkListNum(inList):
        try:
            dt = datetime.datetime(inList[2], inList[1], inList[0])
            print(f'Valid date: {inList[2]} {inList[1]} {inList[0]}')
            print(dt.strftime("%A, %d. %B %Y %I:%M%p"))
        except ValueError as ve:
            print(f'Date : {inList[2]} {inList[1]} {inList[0]}')
            print("ValueError: {0}".format(ve))


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class UserData:

    def userInputInfinitas(self):

        buffer = []
        print("Введите элементы списка, для остановки введите 'no' : ")
        while True:
            try:
                inp_data = input()
                if inp_data == 'no':
                    print(f'list = {buffer}')
                    return
                buffer.append(int(inp_data))

            except ValueError:
                print("Вы ввели не число")

    def userInput(self):
        inp_data = input("Введите делитель числа 10: ")

        try:
            inp_data = int(inp_data)
            if (inp_data == 0):
                raise OwnError("Вы ввели делитель ноль!")

            y = 10 / inp_data
        except ValueError:
            print("Вы ввели не число")
        except OwnError as err:
            print(err)
        else:
            print(f"Все хорошо. Результат: {y}")


from abc import ABC, abstractmethod


class Equipment(ABC):

    def __init__(self, name, cost, date):
        self._name = name
        self._cost = cost
        self._date = date

    def about(self):
        return f'{self._name} {self._cost}'

    def __and__(self, other):
        return self._name == other._name

    @abstractmethod
    def amortization(self, p):
        pass


class Printer(Equipment):

    def amortization(self, date):
        self._cost = self._cost - self._cost * 0.01 * (date - self._date)


class Xerox(Equipment):

    def amortization(self, date):
        self._cost = self._cost - self._cost*0.05 * ( date - self._date)


class Scanner(Equipment):

    def amortization(self, date):
        self._cost = self._cost - self._cost*0.10 * (date - self._date)


class WareHouse:

    def __init__(self):
        self._department = ["Shop", "Accounting", "Administration", "Advertising", "Finance", "Warehouse"]
        self._equipments = []

    def add(self, equipment):
        elem = {"equipment": equipment, "department": self._department[5]}
        self._equipments.append(elem)

    def give(self, equipment, department):
        for i, x in enumerate(self._equipments):
            if x["department"] != department and x["equipment"] == equipment:
                self._equipments[i]["department"] = department

    def report(self):
        print('\n')
        for x in self._equipments:
            print(f' {x["equipment"].about()} {x["department"]}')

    @property
    def department(self):
        return self._department


class Complex:

    def __init__(self, real, imag):
        self.re = real
        self.im = imag

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):

        return Complex(self.re*other.re - self.im*other.im, other.re * self.im + other.im * self.re )

    def print(self):
        print(f'{ self.re} + {self.im}i')

class MyTask:

    @property
    def task_1(self):
        print(f'Task 1')
        m = MyData('01-22-2020')
        lst = MyData.strToListNum(m.strData)
        MyData.checkListNum(lst)

        m = MyData('22-01-2020')
        lst = MyData.strToListNum(m.strData)
        MyData.checkListNum(lst)

    @property
    def task_2(self):
        print(f'Task 2')
        ud = UserData()
        ud.userInput()

    @property
    def task_3(self):
        print(f'Task 3')
        ud = UserData()
        ud.userInputInfinitas()

    @property
    def task_4(self):
        print(f'Task 4')
        wh = WareHouse()
        a = [Printer("Printer", 20000, 2010),
             Scanner("Scanner", 10000, 2010),
             Xerox("Xerox", 40000, 2019),
             Xerox("Xerox_2", 40000, 2020)
             ]
        wh.add(a[0])
        wh.add(a[1])
        wh.add(a[2])
        wh.add(a[3])

        wh.report()
        wh.give(a[0], wh.department[1])
        wh.give(a[1], wh.department[0])
        wh.give(a[2], wh.department[2])
        wh.report()

        print('after amortization:')
        [i.amortization(2020) for i in a]
        wh.report()

    @property
    def task_5(self):
        print(f'Task 5')
        x1 = Complex(1, 2)
        x2 = Complex(2, 3)
        [i.print() for i in [x1, x2, x1 + x2, x1 * x2]]




if __name__ == '__main__':
    mt = MyTask()
    mt.task_1
    mt.task_2
    mt.task_3
    mt.task_4
    mt.task_5
