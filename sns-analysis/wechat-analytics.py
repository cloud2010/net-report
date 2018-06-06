# -*- coding: utf-8 -*-
"""
Using pandas for data analysis
wechat 问卷之星数据分类汇总分析
"""
import os
import time
import re
import numpy as np
import pandas as pd

__author__ = 'Liu Min'

APP_DATA = '531_531_0.xls'


def main():
    '''
    主函数
    '''
    # 问卷之星数据
    df = pd.read_excel(os.path.join('../dataset', APP_DATA))

    pattern = re.compile(u'无|没有|i信工')
    # 数据清洗排除爬虫兴趣标注
    df = df[(df['1、你最爱阅读的微信公众号'].str.contains(pattern) == 0)]

    # 按年级分析
    with pd.ExcelWriter('../result/问卷之星按年级分类汇总统计.xlsx') as xls:
        for grade in ['大一', '大二', '研究生']:
            app = df[(df['2、您目前就读：［单选题］'] == grade)]
            g_df = app.groupby(['1、你最爱阅读的微信公众号']).agg({'3、您的性别：［单选题］': np.size}).sort_values(by=['3、您的性别：［单选题］'], ascending=False)
            g_df.to_excel(xls, '{0}_wechat'.format(grade), index=True)

    # 按性别分析
    with pd.ExcelWriter('../result/问卷之星按性别分类汇总统计.xlsx') as xls:
        for sex in ['男', '女']:
            app = df[(df['3、您的性别：［单选题］'] == sex)]
            g_df = app.groupby(['1、你最爱阅读的微信公众号']).agg({'2、您目前就读：［单选题］': np.size}).sort_values(by=['2、您目前就读：［单选题］'], ascending=False)
            g_df.to_excel(xls, '{0}_wechat'.format(sex), index=True)

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()  # 程序结束时间
    print("\n[Finished in: {0:.6f} mins = {1:.6f} seconds]".format(
        ((end_time - start_time) / 60), (end_time - start_time)))
