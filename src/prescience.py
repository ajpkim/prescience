from datetime import datetime

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import Prediction

engine = create_engine('sqlite+pysqlite:///testing.db', echo=True)

def make_prediction(event, prediction, result_date, tags=None, *args, **kwargs):
    prediction = Prediction(event, prediction, result_date, tags)

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
            if result != 2:  # 2 = N/A, 1 = True, 0 = False
                prediction.result = int(result)

        session.commit()

def view_stats(*args, **kwargs):
    pass
