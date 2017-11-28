# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Sequence

# Lazy Connecting
engine = create_engine('sqlite:///:memory:', echo=True)

# Declare a Mapping
Base = declarative_base()
class User(Base):
    __tablename__ = 'table_name'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     fullname = Column(String)
#     password = Column(String)

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)

# Create a Schema
Base.metadata.create_all(engine)

# Create an Instance of the Mapped Class
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

# Creating a Session
Session = sessionmaker(bind=engine)
session = Session()

# Adding and Updating Objects
session.add(ed_user)

session.dirty
session.new

# Commit the transaction
session.commit()

# Close the Session
session.close()

