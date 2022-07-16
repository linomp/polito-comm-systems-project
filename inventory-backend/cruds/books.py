from pymysql import NULL
from dependencies import db
from schemas.book import *


def add_book(new_book: Book):
    values = (None,
              new_book.book_id,
              new_book.author,
              new_book.year,
              new_book.publisher,
              new_book.language)
    query = "INSERT INTO book_extension_table (id, book_id, author, year, publisher, language) VALUES (%s, %s, %s, %s, %s, %s)"
    db.execute(query, values)

    return


def update_book_info(item_id: int, new_data: BookDAO):
    values = (new_data.author,
              new_data.year,
              new_data.publisher,
              new_data.language,
              item_id)
    query = "UPDATE book_extension_table SET author=%s, year=%s, publisher=%s, language=%s WHERE item_id=%s"
    db.execute(query, values)
    return
