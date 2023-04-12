import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.options.display.float_format = '{:.0f}'.format

df = pd.read_excel('data01.xlsx', sheet_name='Sheet2')
#print(df)
df.groupby('氏名')
#df_name_mean = df[['氏名', 'kingaku']].groupby('氏名').mean()
# df_name_mean = df[['氏名', 'kingaku']].groupby('氏名').mean()
# print(df_name_mean)
# df_name_sum = df[['氏名', 'kingaku']].groupby('氏名').sum()
# print(df_name_sum)
# df_name_cnt = df[['氏名', 'kingaku']].groupby('氏名').count()
# print(df_name_cnt)
# df_name_size = df[['氏名', 'kingaku']].groupby('氏名').size()
# print(df_name_size)
# df_name_size = df[['氏名', 'kingaku']].groupby('氏名').nth(0)
# print(df_name_size)
# df_name_max = df[['氏名', 'kingaku']].groupby('氏名').max()
# print(df_name_max)
# df_name_min = df[['氏名', 'kingaku']].groupby('氏名').min()
# print(df_name_min)
# df_name_mean = df[['氏名', 'Item', 'kingaku']].groupby(['氏名', 'Item'], as_index=False).mean()
# print(df_name_mean)
# df_name_mean = df[['氏名', 'kingaku']].groupby('氏名').mean()
# print(df_name_mean)
# df_name_mean = df[['氏名', 'kingaku']].groupby(['氏名']).agg('mean')
# print(df_name_mean)
# df_name_mean_sum = df[['氏名', 'kingaku']].groupby(['氏名']).agg(['mean', 'sum'])
# print(df_name_mean_sum)
# df_name_mean_sum = df[['氏名', 'kingaku']].groupby(['氏名']).agg(['mean', 'sum'])
# df_name_mean_sum.applymap('{:,.0f}'.format)
# print(df_name_mean_sum)
# df_group = df[['氏名', 'kingaku']].groupby(['氏名']).agg(['mean', 'sum', 'count', 'max', 'min', 'std', 'var'])
# df_group.applymap('{:,.0f}'.format)
# print(df_group)
# df_group = df[['氏名', 'kingaku']].groupby(['氏名']).agg(['describe'])
# df_group.applymap('{:,.0f}'.format)
# print(df_group)

import numpy as np
def cal_tax(s):
    return np.sum(s)*1.10
df_group = df[['氏名', 'kingaku']].groupby(['氏名']).agg({'kingaku': cal_tax})
df_group.applymap('{:,.0f}'.format)
print(df_group)

