words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def words_func():
    for word in words.items():
        key, value = word
        print(key * value)


words_func()
