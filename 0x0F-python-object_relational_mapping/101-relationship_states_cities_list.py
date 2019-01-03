#!/usr/bin/python3
'''List all State objects from the db hbtn_0e_6_usa'''

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State, City).join(City)
    cur_sid = 0
    for row in result:
        sid = row[0].id
        sname = row[0].name
        cid = row[1].id
        cname = row[1].name
        if cur_sid != sid:
            print(str(sid) + ": " + sname)
            cur_sid = sid
        print("    " + str(cid) + ": " + cname)
    session.close()
