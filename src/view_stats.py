import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Prediction

engine = create_engine('sqlite+pysqlite:///testing.db', echo=True)

def view_stats():
    pass

def main():
    view_stats()

if __name__ == '__main__':
    main()
