# map | filter

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22,
                22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


def hot_temperatures(x):
    return x > 28


hot_temperatures_list = list(filter(hot_temperatures, temperatures))

print(max(hot_temperatures_list))
print(min(hot_temperatures_list))
print(round(sum(hot_temperatures_list) / len(hot_temperatures_list), 2))
