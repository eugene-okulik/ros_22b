import random


class Book:
    material = 'бумага'
    is_text = True

    def __init__(self, name_book, author, count_pages, isbn, is_reserve=False):
        self.name_book = name_book
        self.author = author
        self.count_pages = count_pages
        self.isbn = isbn
        self.is_reserve = is_reserve

    def print_book(self):
        if self.is_reserve:
            print(f' Название: {self.name_book}, Автор: {self.author}, страниц: {self.count_pages}, '
                  f'материал: {self.material}, зарезервирована')
        else:
            print(f' Название: {self.name_book}, Автор: {self.author}, страниц: {self.count_pages}, '
                  f'материал: {self.material}')


if __name__ == "__main__":
    book_1 = Book('Герой нашего времени', 'Лермонтов', 229, '1234567890111')
    book_2 = Book('Вишнёвый сад', 'Лермонтов', 48, '0987654321000')
    book_3 = Book('Капитанская дочка', 'Пушкин', 121, '0000011111222')
    book_4 = Book('Дубровский', 'Пушкин', 232, '1111122222333')
    book_5 = Book('Война и Мир', 'Толстой', 1231, '2222222222111')
    books = [book_1, book_2, book_3, book_4, book_5]

    book_is_reserve = False
    while not book_is_reserve:
        for book in books:
            book.is_reserve = random.choice([True, False])
            if book.is_reserve:
                book_is_reserve = True
                break

    for book in books:
        book.print_book()
