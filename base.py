#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///movies_sqlite3.db')
Session = sessionmaker(bind=engine)

Base = sqlalchemy.orm.declarative_base()
