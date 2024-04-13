#!/usr/bin/python3

"""
This script lists all State objects
that contain the letter a
from the database 'hbtn_0e_6_usa'
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Constructing the database URL using command line arguments
    """
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    """ Creating the database engine"""
    engine = create_engine(db_url)

    """ Creating a Session class """
    Session = sessionmaker(bind=engine)

    """Creating a session object """
    session = Session()

    """ Querying the database to get all State objects
    that contain the letter """
    states = session.query(State).filter(State.name.contains('a'))

    """ Checking if there are any states returned from the query"""
    if states is not None:
        for state in states:
            print('{0}: {1}'.format(state.id, state.name))
