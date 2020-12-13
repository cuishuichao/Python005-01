# -*- coding: utf-8 -*-

"""
使用 sqlalchemy ORM 方式创建如下表，使用 PyMySQL 对该表写入 3 条测试数据，并读取:
用户 id、用户名、年龄、生日、性别、学历、字段创建时间、字段更新时间
将 ORM、插入、查询语句作为作业内容提交
"""
import datetime

from sqlalchemy import Column, Integer, String, DateTime, create_engine, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True)
    username = Column(String(20))
    age = Column(Integer)
    birthday = Column(String(50))
    sex = Column(String(2))
    degree = Column(String(20))
    created_on = Column(DateTime, default=datetime.datetime.now)
    update_on = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return "UserTable(_id='{id}',username={username})".format(id=self.id, username=self.username)


dburl = "mysql+pymysql://root:123456@localhost:3306/timegeek?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

SessionClass = sessionmaker(bind=engine)
session = SessionClass()

usera = UserTable(username='小王', age=25, birthday='1990051', sex='M', degree='本科')
userb = UserTable(username='小刘', age=35, birthday='19951010', sex='M', degree='专科')
userc = UserTable(username='小崔', age=20, birthday='1993041', sex='F', degree='硕士')

session.add(usera)
session.add(userb)
session.add(userc)
session.commit()

"""
张三给李四通过网银转账 100 极客币，现有数据库中三张表：
一张为用户表，包含用户 ID 和用户名字，另一张为用户资产表，包含用户 ID 用户总资产，
第三张表为审计用表，记录了转账时间，转账 id，被转账 id，转账金额。
请合理设计三张表的字段类型和表结构；
请实现转账 100 极客币的 SQL(可以使用 pymysql 或 sqlalchemy-orm 实现)，张三余额不足，转账过程中数据库 crash 等情况需保证数据一致性。
"""


class User(Base):
    __tablename__ = 'user'
    uid = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(15), nullable=True, unique=True)


class Asset(Base):
    __tablename__ = 'asset'
    uid = Column(Integer(), primary_key=True, nullable=True)
    asset = Column(DECIMAL(19, 4), nullable=True)


class Record(Base):
    __tablename__ = 'record'
    one_id = Column(Integer(), primary_key=True)
    other_id = Column(Integer(), primary_key=True)
    deal = Column(DECIMAL(19, 4), nullable=True)
    create_date = Column(DateTime(), nullable=True)
