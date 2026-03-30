text_1 = 'результат операции: 42'
text_2 = 'результат операции: 54'
text_3 = 'результат работы программы: 209'
text_4 = 'результат: 2'


def sum_calc(text):
    num = text.index(':')
    return int(text[num + 1:].strip()) + 10


print(sum_calc(text_1))
print(sum_calc(text_2))
print(sum_calc(text_3))
print(sum_calc(text_4))
