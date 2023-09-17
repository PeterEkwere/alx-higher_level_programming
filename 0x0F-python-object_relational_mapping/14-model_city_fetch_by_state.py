#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This script Uses ORm to list all items in a table
    Author: Peter Ekwere

"""
import sqlalchemy
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
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
    city_id = City.id
    query = session.query(City, State).filter(City.state_id == State.id).order_by(city_id)

    for city_instance, state_instance in query:
        print("{}: ({}) {}".format(state_instance.name, city_instance.id,
                                   city_instance.name))

    session.commit()
