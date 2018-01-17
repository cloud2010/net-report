# -*- coding: utf-8 -*-
"""
Using pandas for data analysis
- 按年级分类汇总五类兴趣PV排序
- 按性别分类汇总五类兴趣PV排序
"""
import os
import time
import re
import numpy as np
import pandas as pd

__author__ = 'Liu Min'

APP_DATA = '校园兴趣数据（9月10月）.xlsx'
BASE_DATA = '校园基础数据.xls'


def main():
    # APP数据
    df = pd.read_excel(os.path.join('../dataset', APP_DATA))
    # 人数数据
    df_b = pd.read_excel(os.path.join('../dataset', BASE_DATA))

    # top_list = ['TOP ' + str(i) for i in range(1, 7)]

    pattern = re.compile(u'QQ|软件|手机|公司|体育|b2b')
    # 数据清洗排除爬虫兴趣标注
    df = df[(df['兴趣分类3'].str.contains(pattern) == 0) & (df['统计月份'] == 201710)]
    # 数值缩放
    df['pv'] = df.apply(lambda x: x['pv'] if x['兴趣分类3'] not in ['购物', '门户', '地图'] else x['pv'] / 10, axis='columns')
    # 按年龄分类汇总统计
    with pd.ExcelWriter('../result/按年级分类汇总统计兴趣.xlsx') as xls:
        for hobby in ['生活资讯', '娱乐休闲', '投资理财', '文体教育']:
            for school in ['临港大学城', '闵行大学城', '杨浦大学城', '松江大学城']:
                for age in range(1995, 1999):
                    app = df[(df['校区'] == school) & (df['出生年份'] == age) & (df['兴趣分类1'] == hobby)]
                    g_df = app.groupby(['兴趣分类3']).agg({'性别' : np.size, 'pv' : np.sum, 'uv' : np.sum}).nlargest(10, columns='pv')
                    # 男生女生总和
                    sum_stu = df_b[(df_b['出生年份'] == age) & (df_b['校区'] == school)]['人数'].sum()
                    g_df['u_rate'] = g_df['uv'] / int(sum_stu)
                    g_df['日平均访问次数'] = g_df['pv'] / int(sum_stu) / 30
                    g_df['使用率'] = g_df.apply(lambda x: 1 if x['u_rate'] > 1 else x['u_rate'], axis='columns')
                    g_df['学生数'] = int(sum_stu)
                    g_df.to_excel(xls, '{0}_10月_{1}_{2}_AGE_T5'.format(school, age, hobby), index=True)
    # 按性别分类汇总统计
    with pd.ExcelWriter('../result/按性别分类汇总统计兴趣.xlsx') as xls:
        for hobby in ['生活资讯', '娱乐休闲', '投资理财', '文体教育']:
            for school in ['临港大学城', '闵行大学城', '杨浦大学城', '松江大学城']:
                for sex in ['男', '女']:
                    app = df[(df['校区'] == school) & (df['性别'] == sex) & (df['兴趣分类1'] == hobby)]
                    g_df = app.groupby(['兴趣分类3']).agg({'出生年份' : np.size, 'pv' : np.sum, 'uv' : np.sum}).nlargest(10, columns='pv')
                    # 男生女生总和
                    sum_stu = df_b[(df_b['性别'] == sex) & (df_b['校区'] == school)]['人数'].sum()
                    g_df['u_rate'] = g_df['uv'] / int(sum_stu)
                    g_df['日平均访问次数'] = g_df['pv'] / int(sum_stu) / 30
                    g_df['使用率'] = g_df.apply(lambda x: 1 if x['u_rate'] > 1 else x['u_rate'], axis='columns')
                    g_df['学生数'] = int(sum_stu)
                    g_df.to_excel(xls, '{0}_10月_{1}_{2}_SEX_T5'.format(school, sex, hobby), index=True)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()  # 程序结束时间
    print("\n[Finished in: {0:.6f} mins = {1:.6f} seconds]".format(
        ((end_time - start_time) / 60), (end_time - start_time)))
