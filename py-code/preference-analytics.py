# -*- coding: utf-8 -*-
"""
Using pandas for data analysis
"""
import os
import time
import numpy as np
import pandas as pd

__author__ = 'Liu Min'

FILENAME = '校园app数据.xlsx'


def main():
    df = pd.read_excel(os.path.join('../dataset', FILENAME))

    # print(df.dtypes)

    # 临港大学城大三学生9月份APP情况
    app_lg = df[(df['校区'] == '临港大学城') &
                (df['出生年份'] == 1997) &
                (df['统计月份'] == 201709)]

    # print(app_lg[app_lg['性别'] == '女'].nlargest(20, columns='uv').tail(19).to_string(col_space=10, justify='center'))
    app_lg[app_lg['性别'] == '女'].nlargest(20, columns='uv').to_json(
        '../result/09-w-2-app-t20.json', force_ascii=False, orient="values")
    app_lg[app_lg['性别'] == '男'].nlargest(20, columns='uv').to_json(
        '../result/09-m-2-app-t20.json', force_ascii=False, orient="values")
    # print(app_lg[app_lg['性别'] == '男'].nlargest(20, columns='uv').tail(19).to_string(col_space=10, justify='center'))


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()  # 程序结束时间
    print("\n[Finished in: {0:.6f} mins = {1:.6f} seconds]".format(
        ((end_time - start_time) / 60), (end_time - start_time)))
