def dialog_about_jogging():
    a = float(input("\nenter the number of kilometers for the first day:"))
    b = float(input("enter the target:"))
    k = 0.1
    i = 1
    while b > a:
        a = a + a * k
        i = i + 1
    print(f"the number of days to achieve the target result : {i}")


def dialog_about_company():
    revenue = float(input("\nenter revenue:"))
    cost = float(input("enter cost:"))
    profit = revenue - cost
    if profit > 0:
        print('the company made a profit: %.2f' % profit)
        if revenue > 0:
            profitability = profit / revenue
        else:
            profitability = 0
        print('the company has achieved profitability: %.2f' % profitability)
        num_employ = int(input("enter number of employees:"))
        if num_employ > 0:
            profit_employ = profit/num_employ
        else:
            profit_employ = 0
        print("the company's profit per employee: %.2f" % profit_employ)
    else:
        print('the company suffered losses: %.2f' % profit)


def print_max_number(vec_a):
    s = str(vec_a)
    max_a = 0
    i = 0
    while i < len(s):
        a = int(s[i])
        if a >= max_a:
            max_a = a
        i = i + 1
    print('max num is %d' % max_a)


def print_time(sec):
    h = sec // 3600
    m = (sec - h * 3600) // 60
    #s = sec - h * 3600 - m * 60
    #hh = str(h).zfill(2)
    #mm = str(m).zfill(2)
    #ss = str(s).zfill(2)
    #print('format time: {:s}:{:s}:{:s}'.format(hh, mm, ss))
    s = sec % 60
    print(f"{h:02}:{m:02}:{s:02}")

    # print('format time: %s:%s:%s' % (hh, mm, ss))
    # oct1, oct2, oct3 = [hh, mm, ss]
    # print(f'''format time: {oct1:<1}:{oct2:<1}:{oct3:<1} ''')


def print_sum(n):
    s1 = int(n)
    s2 = int(n + n)
    s3 = int(n + n + n)
    print('sum: {:d}'.format(s1 + s2 + s3))


def print_hi(name):
    print(f'Hi, {name}', ', nice to meet you.')


if __name__ == '__main__':

    who = input("\nwhat is your name? ")
    print_hi(who)

    time = int(input("\nwhat time is it? "))
    print_time(time)

    n = input("\nenter N:")
    print_sum(n)

    num = input("\nenter string numbers:")
    print_max_number(num)

    dialog_about_company()

    dialog_about_jogging()
