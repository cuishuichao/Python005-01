# -*- coding: utf-8 -*-
import pymysql

from week03.dbconfig import read_db_config

dbservier = read_db_config()
db = pymysql.connect(**dbservier)

try:
    with db.cursor() as cursor:
        # %s 是占位符固定的
        sql = 'INSERT INTO book (id, name) VALUES (%s, %s)'
        value = ((1002, "活着")
                 (1005, "飘"))
        cursor.executemany(sql, value)  # execute 插入单条
    db.commit()
except Exception as e:
    print(f'insert error {e}')
finally:
    db.close()
    print(cursor.rowcount)
