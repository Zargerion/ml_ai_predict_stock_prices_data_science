import datetime
import numpy as np

def toTime(time):
    timestamp = time / 1000
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt

def create_dataset(df):
    x = []
    y = []
    shapes = df.shape[0]
    ranges = range(50, df.shape[0])
    for i in range(50, df.shape[0]):
        x.append(df[i-50:i, 0])
        y.append(df[i, 0])
    x = np.array(x)
    y = np.array(y)
    return x,y