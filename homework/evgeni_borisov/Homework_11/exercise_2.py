import random
from exercise_1 import Book


class Textbook(Book):
    def __init__(self, name_book, author, count_pages, subject, category, isbn=None, is_reserve=False,
                 is_building=True):
        super().__init__(name_book, author, count_pages, isbn, is_reserve)
        self.subject = subject
        self.category = category
        self.is_building = is_building

    def print_book(self):
        if self.is_reserve:
            print(f'Название: {self.name_book}, Автор: {self.author}, страниц: {self.count_pages}, '
                  f'предмет: {self.subject}, класс: {self.category}, зарезервирована')
        else:
            print(f'Название: {self.name_book}, Автор: {self.author}, страниц: {self.count_pages}, '
                  f'предмет: {self.subject}, класс: {self.category}')


book_1 = Textbook('Алгебра', 'Иванов', 200, 'Математика', '9А')
book_2 = Textbook('Геометрия', 'Петров', 301, 'Математика', '11В')
book_3 = Textbook('Обществознание', 'Акимов', 400, 'Политика', '10Б')

textbooks = [book_1, book_2, book_3]

# цикл с рандомом можно сделать методом родительского класса?
book_is_reserve = False
while not book_is_reserve:
    for book in textbooks:
        book.is_reserve = random.choice([True, False])
        if book.is_reserve:
            book_is_reserve = True
            break

for textbook in textbooks:
    textbook.print_book()
