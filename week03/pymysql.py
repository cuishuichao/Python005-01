# -*- coding: utf-8 -*-
import pymysql

from week03.dbconfig import read_db_config

dbserver = read_db_config()
# 加载 mysql 配置文件
db = pymysql.connect(**dbserver)

try:
    # 使用 cursor() 方法创建游标对象
    with db.cursor() as cursor:
        sql = 'SELECT VERSION()'
        # execute() 执行 sql
        cursor.execute(sql)
        # 返回所有作用行
        result = cursor.fetchall()
    db.commit()
except Exception as e:
    print(f'fetch error {e}')
finally:
    # 关闭连接
    db.close()

print(f'Database version : {result}')
