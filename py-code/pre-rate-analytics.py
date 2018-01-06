# -*- coding: utf-8 -*-
"""
Using pandas for data analysis
五类兴趣分析
"""
import os
import time
import re
# import numpy as np
import pandas as pd

__author__ = 'Liu Min'

APP_DATA = '校园兴趣数据（9月10月）.xlsx'
BASE_DATA = '校园基础数据.xls'


def main():
    # APP数据
    df = pd.read_excel(os.path.join('../dataset', APP_DATA))
    # 人数数据
    df_b = pd.read_excel(os.path.join('../dataset', BASE_DATA))

    # print(df.dtypes)

    top_list = ['TOP ' + str(i) for i in range(1, 7)]

    pattern = re.compile(u'QQ|软件|手机|公司')
    # 数据清洗排除爬虫兴趣标注
    df = df[(df['兴趣分类3'].str.contains(pattern) == 0) & (df['统计月份'] == 201710)]
    # 各大学城大一至大四10月份APP使用情况按pv指标统计
    with pd.ExcelWriter('../result/10月份五类兴趣分析.xlsx') as xls:
        for hobby in ['生活资讯', '娱乐休闲', '网络科技', '投资理财', '文体教育']:
            # for school in ['临港大学城', '杨浦大学城', '闵行大学城', '松江大学城', '南汇大学城']:
            for school in ['临港大学城', '闵行大学城', '松江大学城']:
                for age in range(1996, 1998):
                    app = df[(df['校区'] == school) & (df['出生年份'] == age) & (df['兴趣分类1'] == hobby)]
                    for sex in ['男', '女']:
                        app_top = app[app['性别'] == sex].nlargest(8, columns='pv')
                        sum_stu = df_b[(df_b['性别'] == sex) & (df_b['出生年份'] == age) & (df_b['校区'] == school)]['人数']
                        app_top['使用率'] = app_top['uv'] / int(sum_stu)
                        app_top['日平均访问次数'] = app_top['pv'] / int(sum_stu) / 30
                        # app_top['TOP'] = top_list
                        app_top['学生数'] = int(sum_stu)
                        app_top.to_excel(xls, '{0}_10月_{1}_{2}_{3}_P_T5'.format(school, sex, age, hobby), index=False)
    

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()  # 程序结束时间
    print("\n[Finished in: {0:.6f} mins = {1:.6f} seconds]".format(
        ((end_time - start_time) / 60), (end_time - start_time)))
