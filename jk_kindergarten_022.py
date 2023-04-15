import pandas as pd
import warnings

warnings.filterwarnings('ignore')

df01 = pd.DataFrame({
    '氏名':['佐藤', '鈴木', '高橋', '田中'],
    'クラス':['a001', 'a001', 'a001', 'a001'],
    '数学':[1, 2, 3, 4],
    '国語':[5, 6, 7, 8]
    })
df02 = pd.DataFrame({
    '氏名':['佐藤', '鈴木', '山本'],
    'クラス':['a002', 'a002', 'a002'],
    '数学':[9, 10, 11],
    '国語':[12, 13, 14]
    })
#df99 = pd.concat([df01, df02])
#df99 = pd.concat([df01, df02], ignore_index=True)
df03 = pd.DataFrame({
    '氏名':['佐藤', '鈴木', '加藤'],
    'クラス':['a003', 'a003', 'a003'],
    '数学':[15, 16, 17],
    '国語':[18, 19, 20]
    })
# df99 = pd.concat([df01, df02, df03], keys=['1番目', '2番目', '3番目'])
# print(df99.index)
df04 = pd.DataFrame({
    '氏名':['佐藤', '鈴木', '佐々木'],
    'クラス':['a004', 'a004', 'a004'],
    '数学':[21, 22, 23],
    '社会':[24, 25, 26]
    })
#df99 = pd.concat([df01, df04])
#df99 = pd.concat([df01, df04], join='outer')
#df99 = pd.concat([df01, df04], join='inner')
#df99 = pd.concat([df01, df04], axis=0)
#df99 = pd.concat([df01, df04], axis='index')
#df99 = pd.concat([df01, df04], axis='columns')
#df99 = pd.concat([df01, df02, df03, df04], axis='columns')
#df99 = pd.concat([df01, df02, df03, df04], axis='columns', join='inner')
df01 = df01.set_index('氏名')
df02 = df02.set_index('氏名')
df03 = df03.set_index('氏名')
df04 = df04.set_index('氏名')
df99 = pd.concat([df01, df02, df03, df04], axis='columns', join='inner')
print(df99)



