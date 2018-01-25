#!/usr/bin/env python3
# coding: utf-8


from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象系统
Base = declaretive_base()

# 定义Word对象
# TODO: 使用sqlite数据库
class Word(Base):
    # 表的名字
    __tablename__ = 'word'

    # 表的结构
    id = Column(String(20), primary_key=True)
    word = Column(String(20))
    content = Column(String(100))
    count = Column(Integer)


# 初始化数据库链接
engine = create_engine('sqlite:///test.db')

# 创建DBsession类型
DBsession = sessionmaker(bind=engine)

