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


class UPDOWN:
    def __init__(self, lis, tick_num):
        self.lis = lis
        self.tick_num = tick_num

    def up_down(self):
        i = 0
        flag = []
        for e in range(0, len(self.lis) - self.tick_num):
            foo = 0
            for j in range(1, self.tick_num + 1):
                if self.lis[e + j] > self.lis[e]:
                    foo = 1
                    break
            flag.append(foo)
        return flag


if __name__ == "__main__":
    lis = [1,2,3,4,5,6,1,2,3,4,2,1,0]
    exem = UPDOWN(lis, tick_num=2)
    result = exem.up_down()
    print(result)

    # read data from csv file
    # path = 'Data/rb1910 Price & LastVolume.csv'
    # vara_name = 'LastVolume'
    # # names = ['Time', vara_name]
    # d = pd.read_csv(path)
    #
    # # plot real data
    # yy = d[vara_name]
    # plt.figure(1)
    # plt.plot(range(1, len(yy)+1), yy)
    #
    # # calculate MA data and plot it
    # n = 120
    # exemp = MA(d[vara_name], n)
    # exemp.calculate_ma()
    # plt.plot(range(1+n, len(exemp.MAlist)+n+1), exemp.MAlist)
    #
    # # plot settings
    # plt.grid(True)
    # plt.legend(['True Data', 'MA Data'])
    # plt.title(vara_name)
    # plt.show()




