#!/usr/bin/python3
'''List all State objects from the db hbtn_0e_6_usa'''

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State, City).join(City)
    cur_state = str(result[0][0])
    print(cur_state)
    for row in result:
        if str(row[0]) == cur_state:
            print("    " + str(row[1]))
        else:
            cur_state = str(row[0])
            print(cur_state)
            print("    " + str(row[1]))
    session.close()
