#!/usr/bin/python3
"""  script that prints the first State
object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    db_url = db_url.format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    record = session.query(State).first()
    if record is None:
        print("Nothing")
    else:
        print(record.id, record.name, sep=": ")
