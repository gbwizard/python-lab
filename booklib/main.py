import sys
from datetime import date
import sqlite3


class Author:
    id = 0
    first_name = ''
    middle_name = ''
    last_name = ''

    def __init__(self, fname, lname, mname):
        self.first_name = fname
        self.last_name = lname
        self.middle_name = mname


class Book:
    book_id = 0
    author_id = 0
    name = ''
    desc = ''
    year = 0
    date = date.min
    series_id = 0
    publisher_id = 0

    def __init__(self, name, desc, year, date=date.min):
        self.name = name
        self.desc = desc
        self.year = year
        self.date = date


class DB:
    def __init__(self, filename):
        self.__filename = filename
        self.__con = sqlite3.connect(self.__filename)
        self.__cur = self.__con.cursor()

    def query_books(self) -> list:
        res = self.__cur.execute("SELECT * FROM tblBooks ORDER BY Year")
        return res.fetchall()

    def query_authors(self) -> list:
        res = self.__cur.execute("SELECT * FROM tblAuthors ORDER BY LastName")
        return res.fetchall()

    def query_publishers(self) -> list:
        res = self.__cur.execute("SELECT * FROM tblPublishers ORDER BY Name")
        return res.fetchall()

    def query_series(self) -> list:
        res = self.__cur.execute("SELECT * FROM tblSeries ORDER BY Name")
        return res.fetchall()

    def add_author(self, author: Author) -> int:
        pass

    def add_publisher(self, name: str) -> int:
        pass

    def add_series(self, name: str) -> int:
        pass

    def add_book(self, book: Book) -> int:
        pass


def print_help():
    pass


def input_str(invite: str) -> str:
    print(invite, end='')
    return input()


def input_int(invite: str) -> int:
    print(invite, end='')
    return int(input())


def main():
    # 'D:\books.lib\db\mytestlib.db'
    # db = DB(sys.argv[1])
    db = DB('D:\\books.lib\\db\\mytestlib.db')
    while True:
        print('> ', end='')
        cmd = input()
        if cmd == '':
            continue
        elif cmd == 'help' or cmd == 'h':
            print_help()
        elif cmd == 'exit' or cmd == 'quit':
            break
        elif cmd == 'q' or cmd == 'query':
            while True:
                print('query > ', end='')
                cmd = input()
                if cmd == 'exit' or cmd == 'quit':
                    break
                elif cmd == 'help' or cmd == 'h':
                    print_help()
                elif cmd == 'books' or cmd == 'b':
                    for book in db.query_books():
                        print(book)
                elif cmd == 'authors' or cmd == 'a':
                    for author in db.query_authors():
                        print(author)
                elif cmd == 'publishers' or cmd == 'p':
                    for publisher in db.query_publishers():
                        print(publisher)
                elif cmd == 'series' or cmd == 's':
                    for series in db.query_series():
                        print(series)
        elif cmd == 'a' or cmd == 'add':
            name = input_str('Enter book name: ')
            author_fname = input_str('Enter author first name: ')
            author_lname = input_str('Enter author last name: ')
            author_mname = input_str('Enter author middle name: ')
            year = input_int('Enter book year: ')
            series = input_str('Enter book series name: ')
            publisher = input_str('Enter publisher name: ')
            author = Author(author_fname, author_lname, author_mname)
            book = Book(name, '', year)
            book.author_id = db.add_author(author)
            book.series_id = db.add_series(series)
            book.publisher_id = db.add_publisher(publisher)
            book_id = db.add_book(book)
            print(f'Book was successfully added to the DB with id: {book_id}')


if __name__ == "__main__":
    # execute only if run as a script
    main()
