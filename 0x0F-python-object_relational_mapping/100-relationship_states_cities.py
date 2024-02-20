#!/usr/bin/python3
"""
Improve the files model_city.py and model_state.py, and save them as
relationship_city.py and relationship_state.py
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    db_url = db_url.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()
