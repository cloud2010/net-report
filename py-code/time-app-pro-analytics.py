# -*- coding: utf-8 -*-
"""
Using pandas for data analysis
- 按年级分类汇总各时段APP的PV排序PRO
- 按性别分类汇总各时段APP的PV排序PRO
"""
import os
import time
import re
import numpy as np
import pandas as pd

__author__ = 'Liu Min'

APP_DATA = '校园APP时段数据.xlsx'
BASE_DATA = '校园基础数据.xls'


def main():
    # APP时段数据
    df_a = pd.read_excel(os.path.join('../dataset', APP_DATA))
    # 人数数据
    df_b = pd.read_excel(os.path.join('../dataset', BASE_DATA))

    pattern = re.compile(u'类应用|浏览器|地图')
    # 数据清洗排除爬虫兴趣标注
    df_a = df_a[(df_a['APP名称'].str.contains(pattern) == 0)]
    # 数值缩放
    df_a['PV'] = df_a.apply(lambda x: x['PV'] if x['APP名称'] not in ['百度贴吧'] else x['PV'] / 3, axis='columns')
    for clock in [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]:
        df = df_a[(df_a['CLOCK'] == clock) | (df_a['CLOCK'] == (clock + 1) % 24)]
        # 按年龄分类汇总统计
        with pd.ExcelWriter('../result/pro-clock-app/{0}_{1}点段_按年级时段分类汇总统计APP.xlsx'.format(clock, clock + 1)) as xls:
            for school in [u'宝山|临港|曹路', u'杨浦|闵行', u'松江']:
                for age in range(1995, 1999):
                    pattern_s = re.compile(school)
                    app = df[(df['大学城'].str.contains(pattern_s) == 1) & (df['年龄'] == age)]
                    g_df = app.groupby(['APP名称']).agg({'CLOCK': np.size, '性别': np.size, 'PV': np.sum}).nlargest(20, columns='PV')
                    # 男生女生总和
                    sum_stu = df_b[(df_b['出生年份'] == age) & (df_b['校区'].str.contains(pattern_s) == 1)]['人数'].sum()
                    g_df['时段平均访问次数'] = g_df['PV'] / int(sum_stu) / 30
                    g_df['学生数'] = int(sum_stu)
                    g_df.to_excel(xls, '{0}_{1}_AGE_T_APP'.format(school, age), index=True)
        # 按性别分类汇总统计
        with pd.ExcelWriter('../result/pro-clock-app/{0}_{1}点段_按性别时段分类汇总统计APP.xlsx'.format(clock, clock + 1)) as xls:
            for school in [u'宝山|临港|曹路', u'杨浦|闵行', u'松江']:
                for sex in ['男', '女']:
                    pattern_s = re.compile(school)
                    app = df[(df['大学城'].str.contains(pattern_s) == 1) & (df['性别'] == sex)]
                    g_df = app.groupby(['APP名称']).agg({'CLOCK' : np.size, '年龄' : np.size, 'PV' : np.sum}).nlargest(20, columns='PV')
                    # 男生女生总和
                    sum_stu = df_b[(df_b['性别'] == sex) & (df_b['校区'].str.contains(pattern_s) == 1)]['人数'].sum()
                    g_df['时段平均访问次数'] = g_df['PV'] / int(sum_stu) / 30
                    g_df['学生数'] = int(sum_stu)
                    g_df.to_excel(xls, '{0}_{1}_SEX_T_APP'.format(school, sex), index=True)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()  # 程序结束时间
    print("\n[Finished in: {0:.6f} mins = {1:.6f} seconds]".format(
        ((end_time - start_time) / 60), (end_time - start_time)))
