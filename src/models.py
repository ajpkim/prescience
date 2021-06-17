from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite+pysqlite:///testing.db', echo=True)
Base = declarative_base()

class Prediction(Base):
    __tablename__ = 'prediction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    prediction_date = Column('prediction_date', String)
    event = Column('event', String)
    prediction = Column('prediction', Float)
    result_date = Column('result_date', String)
    result = Column('result', Integer)

    def __init__(self, prediction_date, event, prediction, result_date, result=None, tags=None):
        self.event = event
        self.prediction_date = prediction_date
        self.prediction = prediction
        self.result_date = result_date
        self.result = result
        self.tags = tags

    def __repr__(self):
        return f"{self.prediction_date} :: {self.event} :: {self.prediction}% :: {self.result}"

Base.metadata.create_all(engine)
