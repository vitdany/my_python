def task_1():
    def div(arg1, arg2):
        if arg2 != 0:
            return arg1 / arg2
        else:
            return 0

    print('\ntask 1')
    a1 = float(input("arg1="))
    a2 = float(input("arg2="))
    d = div(a1, a2)
    print(f'result div = {d}')


def task_2():
    def print_user_data(surname, name, year, city, email, phone):
        print(f'Name: {name}; Family name: {surname};  Year of birth: {year}; City: {city};'
              f' Email: {email}; Phone: {phone}.')

    print('\ntask 2')
    print('args: Benoit, Alex, 1870, Saint-Petersburg, None, None')
    print_user_data(surname='Benoit', name='Alex', year=1870,
                    city='Saint-Petersburg', email=None, phone=None)


def task_3():
    def sum_max_pair(a, b, c):
        arg = [a, b, c]
        return sum(arg) - min(arg)

    print('\ntask 3')
    print('args = 10, 1, 0')
    print(f'sum max pair = {sum_max_pair(10, 1, 0)}')


def task_4():
    def my_sqrt(a, n):
        if n < 0:
            return a ** n

    def my_sqrt_use_for(a, n):
        if n < 0:
            m = 0
            for i in range(1, -n):
                m += a * a
            return 1 / m

    print('\ntask 4')
    print('args = 2, -2')
    print(f'sqrt = {my_sqrt(2, -2)}')
    print(f'sqrt use for = {my_sqrt_use_for(2, -2)}')


def task_5():
    def enter_user_array():
        nonstop = True
        s = 0
        while nonstop:
            str_user = input("Enter array :").split(" ")

            for el in str_user:
                try:
                    s += float(el)
                except ValueError:
                    nonstop = False

            print(f'array sum: {s}')

    print('\ntask 5')
    enter_user_array()


def task_6():
    def get_title_str(str_user):
        return str_user.title()

    def enter_str():
        str = input("Enter str :").split(" ")
        return " ".join([get_title_str(el) for el in str])

    print('\ntask 6')
    print(enter_str())



if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
