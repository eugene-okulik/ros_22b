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
