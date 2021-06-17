import pandas as pd

def get_baseline_graph_coords(str_intervals):
    """
    Return: list of baseline coordinates e.g. [('1-5', 3), ('6-10', 8), ...]
    str_intervals: list of strings representing intervals e.g. ['1-5', '6-10', ...]
    """
    interval_centers = list(map(lambda x: sum(map(int, x.split('-')))/2, str_intervals))
    return list(zip(str_intervals, interval_centers))

def get_default_graph_coords(df):
    """Return: list of ('a-b', x%) coordinates for intervals of 5 given dataframe"""
    df['prediction_bin'] = pd.cut(df['prediction'],
                                  bins=range(0,105,5),
                                  labels=[f'{x}-{x+4}' for x in range(1,100,5)])
    prediction_groups = df.groupby(['prediction_bin'])
    positive_event_percentages = []

    for group in prediction_groups.groups:
        val = prediction_groups.get_group(group)['result'].mean()
        positive_event_percentages.append((group, val))

    return positive_event_percentages

def run_gnuplot():
    pass
