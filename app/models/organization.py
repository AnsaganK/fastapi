from app.models import Base
from sqlalchemy import Column, Integer, String

class Organization(Base):
    __tablename__ = "organization"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    bin = Column(String)
    organizationId = Column(String)

    def __repr__(self):
        return "<organization ({})>".format(self.name)