import pandas as pd
import numpy as np
import re

def double(x):
    return x * 2

def f_rank(x):
    if x >= 20000:
        return 'S'
    elif x >= 10000:
        return 'A'
    elif x >= 5000:
        return 'B'
    else:
        return 'C'

def f_tax(x, tax):
    return x*tax + x

s1 = pd.Series([7000, 5000, 23000, 2500, 12000])
s12 = s1.apply(double)
s13 = s1.apply(lambda x: x*2)
s14 = s1.apply(lambda x: '1万円以上' if x >= 10000 else '1万円未満')
s15 = s1.apply(f_rank)
s16 = s1.apply(f_tax, args=(0.1, ))
s17 = s1.apply(np.square)
s2 = pd.Series(['スカートSkirt',
                'ニットKnit',
                'ジャケットJacket',
                'シャツShirt',
                'ロングパンツSlacks'])
s21 = s2.apply(lambda x: x[0])
s22 = s2.apply(lambda x: re.findall('[A-z]+', x))
d = {'ジャケットJacket':'outer',
     'スカートSkirt':'bottoms',
     'ニットKnit':'tops',
     'ワンピースonepiece':'onepiece'}
#s23 = s2.apply(d) # NG
s4 = pd.Series(['スカートSkirt',
                'ニットKnit',
                'ジャケットJacket',
                'シャツShirt',
                np.nan])
s41 = s4.apply('{}を買います'.format)
s42 = s4.apply('{}を買います'.format, na_action='ignore')
#print(s41)

df = pd.DataFrame(
    [[11000, 6000, 8000],
     [5000, 12000, 6000],
     [4000, 5000, 9000]],
    columns=['1日', '2日', '3日'],
    index=['Aさん', 'Bさん', 'Cさん']
)
df01 = df * 2
df02 = df.applymap(double)
df03 = df.applymap(lambda x: x*2)
df04 = df.applymap(lambda x: '1万円以上' if x >= 10000 else '1万円未満')
df05 = df.applymap(f_rank)
#df06 = df.applymap(f_tax, args=(0.1, )) #NG
df07 = df.mask(df < 10000, '1万円未満')
df08 = df < 10000
df09 = df.where(df < 10000, '1万円以上')
df10 = df.applymap(np.square)
#df11 = df.applymap(np.sum) #NG
df12 = df.sum()
#print(df12)

df2 = pd.DataFrame(
        [['スカートSkirt', 'ニットKnit', 'ジャケットJacket'],
         ['シャツShirt', 'ロングパンツSlacks', 'ワンピースonepiece']],
        columns=['x', 'y', 'z']
)
df21 = df2.applymap(lambda x: x[0])
df22 = df2.applymap(lambda x: re.findall('[A-z]+', x))
df13 = df.apply(double)
df14 = df.apply(lambda x: x*2)
#df15 = df.apply(lambda x: '1万円以上' if x >= 10000 else '1万円未満')
# NG
df16 = df.apply(lambda x: x >= 10000)
df17 = df['1日'].apply(lambda x: '1万円以上' if x >= 10000 else '1万円未満')
df18 = df.apply(f_tax, args=(0.1, ))
df19 = df.apply(np.square)
df1_20 = df.apply(np.sum)
df1_21 = df.apply(np.sum, axis=1)
df1_22 = df.apply(lambda x: max(x) - min(x))
df23 = df2.apply(lambda x: x[0])
#df24 = df2.apply(lambda x: re.findall('[A-z]+', x))
# NG
print(df23)










