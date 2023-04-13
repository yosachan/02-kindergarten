import pandas as pd
import numpy as np

pd.options.display.max_columns = None
pd.options.display.max_rows = None
df = pd.read_excel('data01.xlsx', sheet_name='Sheet2')
#print(df)
# df_pivot = df.pivot_table(index='氏名', columns='Item', values='kingaku', aggfunc='sum')
# print(df_pivot)
#df_pivot = df.pivot_table(index='氏名', values='kingaku', aggfunc='sum')
#df_pivot = df.pivot_table(index='氏名', columns='Item', values='kingaku', aggfunc='mean')
#df_pivot = df.pivot_table(index='氏名', columns='Item', values='kingaku')
# df_pivot = df.pivot_table(index='氏名', columns='Item', values='kingaku')
# df_pivot = df_pivot.applymap('{:,.0f}'.format)
# df_pivot = df.pivot_table(index='氏名', columns='Item', values=['tanka', 'suuryou', 'kingaku'], aggfunc='mean')
# df_pivot = df_pivot.applymap('{:,.0f}'.format)
#df_pivot = df.pivot_table(index=['氏名', '日付'], columns='Item', values=['tanka', 'suuryou', 'kingaku'], aggfunc='mean')
#df_pivot = df.pivot_table(index=['氏名', '日付'], columns='Item', values=['tanka', 'suuryou', 'kingaku'], aggfunc='sum')
#df_pivot = df.pivot_table(index=['氏名', '日付'], columns='Item', values=['tanka', 'suuryou', 'kingaku'], aggfunc='sum', fill_value=0)
#df_pivot = df.pivot_table(index=['氏名', '日付'], values=['suuryou', 'kingaku'], aggfunc='sum', fill_value=0)
#df_pivot = df.pivot_table(index='氏名', columns='Item', values='kingaku', aggfunc='sum', margins=True)
#df_pivot = df.pivot_table(index='氏名', columns='Item', values='kingaku', aggfunc='sum', margins=True, margins_name='合計')
#df_pivot = df.pivot_table(index='氏名', columns='Item', values='kingaku', aggfunc=['sum', 'mean', 'count'])

# def cal_tax(s):
#     return np.sum(s)*1.10
    
# df_pivot = df.pivot_table(index='氏名', columns='Item', values='kingaku', aggfunc=cal_tax)
# df_pivot = df_pivot.applymap('{:,.0f}'.format)

#df = pd.DataFrame({'col01':['A', 'A', 'B', 'B'], 'col02':['a', 'b', 'a', 'b'], 'col03':[1, 2, 3, 4]})
df = pd.DataFrame({'col01':['A', 'A', 'B', 'B'], 'col02':['a', 'b', 'a', 'b'], 'col03':['x', 'y', 'z', 'w']})
#print(df)
#df_pivot = df.pivot(index='col01', columns='col02', values='col03')
df_pivot = df.pivot_table(index='col01', columns='col02', values='col03', aggfunc='first')
print(df_pivot)



