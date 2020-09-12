def task_1():
    print('\ntask 1')
    try:
        f_obj = open("text.txt", "w")
        stop = False
        n = 0
        while not stop:
            str_user = input()
            if len(str_user) == 0:
                stop = True
            else:
                f_obj.write(str_user + "\n")
                str_user = ""
                n += 1
        print(f'Recorded {n} strings')
    except IOError:
        print("Произошла ошибка ввода-вывода!")
    finally:
        f_obj.close()


def task_2():
    print('\ntask 2')
    try:
        n = 0
        k = 0
        with open("text.txt") as f_obj:
            for line in f_obj:
                n += 1
                k += len(line.split())

        print(f'Read {n} strings')
        print(f'Read {k} words')
    except IOError:
        print("Произошла ошибка ввода-вывода!")
    finally:
        f_obj.close()


def task_3():
    print('\ntask 3')
    try:
        f = open("employer.txt", 'r', encoding='utf-8')
        d = f.read().split()
        d_salary = [int(x) for i, x in enumerate(d) if i % 2 != 0]
        ave = sum(d_salary) / len(d_salary)
        d_name = [y for i, y in enumerate(d) if i % 2 == 0]
        print(d_name)
        print(d_salary)
        print("\nsalary < 20000")
        [print(d_name[i]) for i, x in enumerate(d_salary) if x < 20000]
        print(f"\nave salary {ave}")
    except IOError:
        print("Произошла ошибка ввода-вывода!")
    finally:
        f.close()


def task_4():
    print('\ntask 4')
    try:
        d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
        f = open("number_ru.txt", 'w', encoding='utf-8')
        with open("number.txt", encoding='utf-8') as f_obj:
            for line in f_obj:
                s = line.split()
                s[0] = d[s[0]]
                line_ru = " ".join(s)
                line_ru += "\n"
                f.write(line_ru)

        import os
        if os.path.exists(r"./number_ru.txt"):
            print("Recorded file number_ru.txt")
        else:
            print('Error write file ./number_ru.txt')

    except IOError:
        print("Произошла ошибка ввода-вывода!")
    finally:
        f.close()


def task_5():
    print('\ntask 5')
    try:
        a = [i for i in range(100)]
        with open("vector.txt", 'w') as fnum:
            print(f'{a}', file=fnum)

        f = open("vector.txt", 'r')
        b = f.read().replace('[', '').replace(']','').replace(',','').split()

        print(b)
        import os
        if os.path.exists(r"./vector.txt"):
            print("Recorded file vector.txt")
        else:
            print('Error write ./vector.txt')

    except IOError:
        print("Произошла ошибка ввода-вывода!")
    finally:
        f.close()


def task_6():
    print('\ntask 6')
    try:
        import re
        w = {}
        with open("schedule.txt", 'r', encoding='utf-8') as ftxt:
             for line in ftxt:
                s = line.split(':')
                if len(s) == 2:
                        match = re.findall(r'\d+', s[1])
                        sum_el = sum(map(int, match))
                        if sum_el != 0:
                            w.update({s[0]: sum_el})
        for key, value in w.items():
            print("{0}: {1}".format(key, value))
    except IOError:
        print("Произошла ошибка ввода-вывода!")


def task_7():
    print('\ntask 7')
    try:
        import re, json
        w = {}
        p = {}
        ave_profit = 0
        sum_profit = 0
        n_firms_profit = 0
        with open("firms.txt", 'r', encoding='utf-8') as ftxt:
            for line in ftxt:
                s = line.split()[0]
                m = re.findall(r'\d+', line)
                #print(m)
                profit = int(m[1]) - int(m[2])

                if profit > 0:
                    n_firms_profit += 1
                    sum_profit += profit
                w.update({s: profit})
            if n_firms_profit > 0:
                p.update({'average_profit': sum_profit/n_firms_profit})

        for key, value in w.items():
            print("{0}: {1}".format(key, value))
        for key, value in p.items():
            print("{0}: {1}".format(key, value))
        data = [w, p]
        with open("firms.json", "w") as write_f:
            json.dump(data, write_f)



    except IOError:
        print("Произошла ошибка ввода-вывода!")


if __name__ == '__main__':

    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
