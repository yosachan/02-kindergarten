import pandas as pd

pd.options.display.max_rows = None
pd.options.display.max_columns = None

df01 = pd.read_csv('sample01.csv', encoding='shift-jis', header=0)
#df01.info()
df01['売上日'] = pd.to_datetime(df01['売上日'])
df_01 = df01.set_index('売上日')
#df_01.info()
df02 = pd.read_csv('sample02.csv', encoding='shift-jis', header=0)
df02['売上日'] = pd.to_datetime(df02['売上日'], format='%Y年%m月%d日')
#print(df02)
#df02.info()
df_02 = df02.set_index('売上日')
#print(df_02)
df = pd.read_csv('sample01.csv', encoding='shift-jis', header=0, parse_dates=True, index_col='売上日')
#print(df_02['2023-01-03':'2023-01-05'])
df_03 = df[['売上']]
# print(df_03.resample('M').sum())
# print(df_03.resample('Q').sum())
# print(df_03.resample('10D').sum())
# print(df_03.resample('M').mean())
# print(df_03.resample('M').max())
# print(df_03.resample('M').min())
# print(df_03.resample('Q').agg(['sum', 'mean', 'max', 'min']))
# print(df_03.index.weekday)
# print(df_03[df_03.index.weekday==0])
# print(df_03[df_03.index.weekday==0].mean())
df_04 = df_03.set_index(df_03.index.weekday)
print(df_04)
df_04_01 = df_04.index.name = "曜日番号"
print(df_04_01)
df_99 = df_04.sum(level="曜日番号").sort_index()
print(df_99)