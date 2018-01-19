# -*- coding: utf-8 -*-
"""
Using pandas for data analysis
-APP整体情况分类汇总分析
"""
import os
import time
import re
import numpy as np
import pandas as pd

__author__ = 'Liu Min'

APP_DATA = '校园app数据.xlsx'
BASE_DATA = '校园基础数据.xls'

def scale_pv(x):
    '''
    缩放PV值
    '''
    s_pv = x['pv']
    if x['app名称/类型'] == '微信朋友圈':
        s_pv = x['pv'] / 4
    if x['app名称/类型'] == '微博':
        s_pv = x['pv'] / 3.5
    if x['app名称/类型'] == '百度贴吧':
        s_pv = x['pv'] / 2
    if x['app名称/类型'] == '高德地图':
        s_pv = x['pv'] / 6
    if x['app名称/类型'] == '百度地图':
        s_pv = x['pv'] / 3
    return s_pv

def main():
    '''
    主函数
    '''
    # APP数据
    df = pd.read_excel(os.path.join('../dataset', APP_DATA))
    # 人数数据
    df_b = pd.read_excel(os.path.join('../dataset', BASE_DATA))
    # 标签替换
    replace_list = {u'腾讯类应用': u'微信朋友圈'}
    # inplace 直接修改源
    df['app名称/类型'].replace(replace_list, inplace=True)
    # 数据清洗排除爬虫兴趣标注
    pattern = re.compile(u'类应用|浏览器|微云|商店')
    pattern_s = re.compile(u'大学城|校区')
    df = df[(df['app名称/类型'].str.contains(pattern) == 0) & (df['统计月份'] == 201710) & (df['校区'].str.contains(pattern_s) == 1)]
    # 数值缩放
    df['scale_pv'] = df.apply(scale_pv, axis='columns')
    
    # 按性别分析
    with pd.ExcelWriter('../result/整体APP按性别分类汇总统计.xlsx') as xls:
        for sex in ['男', '女']:
            app = df[(df['性别'] == sex)]
            g_df = app.groupby(['app名称/类型']).agg({'出生年份' : np.size, 'pv' : np.sum, 'uv' : np.sum, 'scale_pv' : np.sum}).nlargest(20, columns='scale_pv')
            sum_stu = df_b[(df_b['性别'] == sex) & (df_b['校区'].str.contains(pattern_s) == 1)]['人数'].sum()
            g_df['渗透率'] = g_df['uv'] / int(sum_stu)
            g_df['月均访问人次'] = g_df['scale_pv'] / int(sum_stu)
            g_df['学生数'] = int(sum_stu)
            g_df.to_excel(xls, '{0}_整体_SEX_APP_T20'.format(sex), index=True)
    
    # 按年级分析
    with pd.ExcelWriter('../result/整体APP按年级分类汇总统计.xlsx') as xls:
        for age in range(1995, 1999):
            app = df[(df['出生年份'] == age)]
            g_df = app.groupby(['app名称/类型']).agg({'性别' : np.size, 'pv' : np.sum, 'uv' : np.sum, 'scale_pv' : np.sum}).nlargest(20, columns='scale_pv')
            sum_stu = df_b[(df_b['出生年份'] == age) & (df_b['校区'].str.contains(pattern_s) == 1)]['人数'].sum()
            g_df['渗透率'] = g_df['uv'] / int(sum_stu)
            g_df['月均访问人次'] = g_df['scale_pv'] / int(sum_stu)
            g_df['学生数'] = int(sum_stu)
            g_df.to_excel(xls, '{0}_整体_AGE_APP_T20'.format(age), index=True)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()  # 程序结束时间
    print("\n[Finished in: {0:.6f} mins = {1:.6f} seconds]".format(
        ((end_time - start_time) / 60), (end_time - start_time)))
