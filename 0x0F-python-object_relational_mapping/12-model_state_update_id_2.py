#!/usr/bin/python3
"""
This script changes the name of a State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updates a State object on the database.
    """

    """ Constructing the database URL using command line arguments"""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1],
                                                              argv[2], argv[3])

    """Creating an SQLAlchemy engine"""
    engine = create_engine(db_url)

    """Creating a session maker bound to the engine"""
    Session = sessionmaker(bind=engine)

    """Creating a session"""
    session = Session()

    """Querying the State object with id equal to 2"""
    state = session.query(State).filter(State.id == 2).first()

    """Changing the name of the State object"""
    state.name = "New Mexico"

    """# Committing the changes to the database"""
    session.commit()

    """Closing the session"""
    session.close()
