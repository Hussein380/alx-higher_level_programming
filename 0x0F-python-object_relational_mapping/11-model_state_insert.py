#!/usr/bin/python3
"""
This script adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Main block of the script, executed only if the script is run directly
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    .format(argv[1], argv[2], argv[3])

    """ Create the database engine"""
    engine = create_engine(db_url)

    """Create a session class """
    Session = sessionmaker(bind=engine)

    """ Create a session object"""
    session = Session()

    """ Create a new State object with the name "Louisiana" """
    new_state = State(name="Louisiana")

    """Add the new State object to the session """
    session.add(new_state)

    """Commit the transaction to the database """
    session.commit()

    """ Print the ID of the newly added State object"""
    print('{0}'.format(new_state.id))

    """ Close the session"""
    session.close()
