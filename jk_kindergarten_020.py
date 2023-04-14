import pandas as pd

df01 = pd.DataFrame({
    '氏名':['高橋', '伊藤', '鈴木', '佐藤'],
    'クラス':['a001', 'a001', 'a001', 'a001'],
    '数学':[100, 82, 63, 74]
    })
df02 = pd.DataFrame({
    '氏名':['高橋', '伊藤', '鈴木', '佐藤'],
    'クラス':['a001', 'a001', 'a001', 'a001'],
    '国語':[55, 96, 47, 88]
    })
#df_merge = pd.merge(df01, df02, on='氏名')
#df_merge = pd.merge(df01, df02, on='氏名', suffixes=['_left', '_right'])
#df_merge = pd.merge(df01, df02, on='氏名', suffixes=['', '_重複'])
df02_name = pd.DataFrame({
    '名前':['高橋', '伊藤', '鈴木', '佐藤'],
    'クラス':['a001', 'a001', 'a001', 'a001'],
    '国語':[55, 96, 47, 88]
    })
df03 = pd.DataFrame({
    '名前':['高橋', '高橋'],
    'クラス':['a001', 'a002'],
    '英語':[81, 88]
    })
df04 = pd.DataFrame({
    '氏名':['高橋', '伊藤', '渡辺', '加藤'],
    'クラス':['a001', 'a001', 'a001', 'a001'],
    '国語':[66, 77, 88, 99]
    })
#df_merge = pd.merge(df01, df04, on='氏名', how='left')
#df_merge = pd.merge(df01, df04, on='氏名',how='right')
#df_merge = pd.merge(df01, df04, on='氏名',how='outer')
#df_merge = pd.merge(df01, df04, on='氏名',how='inner')
#df_merge = pd.merge(df01, df04, on='氏名')
df05 = pd.DataFrame({
    'クラス':['a001', 'a001', 'a001', 'a001'],
    '数学':[100, 82, 63, 74]
    },
    index=['高橋', '伊藤', '鈴木', '佐藤'])
#print(df05)
#df_merge = pd.merge(df05, df02, left_index=True, right_on='氏名')
df_merge = pd.merge(df05, df02, left_index=True, right_on='氏名', sort=True)
print(df_merge)

