import argparse
from datetime import datetime, timedelta
import random

HEADER = "prediction_date,event,prediction,result_date,result\n"
DATETIME_FMT = "%Y-%m-%d %H:%M:%S"

def add_time_noise(dt, days=5):
    return dt + timedelta(days=random.randint(0,days),
                          hours=random.randint(0,23),
                          minutes=random.randint(1,59))

def main(resolved_rows=500, unresolved_rows=10):
    years = 1 + resolved_rows // (5 * 365)  # 5 predictions a day
    date = datetime.now() - timedelta(weeks=52*years)
    delta_day = timedelta(days=1)

    with open("test-predictions.csv", 'w') as f:
        f.write(HEADER)
        for row in range(resolved_rows):
            prediction_date = add_time_noise(date).strftime(DATETIME_FMT)
            event = f"Test prediction #{row}"
            prediction = random.randint(25,75)
            result = random.randint(0,1)
            result_date = add_time_noise(date,days=3).strftime(DATETIME_FMT)
            f.write(f"{prediction_date},{event},{prediction},{result_date},{result}\n")

            if row % 5 == 0:
                date += delta_day

        for row in range(unresolved_rows):
            prediction_date = add_time_noise(date).strftime(DATETIME_FMT)
            event = f"Unresolved test prediction #{row}"
            prediction = random.randint(1,99)
            result = ''
            result_date = add_time_noise(date,days=3).strftime(DATETIME_FMT)
            f.write(f"{prediction_date},{event},{prediction},{result_date},{result}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('resolved_rows', type=int)
    parser.add_argument('unresolved_rows', type=int)
    args = parser.parse_args()

    main(**vars(args))
