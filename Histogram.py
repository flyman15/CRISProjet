# To draw a histogram
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_csv1(file_path, filed_names):
    df = pd.read_csv(file_path)
    d=[]
    for index,row in df.iterrows():
        d.append(row[filed_names])
    return d


if __name__ == "__main__":
    # read data from csv file
    path = 'Data/rb1910 Price & LastVolume.csv'
    vara_name = 'LastVolume'
    d = read_csv1(path, vara_name)
    # d = pd.read_csv(path)
    # foo = d[d['LastVolume'] != 0]
    # foo1 = foo[vara_name]
    # summary = foo1.describe()
    # print(summary)
    # foo1 = foo1.tolist()

    df = pd.read_csv(path)
    summary= df['LastVolume'].describe()
    print(summary)
    print(d)

    sns.set_style('darkgrid')
    # 设置了20个矩形条，画出频率直方图及核密度估计曲线
    sns.distplot(d, kde=True, rug=False)
    plt.legend(['Price'])
    plt.title(vara_name)
    # plt.xlim((0, 100))
    plt.show()

