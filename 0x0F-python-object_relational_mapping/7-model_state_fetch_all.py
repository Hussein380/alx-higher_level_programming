#!/usr/bin/python3

"""
This script lists all State objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """
    Access to the database and get states
    from the database
    """

    """Construct the database URL using command line arguments"""
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    .format(argv[1],   argv[2], argv[3])

    """Create an SQLAchemy engine"""
    engine = create_engine(db_url)

    """create a configured "Session " class"""
    Session = sessionmaker(bind=engine)

    """Create a session"""
    session = Session()

    """Querry database for all the states objects, ordered by id"""
    for instance in session.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
