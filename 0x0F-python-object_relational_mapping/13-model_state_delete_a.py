#!/usr/bin/python3
"""
script to delete all obj that contain letter a
takes 3 args
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import State, Base
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state = session.query(State).filter(text(
        "name LIKE BINARY '%a%'")).all()
    if state:
        for stat in state:
            session.delete(stat)
        session.commit()
    session.close()
