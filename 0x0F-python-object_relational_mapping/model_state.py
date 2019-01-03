#!/usr/bin/python3
'''
Contains the class def of States and an instance
Base = declarative_base()
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''Class def for State'''

    __tablename__ = 'states'
    id = Column(Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True)
    name = Column(String(128),
                  nullable=False)

    def __repr__(self):
        '''REPR form of the class'''
        return "<State(id='%s', name='%s')>" % (self.id, self.name)
