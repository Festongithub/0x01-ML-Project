#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import mapper

from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = sqlalchemy.orm.declarative_base()

class Post(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    slug  = Column(String(100), nullable=False)
    content = Column(String(50), nullable=False)
    published = Column(String(100), nullable=False, unique=True)
    created_on = Column(String(100), default=datetime.now)
    updated_on = Column(String(100), default=datetime.now, onupdate=datetime)


metadata = MetaData()

post = Table('post', metadata,
             Column('id', Integer, primary_key=True),
             Column('title', String(100), nullable=False),
             Column('slug', String(100), nullable=False),
             Column('content', String(50), nullable=False),
             Column('published', String(100), nullable=False, unique=True),
             Column('created_on', String(100), default=datetime.now),
             Column('updated_on', String(100), default=datetime.now, onupdate=datetime)
             )
class Post(object):
    pass
mapper(Post, post)
