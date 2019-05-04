import pandas as pd
import time


def read_csv(file_path, filed_names):
    df = pd.read_csv(file_path)
    d = {}
    for name in filed_names:
        d[name] = df[name]
    return d


start = time.clock()
file_path = 'Data/MarketData_20190315_084003.csv'
instrument = 'rb1910'
vara_name = 'LastVolume'
names = ['InstrumentID', vara_name]
df = pd.read_csv(file_path, usecols=names)
print(df)
df1 = df[df['InstrumentID'] == instrument]
df1.to_csv('Data/rb1910.csv', index=False, sep=',')
print(df1)
print(time.clock()-start)
