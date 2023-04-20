import pandas as pd
import numpy as np

s1 = pd.Series([7000, 15000, 21000, 30000, 2000])
#print(s1)
#s2 = s1 * 2
#print(s2)
def double(x):
    return x * 2
s3 = s1.map(double)
#print(s3)
s4 = s1.map(lambda x: x *2)
#print(s4)
s5 = s1.map(lambda x: '一万円以上' if x >= 10000 else '一万円未満')
#print(s5)
def f_rank(x):
    if x >= 20000:
        return 'S'
    elif x >= 10000:
        return 'A'
    elif x >= 5000:
        return 'B'
    else:
        return 'C'
s6 = s1.map(f_rank)
#print(s6)
s7 = s1.map(np.square)
#print(s7)
s8 = s1.map(np.sum)
#print(s8)
s9 = s1.sum()
print(s9)











