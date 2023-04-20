import pandas as pd
import numpy as np
import re

s2 = pd.Series(['スカートSkirt',
                'ニットKnit',
                'ジャケットJacket',
                'シャツShirt',
                'ロングパンツSlacks'])
s21 = s2.map(lambda x: x[0])
# print(s2)
# print(s21)
s22 = s2.map(lambda x: re.findall('[A-z]+', x))
#print(s22)
s3 = pd.Series(['スカートSkirt',
                'ニットKnit',
                'ジャケットJacket',
                'シャツShirt',
                'BottomsロングパンツSlacks'])
s31 = s3.map(lambda x: re.findall('[A-z]+', x))
#print(s31)
s4 = pd.Series(['スカートSkirt',
                'ニットKnit',
                'ジャケットJacket',
                'シャツShirt',
                np.nan])
#print(s4)
d = {'ジャケットJacket':'outer',
     'スカートSkirt':'bottoms',
     'ニットKnit':'tops',
     'ワンピースonepiece':'onepiece'}
s41 = s4.map(d)
#print(s41)
s42 = s4.map('{}を買います'.format)
#print(s42)
s43 = s4.map('{}を買います'.format, na_action='ignore')
print(s43)



