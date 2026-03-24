
#   Задача #1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']

name, last_name, city, phone, country = person

print(name, last_name, city, phone, country, sep='\n')


#   Задача #2
'''
Меня смутила постановка задачи , а именно 'числа могут быть другие'. Не знаю, какой результат ожидается(мб просто
три строки надо было перечислить с этими числами, поэтому предосталю вроде бы рабочий код, где в первом варианте
необходимо самому ввести рандомное число, ведь текст одинаковый в первых двух вариантах)
'''

text_1 = 'результат операции: ' + str(input("Введите любое число: "))
text_2 = "результат работы программы: 9"

num_1 = text_1.index(':')
num_2 = text_2.index(':')
print(int(text_1[num_1 + 1:].strip()) + 10)
print(int(text_2[num_2 + 1:].strip()) + 10)


#   Задача #3
students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

print('Students ' + ', '.join(students) + ' study these subjects: ' + ', '.join(subjects))
