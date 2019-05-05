from MA import MA, UPDOWN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def joint_distribution(Na_list, Nb_list, result):
    probability_2d = []
    for e in Nb_list:
        probability_1d = []
        for i in range(0, len(Na_list) - 1):
            select_result = result.loc[(result['XX'] >= Na_list[i]) &
                                       (result['XX'] <= Na_list[i+1]) &
                                       (result['YY'] >= e)]
            z_up = select_result[select_result['ZZ'] == 1]
            if len(select_result.index) > 0:
                probability_1d.append(len(z_up.index)/len(select_result.index))
            else:
                probability_1d.append(0)
        probability_2d.append(probability_1d)
    return probability_2d


path = 'Data/rb1910 Price & LastVolume.csv'
vara_name1 = 'Price'
vara_name2 = 'LastVolume'
d = pd.read_csv(path)
n = 120
exemp = MA(d[vara_name1], n)
exemp.calculate_ma()
print(len(exemp.MAlist) - len(exemp.list[120:]))


price = np.array(exemp.list[n:])
price_MA = np.array(exemp.MAlist)
dist_price = np.subtract(price, price_MA)


last_volume_exemp = MA(d[vara_name2], n)
last_volume_exemp.calculate_ma()
last_volume_MA = last_volume_exemp.MAlist

XX = dist_price
tick_num = 5
ex2 = UPDOWN(price_MA, tick_num)
ZZ = ex2.up_down()
foo = np.array(last_volume_MA)
# q = np.percentile(foo, 80)
# foo[foo <= q] = 0
# foo[foo >= q] = 1
YY = foo
XX = XX[0:len(XX)-tick_num]
YY = YY[0:len(YY)-tick_num]

result = pd.DataFrame({'XX':XX,'YY':YY, 'ZZ':ZZ})
Na_list = np.linspace(result['XX'].min(), result['XX'].max(), 16)
print(Na_list)
percentile_list= np.array([50, 70, 80, 90])
Nb_list = [np.percentile(result['YY'], e) for e in percentile_list]
print(Nb_list)

probability = joint_distribution(Na_list, Nb_list, result)
for e in probability:
    print(e)


# print(select_result['XX'])
#
# sns.set_style('darkgrid')
# # 设置了20个矩形条，画出频率直方图及核密度估计曲线
# sns.distplot(select_result['XX'], kde=True, rug=False)
# plt.legend(['Price'])
# plt.show()