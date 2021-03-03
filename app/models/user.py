import sqlalchemy
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from app.models import Base, DATABASE_URL, engine
from app.models.UserRole import UsersRoles


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    roles = relationship("Role", secondary=UsersRoles, backref="users")

    def __repr__(self):
        return "<User ({0},{1},{2})>".format(self.name, self.first_name, self.last_name)




