# -*- coding: utf-8 -*-

import pymysql

from week03.dbconfig import read_db_config

dbseriver = read_db_config()
db = pymysql.connect(**dbseriver)

try:
    with db.cursor() as cursor:
        sql = 'SELECT name FROM book'
        cursor.execute(sql)
        books = cursor.fetchall()  # fetchone 返回单条
        for book in books:
            print(book)
    db.commit()
except Exception as e:
    print(f'select error {e}')
finally:
    db.close()
    print(cursor.rowcount)
