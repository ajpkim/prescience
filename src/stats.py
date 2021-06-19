# import pathlib
from importlib import resources
import subprocess

from sqlalchemy import create_engine
import pandas as pd

from models import Prediction

engine = create_engine('sqlite+pysqlite:///testing.db', echo=True)

def get_stats_df():
    stmt = "SELECT * FROM prediction WHERE result IS NOT NULL"
    return pd.read_sql(stmt, engine, index_col='id')

def get_optimal_coords(observed_coords):
    """
    Return: list of optimal prediction coordinates e.g. [('1-5', 3), ('6-10', 8), ...]
    """
    str_intervals = [xy[0] for xy in observed_coords]
    interval_centers = list(map(lambda x: sum(map(int, x.split('-')))/2, str_intervals))
    return list(zip(str_intervals, interval_centers))

def get_default_observed_coords(df):
    """Return: list of ('a-b', x%) coordinates for intervals of 5 given dataframe"""
    df['prediction_bin'] = pd.cut(df['prediction'],
                                  bins=range(0,105,5),
                                  labels=[f'{x}-{x+4}' for x in range(1,100,5)])
    prediction_groups = df.groupby(['prediction_bin'])
    observed_coords = []

    for group in prediction_groups.groups:
        val = prediction_groups.get_group(group)['result'].mean() * 100
        observed_coords.append((group, val))

    return observed_coords

def write_gnuplot_data(optimal_coords, observed_coords):
    x = optimal_vals = [op[1] for op in optimal_coords]
    observed_vals = [a[1] for a in observed_coords]

    with open('/tmp/prescience.dat', 'w') as f:
        f.write('# x optimal observed')
        for a, b, c in zip(x, optimal_vals, observed_vals):
            f.write(f"{a} {b} {c}\n")

def plot():
    """Plot in terminal with gnuplot script that reads data from /tmp/prescience.dat"""
    gnuplot_script = pathlib.Path(__file__).parent / "gnuplot-default"
    # with resources.open_text('src', 'gnuplot-default') as f:
    #     gnuplot_script = f.read()
    gnuplot = subprocess.Popen("gnuplot", stdin=subprocess.PIPE)
    gnuplot.stdin.write(f'load "{gnuplot_script}"\n'.encode())
    gnuplot.stdin.flush()

def plot_default():
    df = get_stats_df()
    observed_coords = get_default_observed_coords(df)
    optimal_coords = get_optimal_coords(observed_coords)
    write_gnuplot_data(optimal_coords, observed_coords)
    plot()

if __name__ == "__main__":
    plot_default()
