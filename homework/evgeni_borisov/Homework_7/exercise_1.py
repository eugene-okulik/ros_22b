number = 8
while True:
    num = int(input("Попробуйте угадать цифру! Введите цифру "))
    if num == number:
        print('Поздравляю! Вы угадали!')
        break
    print("Попробуйте снова")
