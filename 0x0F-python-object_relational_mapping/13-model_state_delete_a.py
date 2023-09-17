#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This script Uses ORM to list all items in a table
    Author: Peter Ekwere

"""
import sqlalchemy
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, dbname), pool_pre_ping=True
            )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state_id = State.id

    for instance in session.query(State).order_by(state_id):
        if instance.id == 2:
            instance.name = 'New Mexico'

    session.commit()
