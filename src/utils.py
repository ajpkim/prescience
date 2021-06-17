import pandas as pd

from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import Session

from models import Prediction

engine = create_engine('sqlite+pysqlite:///testing.db', echo=True)


def print_db_rows():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM prediction'))
        for row in result:
            print(row)

def load_csv(file):
    df = pd.read_csv(file)
    with Session(engine) as session:
        for _, row in df.iterrows():
            prediction = Prediction(prediction_date = row['prediction_date'],
                                    event = row['event'],
                                    prediction = row['prediction'],
                                    result_date = row['result_date'],
                                    result = row['result'],
                                    )
            session.add(prediction)
        session.commit()

