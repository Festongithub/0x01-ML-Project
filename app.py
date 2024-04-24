#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm  import declarative_base

engine = create_engine('sqlite:///users_sqlite3.db', echo=True)

Base = declarative_base()

class User(Base):
    __table__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s'>" % (self.name, self.fullname, self.nickname)


# create the schema
print(User.__table__)
