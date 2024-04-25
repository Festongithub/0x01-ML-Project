#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import ForeignKey, Column, Integer, String, create_engine
from sqlalchemy.orm import relationship
import Test
from Test import User
from sqlalchemy.orm import declarative_base
engine = create_engine('sqlite:///products.db', echo=True)
Base = sqlalchemy.orm.declarative_base()

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'))

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address

   # User.addresses = relationship("Address", order_by=Address.id, back_populates="user")


# create Address DataBase
print(Base.metadata.create_all(engine))
