#   Пока только такое решение пришло в голову. Но оно приведено под эту конкретную строку, и это плохая практика.
#   Просьба подсказать, как можно заменить запятую и точку. ( в рамках полученных знаний или чуть больше)


text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, " \
       "dignissim vitae libero"

words = text.split()
words_list = []

for word in words:
    if ',' in word:
        words_list.append(word[:-1] + 'ing' + ',')
    elif '.' in word:
        words_list.append(word[:-1] + 'ing' + '.')
    else:
        words_list.append(word + 'ing')

new_text = ' '.join(words_list)
print(new_text)
