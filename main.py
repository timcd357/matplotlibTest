import matplotlib.pyplot as plt

import numpy as np

import pandas as pd


def test():
    xls = pd.read_excel("C:\\Users\\timcd\\Desktop\\出库.XLS", date_parser=['2020-01-01'])
    # xls["出库时间"] = pd.to_datetime(xls.出库时间, format="%Y.%m")
    xls["出库时间"] = xls["出库时间"].str[0:7]
    xls.to_excel("C:\\Users\\timcd\\Desktop\\1.xls")
    sum_name = xls.groupby("品名/品规").sum()[["数量", "无税金额"]]
    sum_name = sum_name.sort_values("无税金额", ascending=False)
    sum_name.to_excel("C:\\Users\\timcd\\Desktop\\按品名.xls")
    sum_cus = xls.groupby("客户名称").sum()[["数量", "无税金额"]]
    sun_cus = sum_cus.sort_values("无税金额", ascending=False)
    sum_cus.to_excel("C:\\Users\\timcd\\Desktop\\按客户.xls")

    sum_date = xls.groupby("出库时间").sum()[["数量", "无税金额"]]
    sum_date["无税金额"].plot(kind='bar')
    plt.rcParams['font.sans-serif'] = ['KaiTi']
    plt.show()
    sum_date = sum_date.sort_values("无税金额", ascending=False)
    sum_date.to_excel("C:\\Users\\timcd\\Desktop\\按时间.xls")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
