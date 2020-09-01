def task_1():
    print('\ntask 1')
    text = ["Основоположником алгебры логики является английский математик и логик Дж. Буль (", 1815, "–", 1864, ")"]
    print(text)
    count = [0, 0]
    for i in range(len(text)):
        # print(type(text[i]))
        if type(text[i]) == str:
            count[0] += 1
        if type(text[i]) == int:
            count[1] += 1
        i += 1
    print(f'Count str ={count[0]} int = {count[1]}')


def task_2():
    print('\ntask 2')
    sen = input("Print few tokens:")
    text = sen.split(" ")
    print(text)
    i = 1
    while i < len(text):
        tmp = text[i - 1]
        text[i - 1] = text[i]
        text[i] = tmp
        i += 2
    print(text)


def task_3():
    print('\ntask 3')
    season = ["winter", "spring", "summer", "autumn"]
    n = int(input("Enter num month:"))
    index = n // 3
    if index > 3:
        index = 0
    print(f'season = {season[index]}')
    print("Find value by key:")
    season_d = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring",
                6: "summer", 7: "summer", 8: "summer",
                9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
    print(f'season = {season_d[n]}')


def task_4():
    print('\ntask 4')
    sen = input("Print sentence, please:")
    text = sen.split(" ")
    i = 0
    while i < len(text):
        print(f'{i + 1} {text[i][:10]}')
        i += 1


def task_5():
    print('\ntask 5')
    my_list = [7, 7, 5, 5, 3, 3, 2, -1]
    print(my_list)
    n = int(input('Enter next num:'))
    i = 0

    while i < len(my_list):
        if my_list[i] < n:
            break
        i += 1

    my_list.insert(i, n)
    print(my_list)


def task_6():
    print('\ntask 6')
    season = [
        (1, {"season": "winter", "rainfall ": 40, "number of Sunny days": 10}),
        (2, {"season": "spring", "rainfall ": 30, "number of Sunny days": 30}),
        (3, {"season": "summer", "rainfall ": 10, "number of Sunny days": 70}),
        (4, {"season": "autumn", "rainfall ": 30, "number of Sunny days": 30})
    ]

    print(f'season = {season}')
    keys = list(season[0][1].keys())
    val = []
    for el in season:
        val.append(list(el[1].values()))
    t_list = zip(*val)
    t_list = list(t_list)
    stat = {}
    i = 0
    for el in keys:
        stat.update({el: list(t_list[i])})
        i += 1
    print(f'result = {stat}')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
