#!/usr/bin/python3
"""
Script to create the 'states' table in the database.
"""
import sys
from sqlalchemy import create_engine
from model_state import Base

if __name__ == "__main__":
    """
    Connects to a MySQL database and creates the 'states' table.
    """
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
