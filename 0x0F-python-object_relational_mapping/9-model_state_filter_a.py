#!/usr/bin/python3
"""
script to list all obj that contain letter a
takes 3 args
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    state = session().query(State).filter(text(
        "name LIKE BINARY '%a%'")).order_by(
        State.id).all()
    if state:
        for stat in state:
            print("{}: {}".format(stat.id, stat.name))
    session().close()
