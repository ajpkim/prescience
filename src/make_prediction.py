import argparse

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

from models import Prediction

engine = create_engine('sqlite+pysqlite:///testing.db', echo=True)

def make_prediction(event, prediction, result_date, tags=None):
    prediction = Prediction(event, prediction, result_date, tags)

    with Session(engine) as session:
        session.add(prediction)
        session.commit()

def main(*args, **kwargs):
    # engine = create_engine('sqlite+pysqlite:///testing.db', echo=True)

    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--event', help='Describe prediction event')
    parser.add_argument('-p', '--prediction', help='0%-100% likelihood of event happening')
    parser.add_argument('-d', '--result_date', help='Date when the outcome of event will be known')
    parser.add_argument('-t', '--tags', nargs='+', help='Optional tags')
    args = parser.parse_args()

    make_prediction(**vars(args))
    # prediction = Prediction(**vars(args))
    
    # with Session(engine) as session:
    #     session.add(prediction)
    #     session.commit()
        
if __name__ == '__main__':
    main()
    
