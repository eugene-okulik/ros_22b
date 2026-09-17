import random
salary = int(input("Укажите свою заработную плату: "))

bonus = random.randint(0, 1000000)
bonus_value = random.choice([True, False])


def random_bonus():
    if bonus_value is True:
        print(f"{salary}, {bonus_value} - '${salary + bonus}', 'Ваш бонус - {bonus}$'")
    else:
        print(f"{salary}, {bonus_value} - '${salary}'")


random_bonus()
