#!/usr/bin/python3
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Sequence, text
from sqlalchemy.orm  import declarative_base, sessionmaker
Base = declarative_base()
metadata = MetaData
# connecting
engine = create_engine('sqlite:///products.db', echo=True)

class User(Base):
    __tablename__ ='users'

    id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s',nickname='%s'>" % (self.name, self.fullname, self.nickname)

#print(Base.metadata.create_all(engine))
Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
# add a single user
mk_user = User(name='Macron', fullname='Macron Kem', nickname='Mac')
mk_user.name ='Festus'
session.add(mk_user)
fake_User = User(name='Fake', fullname='Invalid', nickname='12345')
session.add(fake_User)
session.add_all([
    User(name='ed', fullname='Ed Jones', nickname='ednickname'),
    User(name='Wendy', fullname='Wendy Williams', nickname='Windy'),
    User(name='Mary', fullname='Mary Contrary', nickname='Mary'),
    User(name='Fred', fullname='Fred Flinstone', nickname='Flintstone')
    ])
session.dirty
session.new
#session.query(User).filter(User.name.in_([ 'Festus', 'fake_user'])).all()
#session.rollback()
# issue changes to the database
session.commit()
print(mk_user.id)

# Querying the data

for name, fullname in session.query(User.name, User.fullname).all():
    print(name,fullname)

query = session.query(User.name.like('%ed')).order_by(User.id)
query.all()
query.first()

for user in session.query(User).filter(text("id<224")).order_by(text("id")).all():
    print(user.nickname)

test = session.query(User).filter(User.name.like('%Fred')).count()
print(test)
