from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite+pysqlite:///testing.db', echo=True)
Base = declarative_base()

class Prediction(Base):
    __tablename__ = 'prediction'

    id = Column(Integer, primary_key=True)
    event = Column('event', String)
    prediction = Column('prediction', Integer)
    result_date = Column('result_date', String)
    result = Column('result', Integer)

    def __init__(self, event, prediction, result_date, tags=None):
        self.event = event
        self.prediction = prediction
        self.result = None
        self.result_date = result_date
        self.tags = tags

    def __repr__(self):
        s = f"{self.event} :: {self.prediction}% :: {self.result} :: {self.result_date}"
        s += f" :: {' '.join(self.tags)}" if self.tags else ""
        return s

Base.metadata.create_all(engine)
