my_dict = {"tuple": (1, True, "new", 6.67, [1, 5, 7, 9]), "list": ["new" "python", True, 90, {1: "one"}],
           "dict": {"one": 1, 2: "two", 3.0: "three", "four": False, "five": 5}, "set": {5.65, 6, 7, 80, 9, 6}}

#  Действия с кортежем
print("Значение последнего элемента кортежа: ", my_dict["tuple"][-1])

# Действия со списком
my_dict["list"].append("new")
delete_param = my_dict["list"].pop(1)
print("Значение удаленного параметра: ", delete_param)

#  Действия со словарем
my_dict["dict"]['i am a tuple'] = "new word"
delete_param_dict = my_dict["dict"].pop("four")
print("Значение удаленного параметра: ", delete_param_dict)

#  Действия со множеством
added_param_set = my_dict["set"].add(1000)
delete_param_set = my_dict["set"].pop()
print("Значение случайного удаленного элемента из множества:", delete_param_set)

print("Вывод словаря: ", my_dict)
