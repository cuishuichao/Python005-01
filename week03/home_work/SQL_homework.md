#### 安装 mysql 设置字符集
- 在 Linux 环境下，安装 MySQL5.6 以上版本，修改字符集为 UTF8mb4 并验证
- 新建一个数据库 testdb，并为该数据库增加远程访问的用。
- 将修改字符集的配置项、验证字符集的 SQL 语句作为作业内容提交
- 将增加远程用户的 SQL 语句作为作业内容提交

````
# 注意 MySQL 中的 utf8 不是 UTF-8 字符集

# 在配置文件增加配置
vim /etc/my.cnf
[client]
default_character_set = utf8mb4

[mysql]
default_character_set = utf8mb4

interactive_timeout= 28800         #针对交互式连接设置超时时间
wait_timeout= 28800                #针对非交互式连接超时时间
max_connections= 1000              #MySQL 最大连接数
character_set_server= utf8mb4      #MySQL 字符集基础设置
init_connect= 'SET NAMES utf8mb4'  #服务器为每个连接的客户端执行的字符集

#重启生效设置
systemctl restart mysqld

# 查看字符集
show variables like '%character%';

# 查看校对规则
show variables like 'collation_%';

#创建数据库
create database testdb

#增加用户远程访问数据库
# mysql> create database testdb;
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY 'testpass';


````

#### 为以下 sql 语句标注执行顺序：
```
SELECT DISTINCT player_id, player_name, count(*) as num   #5
FROM player JOIN team ON player.team_id = team.team_id    #1
WHERE height > 1.80                                       #2  
GROUP BY player.team_id                                   #3  
HAVING num > 2                                            #4  
ORDER BY num DESC                                         #6  
LIMIT 2                                                   #7  
```

### 以下两张基于 id 列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?
```
Table1
id name
1 table1_table2
2 table1

Table2
id name
1 table1_table2
3 table2

INNER JOIN

SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
INNER JOIN Table2
ON Table1.id = Table2.id;

Table1 和 Table2 id字段相匹配的数据

LEFT JOIN

SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
LEFT JOIN Table2
ON Table1.id = Table2.id;

Table1 所有数据， Table2 id字段和Table1，id字段相匹配的数据

 
RIGHT JOIN

SELECT Table1.id, Table1.name, Table2.id, Table2.name
FROM Table1
RIGHT JOIN Table2
ON Table1.id = Table2.id;

Table2 所有数据， Table1 id字段和Table1，id字段相匹配的数据

```

#### 使用 MySQL 官方文档，学习通过 sql 语句为上题中的 id 和 name 增加索引，并验证。根据执行时间，增加索引以后是否查询速度会增加？请论述原因，并思考什么样的场景下增加索引才有效。

```
ALTER TABLE Table1 ADD PRIMARY KEY (id)

ALTER TABLE table2 ADD INDEX index_name (name)
```


