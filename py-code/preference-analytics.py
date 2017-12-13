# -*- coding: utf-8 -*-
"""
Using pandas for data analysis
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

__author__ = 'Liu Min'

FILENAME = '校园app数据.xlsx'

df = pd.read_excel(os.path.join('dataset', FILENAME))

# print(df.dtypes)

# 临港大学城大三学生10月份APP情况
app_lg = df[(df['校区'] == '临港大学城') & 
            (df['出生年份'] == 1997) & 
            (df['统计月份'] == 201709)]

# print(app_lg[app_lg['性别'] == '女'].nlargest(20, columns='uv').tail(19).to_string(col_space=10, justify='center'))
# print(app_lg[app_lg['性别'] == '男'].nlargest(20, columns='uv').tail(19).to_string(col_space=10, justify='center'))
sns.set()
plt.rcParams['font.sans-serif']=['SimHei']
n_groups = 10
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.4
error_config = {'ecolor': '0.3'}

# rects1 = plt.bar(index, app_lg[app_lg['性别'] == '女'].nlargest(20, columns='uv')['uv'], bar_width,
#                  alpha=opacity,
#                  label='女')

rects2 = plt.bar(index + bar_width, app_lg[app_lg['性别'] == '男'].nlargest(n_groups, columns='uv')['uv'], bar_width,
                 alpha=opacity,
                 label='男')

plt.xlabel('APP名称')
plt.ylabel('UV')
plt.title('APP使用情况')
plt.xticks(index, app_lg[app_lg['性别'] == '男'].nlargest(n_groups, columns='uv')['app名称/类型'])
plt.legend()

plt.tight_layout()

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.00*height,
                '%d' % int(height),
                ha='center', va='bottom')

# autolabel(rects1)
autolabel(rects2)
plt.show()