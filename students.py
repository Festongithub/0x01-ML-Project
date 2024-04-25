#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, String, Column, Text, DateTime, Integer, ForeignKey, insert
from datetime import datetime

metadata = MetaData()

engine = create_engine('sqlite:///customer_sqlite3.db')
students = Table('students', metadata,
                 Column('id', Integer(), primary_key=True),
                 Column('student_name', String(200), nullable=False),
                 Column('subject', String(200), nullable=False),
                 Column('registration_number', Integer(), nullable=False),
                 Column('score', Integer(), nullable=False),
                 Column('printed_on', DateTime(), default=datetime.now),
                 Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
                 )

House = Table('house', metadata,
              Column('id', Integer(), primary_key=True),
              Column('house_name', String(200), nullable=False),
              Column('students_id', ForeignKey('students.id')),
              )

for t in metadata.tables:
    print(metadata.tables[t])

print('--------------')

for i in metadata.sorted_tables:
    print(i.name)
print(students.columns.updated_on.type)

# create Data
metadata.create_all(engine)

students_data = insert(students).values(
    student_name = 'Michael Keyls',
    subject = 'Mathematics',
    registration_number = 1234,
    score = 80
    )

#print(str(students_data))
#print(students_data.compile().params)

# connect to the database
conn = engine.connect()
r = conn.execute(students_data,[
    {
        "student_name":"Becky Oyando",
        "subject":"Mathematics",
        "registration_number":1749,
        "score":84
    },
    {
        "student_name":"Dennis Kelvin",
        "subject":"Mathematics",
        "registration_number":2013,
        "score":78
    },
    {
        "student_name":"Brenda Kipkoech",
        "subject": "Mathematics",
        "registration_number":2345,
        "score":67
    },
    {
        "student_name":"Paul Kenyatta",
        "subject":"Mathematics",
        "registration_number":4917,
        "score":"90"
    },
    {
        "student_name":"Becky Lughali",
        "subject":"Mathematics",
        "registration_number":7890,
        "score": 96
    },
    ])

r.rowcount

our_house = [
    {"house_name":"Longonot"},
    
engine = create_engine('sqlite:///students.db', echo=True)

students = Table('students', metadata,
                 Column('id', Integer(), primary_key=True),
                 Column('student_name', String(200), nullable=False),
                 Column('subject', String(200), nullable=False),
                 Column('registration_number', Integer(), nullable=False),
                 Column('score', Integer(), nullable=False),
                 Column('printed_on', DateTime(), default=datetime.now),
                 Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
                 )

House = Table('house', metadata,
              Column('id', Integer(), primary_key=True),
              Column('house_name', String(200), nullable=False),
              Column('students_id', ForeignKey('students.id')),
              )

for t in metadata.tables:
    print(metadata.tables[t])

print('--------------')

for i in metadata.sorted_tables:
    print(i.name)
print(students.columns.updated_on.type)

# create Data
metadata.create_all(engine)

students_data = insert(students).values(
    student_name = 'Michael Keyls',
    subject = 'Mathematics',
    registration_number = 1234,
    score = 80
    )

#print(str(students_data))
#print(students_data.compile().params)

# connect to the database
conn = engine.connect()
r = conn.execute(students_data,[
    {
        "student_name":"Becky Oyando",
        "subject":"Mathematics",
        "registration_number":1749,
        "score":84
    },
    {
        "student_name":"Dennis Kelvin",
        "subject":"Mathematics",
        "registration_number":2013,
        "score":78
    },
    {
        "student_name":"Brenda Kipkoech",
        "subject": "Mathematics",
        "registration_number":2345,
        "score":67
    },
    {
        "student_name":"Paul Kenyatta",
        "subject":"Mathematics",
        "registration_number":4917,
        "score":"90"
    },
    {
        "student_name":"Becky Lughali",
        "subject":"Mathematics",
        "registration_number":7890,
        "score": 96
    },
    ])

r.rowcount

our_house = [
    {"house_name":"Longonot"},
    {"house_name":"Barckely"},
    {"house_name":"Kilimanjaro"},
    {"house_name":"Kenya"},
    {"house_name":"Elgon"},
]]

r = conn.execute(insert(House), our_house)
r.rowcount