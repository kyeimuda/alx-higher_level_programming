#!/usr/bin/python3
"""
A script that Changes the name of a State object from the database\
 hbtn_0e_6_usa
"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    change_data = session.query(State).filter(State.id == 2).first()
    change_data.name = "New Mexico"
    session.commit()
    session.close()
