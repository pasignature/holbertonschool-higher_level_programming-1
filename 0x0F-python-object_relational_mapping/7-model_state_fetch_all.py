#!/usr/bin/python3
'''List all State objects from the db hbtn_0e_6_usa'''

import sys
from model_state import Base, State

from sqlalchemy import create_engine, select, MetaData, Table

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    states = Table('states', MetaData(bind=None), autoload_with=engine)
    result = engine.connect().execute(select([states])).fetchall()
    for row in result:
        print("{}: {}".format(row[0], row[1]))
