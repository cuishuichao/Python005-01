# -*- coding: utf-8 -*-

import pymysql

from week03.dbconfig import read_db_config

dbseriver = read_db_config()
db = pymysql.connect(**dbseriver)

try:
    with db.cursor() as cursor:
        sql = 'UPDATE book SET id=%s WHERE name = %s'
        values = (1003, '活着')
        cursor.execute(sql, values)
    db.commit()
except Exception as e:
    print(f'update error {e}')
finally:
    db.close()
    print(cursor.rowcount)
