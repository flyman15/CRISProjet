# To implement MA method
import matplotlib.pyplot as plt
import pandas as pd


class MA:
    def __init__(self, lis, n):
        self.list = lis
        self.n = n
        self.MAlist = []

    def calculate_ma(self):
        for i in range(self.n, len(self.list)):
            foo = sum(self.list[i - self.n:i]) / self.n
            self.MAlist.append(foo)


def read_csv(file_path, filed_names):
    df = pd.read_csv(file_path)
    d = {}
    for name in filed_names:
        d[name] = df[name]
    return d


if __name__ == "__main__":
    # read data from csv file
    path = 'Data/1.csv'
    vara_name = 'cu1904'
    names = ['Time', vara_name]
    d = read_csv(path, names)

    # plot real data
    yy = d[vara_name]
    plt.figure(1)
    plt.plot(range(1, len(yy)+1), yy)

    # calculate MA data and plot it
    n = 120
    exemp = MA(d[vara_name], n)
    exemp.calculate_ma()
    plt.plot(range(1+n, len(exemp.MAlist)+n+1), exemp.MAlist)

    # plot settings
    plt.grid(True)
    plt.legend(['True Data', 'MA Data'])
    plt.title(vara_name)
    plt.show()




