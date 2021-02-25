from typing import List

import databases
import sqlalchemy

from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

from fastapi import FastAPI
from pydantic import BaseModel

DATABASE_URL = "sqlite:///./test.db"

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User({0},{1},{2})>".format(self.name, self.first_name, self.last_name)








metadata = sqlalchemy.MetaData(DATABASE_URL)
Base.metadata.create_all(engine)




'''
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData(DATABASE_URL)

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("fullname", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
    sqlalchemy.Column("hash_password", sqlalchemy.String)
)

organization = sqlalchemy.Table(
    "organization"
)


metadata.create_all(engine)

'''