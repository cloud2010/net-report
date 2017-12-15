# -*- coding: utf-8 -*-
"""
Using pandas for data analysis
"""
import os
import time
# import numpy as np
import pandas as pd

__author__ = 'Liu Min'

APP_DATA = '校园app数据.xlsx'
BASE_DATA = '校园基础数据.xls'


def main():
    # APP数据
    df = pd.read_excel(os.path.join('../dataset', APP_DATA))
    # 人数数据
    df_b = pd.read_excel(os.path.join('../dataset', BASE_DATA))

    # print(df.dtypes)

    top_list = ['TOP ' + str(i) for i in range(1, 21)]

    # 各大学城大一至大四10月份APP使用情况按pv指标统计
    with pd.ExcelWriter('../result/10月份APP分析.xlsx') as xls:
        for school in ['临港大学城', '杨浦大学城', '闵行大学城', '松江大学城', '南汇大学城']:
            for age in range(1995, 1999):
                app = df[(df['校区'] == school) & (df['出生年份'] == age) & (df['统计月份'] == 201710)]
                for sex in ['男', '女']:
                    app_top=app[app['性别'] == sex].nlargest(20, columns='uv')
                    app_top['TOP']=top_list
                    sum_stu = df_b[(df_b['性别'] == sex) & (df_b['出生年份'] == age) & (df_b['校区'] == school)]['人数']
                    app_top['渗透率'] = app_top['uv'] / int(sum_stu)
                    app_top['月平均访问人次'] = app_top['pv'] / int(sum_stu)
                    app_top.to_excel(xls, '{0}_10月_{1}_{2}_APP_T20'.format(school, sex, age), index=False)
    
    # 各大学城大一至大四9月份APP使用情况按pv指标统计
    with pd.ExcelWriter('../result/9月份APP分析.xlsx') as xls:
        for school in ['临港大学城', '杨浦大学城', '闵行大学城', '松江大学城', '南汇大学城']:
            for age in range(1995, 1999):
                app = df[(df['校区'] == school) & (df['出生年份'] == age) & (df['统计月份'] == 201709)]
                for sex in ['男', '女']:
                    app_top=app[app['性别'] == sex].nlargest(20, columns='uv')
                    app_top['TOP']=top_list
                    sum_stu = df_b[(df_b['性别'] == sex) & (df_b['出生年份'] == age) & (df_b['校区'] == school)]['人数']
                    app_top['渗透率'] = app_top['uv'] / int(sum_stu)
                    app_top['月平均访问人次'] = app_top['pv'] / int(sum_stu)
                    app_top.to_excel(xls, '{0}_9月_{1}_{2}_APP_T20'.format(school, sex, age), index=False)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()  # 程序结束时间
    print("\n[Finished in: {0:.6f} mins = {1:.6f} seconds]".format(
        ((end_time - start_time) / 60), (end_time - start_time)))
