# -*- coding: utf-8 -*-
"""
Using pandas for data analysis
游戏APP 分类汇总分析
"""
import os
import time
import re
import numpy as np
import pandas as pd

__author__ = 'Liu Min'

APP_DATA = '校园app数据.xlsx'
BASE_DATA = '校园基础数据.xls'

def main():
    '''
    主函数
    '''
    # APP数据
    df = pd.read_excel(os.path.join('../dataset', APP_DATA))
    # 人数数据
    df_b = pd.read_excel(os.path.join('../dataset', BASE_DATA))

    pattern = re.compile(u'王者荣耀|游戏|消消乐|飞车|荒野|阴阳师|刀塔|炉石传说|英雄联盟|动漫')
    # 数据清洗排除爬虫兴趣标注
    replace_list = {u'掌上英雄联盟': u'英雄联盟', u'海滨消消乐': u'开心消消乐'}
    # inplace 直接修改源
    df['app名称/类型'].replace(replace_list, inplace=True)
    df = df[(df['app名称/类型'].str.contains(pattern) == 1) & (df['统计月份'] == 201710)]
    # 数值缩放
    df['pv'] = df.apply(lambda x: x['pv'] if x['app名称/类型'] not in ['网易云音乐'] else x['pv'] / 2, axis='columns')
    
    # 按性别分析
    with pd.ExcelWriter('../result/游戏APP按性别分类汇总统计.xlsx') as xls:
        for school in ['临港大学城', '杨浦大学城', '闵行大学城', '松江大学城']:
            for sex in ['男', '女']:
                app = df[(df['校区'] == school) & (df['性别'] == sex)]
                g_df = app.groupby(['app名称/类型']).agg({'出生年份' : np.size, 'pv' : np.sum, 'uv' : np.sum}).nlargest(20, columns='pv')
                sum_stu = df_b[(df_b['性别'] == sex) & (df_b['校区'] == school)]['人数'].sum()
                g_df['渗透率'] = g_df['uv'] / int(sum_stu)
                g_df['月均访问人次'] = g_df['pv'] / int(sum_stu)
                g_df['学生数'] = int(sum_stu)
                g_df.to_excel(xls, '{0}_游戏_{1}_SEX_APP_T20'.format(school, sex), index=True)
    
    # 按年级分析
    with pd.ExcelWriter('../result/游戏APP按年级分类汇总统计.xlsx') as xls:
        for school in ['临港大学城', '杨浦大学城', '闵行大学城', '松江大学城']:
            for age in range(1995, 1999):
                app = df[(df['校区'] == school) & (df['出生年份'] == age)]
                g_df = app.groupby(['app名称/类型']).agg({'性别' : np.size, 'pv' : np.sum, 'uv' : np.sum}).nlargest(20, columns='pv')
                sum_stu = df_b[(df_b['出生年份'] == age) & (df_b['校区'] == school)]['人数'].sum()
                g_df['渗透率'] = g_df['uv'] / int(sum_stu)
                g_df['月均访问人次'] = g_df['pv'] / int(sum_stu)
                g_df['学生数'] = int(sum_stu)
                g_df.to_excel(xls, '{0}_游戏_{1}_AGE_APP_T20'.format(school, age), index=True)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()  # 程序结束时间
    print("\n[Finished in: {0:.6f} mins = {1:.6f} seconds]".format(
        ((end_time - start_time) / 60), (end_time - start_time)))
