#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    session.add(State(name='California'))
    session.commit()
    id_num = [row.id for row in session.query(State).
              filter(State.name == 'California')][0]
    session.add(City(name='San Francicso', state_id=id_num))
    session.commit()
    session.close()
