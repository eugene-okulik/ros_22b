PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

list_price = PRICE_LIST.split()

list_key = list_price[0::2]
list_value = [int(value[:-1]) for value in list_price[1::2]]

price_dict = dict(zip(list_key, list_value))

print(price_dict)
