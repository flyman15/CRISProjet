import pandas as pd

def filter_data(msg, ID):
    MSG = msg[msg['InstrumentID'] == ID]
    data = MSG[((pd.to_datetime(MSG['UpdateTime'], format='%H:%M:%S')
                 >= pd.to_datetime('09:00:00', format='%H:%M:%S'))
                & (pd.to_datetime(MSG['UpdateTime'], format='%H:%M:%S')
                   <= pd.to_datetime('10:15:00', format='%H:%M:%S')))
               | ((pd.to_datetime(MSG['UpdateTime'], format='%H:%M:%S')
                   >= pd.to_datetime('10:30:00', format='%H:%M:%S'))
                  & (pd.to_datetime(MSG['UpdateTime'], format='%H:%M:%S')
                     <= pd.to_datetime('11:30:00', format='%H:%M:%S')))
               | ((pd.to_datetime(MSG['UpdateTime'], format='%H:%M:%S')
                   >= pd.to_datetime('13:30:00', format='%H:%M:%S'))
                  & (pd.to_datetime(MSG['UpdateTime'], format='%H:%M:%S')
                     <= pd.to_datetime('15:00:00', format='%H:%M:%S')))]
    return data


data_path = 'MarketData_20190315_084003.csv'
ID = 'rb1910'

msg = pd.read_csv(data_path)
data = filter_data(msg, ID)
new_data = pd.DataFrame(columns=['Price', 'LastVolume'])

for index, row in data.iterrows():
    p = [row['LastPrice'], row['AskPrice1'], row['BidPrice1']]
    p.sort()
    new_data.loc[new_data.shape[0]+1] = {'Price': p[1], 'LastVolume': row['LastVolume']}
new_data.to_csv('rb1910 Price & LastVolume.csv', index=False, sep=',')



