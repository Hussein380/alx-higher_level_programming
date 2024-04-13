#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes State objects on the database.
    """
    """ Construct the database URL using command line arguments"""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3])

    """ Create an SQLAlchemy engine"""
    engine = create_engine(db_url)

    """Create a session class"""
    Session = sessionmaker(bind=engine)

    """Create a session"""
    session = Session()

    """Query for states containing the letter 'a'"""
    states = session.query(State).filter(State.name.contains('a'))
    """Check if any states were found"""
    if states is not None:
        """ Iterate over found states"""
        for state in states:
            """ Delete each state"""
            session.delete(state)
    """ Commit the changes to the database"""
    session.commit()
    """Close the session"""
    session.close()
