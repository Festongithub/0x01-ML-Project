#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, String, Column, Text, DateTime, Boolean, Integer
from datetime import datetime

# create the engine
engine = create_engine(
    'sqlite:///sqlite3.db')
# engine connect
engine.connect()
print(engine)

metadata = MetaData()

blog = Table('blog', metadata,
             Column('id', Integer(), primary_key=True),
             Column('post_title', String(200), nullable=False),
             Column('post_slug', String(200), nullable=False),
             Column('content', Text(), nullable=False),
             Column('published', Boolean(),  default=False),
             Column('created_on', DateTime(), default=datetime.now),
             Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now))


for t in metadata.tables:
    print(metadata.tables[t])

print('-------------')

for t in metadata.sorted_tables:
    print(t.name)

print(blog.columns)
print(blog.c)
print(blog.metadata)
print(blog.columns.updated_on)
#User = Table('users', metadata,
             #Colmn('id', Integer(), primary_key=True),
             #olumn('user', String(200), nullable=False),
            # )


#osts Table('posts', metadata,
             #Column('id', Integer(), primary_key=True),
             #Column('post_title', String(200), nullable=False),
             #Column('post_slug', String(200), nullable=False),
             #Column('content', Text(), nullable=False),
             #Column('user_id', ForeignKey(user.c.id)),
             #)

#mployees = Table('employees', metadata,
                 #Column('employee_id', Integer(), primary_key=True),
                 #Column('first_name', String(200), nullable=False),
                 #Column('last_name', String(200), nullable=False),
                 #Column('dob', DateTime(), nullable=False),
                 #Column('designation', String(200), nullable=False),
                 #)
#mployee_details = Table('employee_details', metadata,
                        #Column('employee_id', ForeignKey('employees.employees_id'), primary_key=True),
                        #Column('ssn', String(200), nullable=False),
                        #Column('salary', String(200), nullable=False),
                        #Column('blood_group', String(200), nullable=False),
                        #Column('residential_address', String(200), nullable=False),
                        #)
