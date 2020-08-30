from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class SalesContent(Base):
    __tablename__ = 'sales'
    name = Column(String(128))
    title = Column(Integer)
    body = Column(Integer)

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)
