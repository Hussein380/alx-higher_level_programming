#!/usr/bin/python3

"""
This script prints the first State object
from the database 'hbtn_0e_6_usa'

"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """construct the database URL using command-line arguments"""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    .format(argv[1], argv[2], argv[3])

    """ Create the database engine"""
    engine = create_engine(db_url)

    """Create a session class"""
    Session = sessionmaker(bind=engine)

    """ Create a session """
    session = Session()

    """Query the databse for the first State object and order id """
    state = session.query(State).order_by(State.id).first()

    """" Check if a state object was found"""
    if state is not None:
        print('{0}: {1}'.format(state.id, state.name))
    else:
        print("Nothing")
