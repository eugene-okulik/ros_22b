import sys


sys.set_int_max_str_digits(0)


def nums_fibonacci():
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


def result_fibonacci(num):
    count = 1
    for number in nums_fibonacci():
        if count == num:
            print(number)
            break
        count += 1


result_fibonacci(5)
result_fibonacci(200)
result_fibonacci(1000)
result_fibonacci(100000)
