import pandas as pd
from filter import filter_data, filter_data1
from datetime import datetime
import time
import numpy as np
start = time.clock()

a = pd.date_range('2019-03-15 09:00:00', '2019-03-15 10:15:00', freq='500ms')
b = pd.date_range('2019-03-15 10:30:00', '2019-03-15 11:30:00', freq='500ms')
c = pd.date_range('2019-03-15 13:30:00', '2019-03-15 15:00:00', freq='500ms')
df = pd.DataFrame(a, columns=['Time'])
df = df.append(pd.DataFrame(b, columns=['Time']))
df = df.append(pd.DataFrame(c, columns=['Time']))
df.to_csv('1.csv', index=False, sep=',')
df.reset_index(drop=True, inplace=True)

data_path1 = 'Data/MarketData_20190315_084003.csv'
data_path2 = '1.csv'

ID = 'rb1910'

msg = pd.read_csv(data_path1)
data = filter_data(msg, ID)
data1 = filter_data1(msg, ID)

data2 = pd.read_csv(data_path2)
print(time.clock()-start)


print(df.iterrows())


for index1, row1 in df.iterrows():
    print(index1, row1)



for index1, row1 in df.iterrows():
    print(type(df.iterrows()))
    millisec = datetime.utcfromtimestamp(row1['Time'].timestamp()).timestamp() * 1000
    print(time.clock() - start)
    for index2, row2 in data.iterrows():
        dt_obj = datetime.strptime('2019-03-15 ' + row2['UpdateTime'], '%Y-%m-%d %H:%M:%S')
        time_millisec = dt_obj.timestamp() * 1000 + row2['UpdateMillisec']
        if millisec == time_millisec:
            p = [row2['LastPrice'], row2['AskPrice1'], row2['BidPrice1']]
            p.sort()
            df = df.copy()
            df.loc[df.index[index1], ID] = p[1]
            break
    # if np.isnan(df[ID][index1]):
    #     if index1 == 0:
    #         if data1.empty:
    #             df[ID] = pd.DataFrame([0], index=[0])
    #         else:
    #             p = [data1.head(1)['LastPrice'], data1.head(1)['AskPrice1'], data1.head(1)['BidPrice1']]
    #             p.sort()
    #             df = df.copy()
    #             df.loc[df.index[index1], ID] = p[1]
    #     else:
    #         df = df.copy()
    #         df.loc[df.index[index1], ID] = df.loc[df.index[index1 - 1], ID]
df.to_csv('1.csv', index=False, sep=',')




