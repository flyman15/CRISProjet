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


def filter_data1(msg, ID):
    MSG = msg[msg['InstrumentID'] == ID]
    data = MSG[((pd.to_datetime(MSG['UpdateTime'], format='%H:%M:%S')
                 >= pd.to_datetime('00:00:00', format='%H:%M:%S'))
                & (pd.to_datetime(MSG['UpdateTime'], format='%H:%M:%S')
                   < pd.to_datetime('9:00:00', format='%H:%M:%S')))]
    b = data.sort_values(by='UpdateTime', ascending=False)
    return b
