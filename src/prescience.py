import pdb

from datetime import datetime
import subprocess

import numpy as np
import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Prediction
from plotting import *

engine = create_engine('sqlite+pysqlite:///testing.db', echo=True)

## TODO add tag support
def make_prediction(event, prediction, result_date, tags=None, *args, **kwargs):
    time = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
    prediction = Prediction(time, event, prediction, result_date, tags)

    with Session(engine) as session:
        session.add(prediction)
        session.commit()

def resolve_predictions(*args, **kwargs):
    today = datetime.now().strftime('%Y-%m-%d')
    stmt = select(Prediction). \
        where(Prediction.result == None). \
        where(Prediction.result_date < today). \
        order_by(Prediction.result_date)

    with Session(engine) as session:
        unresolved = session.execute(stmt)
        for row in unresolved.all():
            prediction = row[0]
            prompt = f'"{prediction.event}" ({prediction.prediction})  ::  '
            while (result := input(prompt)) not in '012':
                continue
            if result != '2':  # 2 = N/A, 1 = True, 0 = False
                prediction.result = int(result)

        session.commit()

## TODO add various paths for stat viewing beyond default graph
def view_stats(*args, **kwargs):

    stmt = "SELECT * FROM prediction WHERE result IS NOT NULL"
    df = pd.read_sql(stmt, engine, index_col='id')
    coordinates = get_default_graph_coords(df)

    breakpoint()
