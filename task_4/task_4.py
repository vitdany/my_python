import sys


def task_1():
    print('\ntask 1')
    try:
        if len(sys.argv) != 4:
            print("There must be four arguments")
            # raise Exception("There must be four arguments")
            return
        pay = int(sys.argv[1]) * int(sys.argv[2]) + int(sys.argv[3])  # (выработка в часах * ставка в час) + премия.
        print(f'pay = {pay}')
    except ValueError as ve:
        print("ValueError! {0}".format(ve))
        return


def task_2():
    print('\ntask 2')
    try:
        from random import randint
        a = [randint(0, 100) for i in range(10)]
        print(a)
        b = [i for x, i in enumerate(a) if x > 0 if i > a[x - 1]]
        print(b)
    except ValueError as ve:
        print("ValueError! {0}".format(ve))
        return


def task_3():
    print('\ntask 3')
    try:
        print('Range: 20-240, % 20')
        a = [i for i in range(20, 241) if i % 20 == 0]
        print(a)
    except ValueError as ve:
        print("ValueError! {0}".format(ve))
        return


def task_4():
    print('\ntask 4')
    try:
        from random import randint
        a = [randint(0, 10) for i in range(20)]
        # a = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
        b = [i for x, i in enumerate(a) if i not in a[x + 1:] and i not in a[:x]]

        print(a)
        print(b)
    except ValueError as ve:
        print("ValueError! {0}".format(ve))
        return


def task_5():
    print('\ntask 5')
    from functools import reduce

    def mult(prev_el, el):
        return prev_el * el

    try:
        a = [i for i in range(1, 11, 2)]
        print(a)
        b = reduce(mult, a)
        print(b)
    except ValueError as ve:
        print("ValueError! {0}".format(ve))
        return


def task_6():
    print('\ntask 6')
    try:
        from itertools import cycle, count

        for el in count(7):
            if el > 9:
                break
            else:
                print(f'el >= 7 {el}' )

        progr_lang = "Fortran (Formula Translator) был самым первым высокоуровневым языком программирования.".split()
        print(f'source ={progr_lang}')
        iter = cycle(progr_lang)
        print(iter)
        stop = False
        i = 0
        print('\nresult: ')
        while i != len(progr_lang):
            print(next(iter))
            i += 1
        # stop = input("for stop print true :") == "true"

    except ValueError as ve:
        print("ValueError! {0}".format(ve))
        return


def task_7():
    print('\ntask 7')

    def fact(n):
        r = 1
        for j in n:
            r *= j
            yield r

    try:
        n = [1, 2, 3, 4, 5]
        for j in fact(n):
            print(j)
    except ValueError as ve:
        print("ValueError! {0}".format(ve))
        return


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
