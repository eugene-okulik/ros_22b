def calc_func(func):
    def wrapper(first, second):
        if first == second:
            operation = "+"
        elif first < 0 or second < 0:
            operation = "*"
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        else:
            operation = None

        return func(first, second, operation)
    return wrapper


@calc_func
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

print(calc(first_num, second_num))

'''просьба пояснить про аргумент "operation". Должен ли я его передавать в функции "wrapper"? Если я его передаю
без заданного значения, то ловлю ошибку, что аргумент не задан
(TypeError: calc_func.<locals>.wrapper() missing 1 required positional argument: 'operation'), 
а если не передаватать и закомментировать строки 11-12, 
то тогда синтаксис  ругается на 19 строку "Local variable 'operation' might be referenced before assignment)
'''
