import pandas as pd
import numpy as np

s1=pd.Series([90, 78, 65, 87, 72])
print(s1)
data=[90, 78, 65, 87, 72]
s1=pd.Series(data)
print(s1)
print(np.arange(1, 10, 2))
s2=pd.Series(np.arange(1, 10, 2))
print(s2)
data=np.arange(1, 10, 2)
s2=pd.Series(data)
print(s2)
print(s1.dtypes)
print(s1.index)
s1.index=["sato", "suzuki", "takahashi", "tanaka", "ito"]
print(s1)
print(s1.index)
dict01={"sato":90, "suzuki":78, "takahashi":65, "tanaka":87, "ito":72}
print(dict01)
s3=pd.Series(dict01)
print(s3)
print(s1.values)
print(s1["suzuki"])
print(s1[1])
print(s1[["suzuki", "takahashi"]])
print(s1[[1, 3]])
print(s1 > 80)
print(s1[s1 > 80])
print(s1[s1 <= 80])
print(s1.size)
print(len(s1))
s1.index.name = "member"
s1.name = "score"
print(s1)
print(s1 + 2)
print(s1 - 2)
print(s1 * 2)
print(s1 / 2)
s2.index=["suzuki", "takahashi", "tanaka", "ito", "watanabe"]
print(s1)
print(s2)
print(s1 + s2)
print(s1.hasnans)
s4=pd.Series([90, 78, 65, None, 72])
print(s4.hasnans)
print(pd.isnull(s4))
df = pd.DataFrame([[1, 2, 3], [4, 5, 6],[7, 8, 9]],
                  columns=["col01", "col02", "col03"],
                  index=["idx01", "idx02", "idx03"])
print(df)
print(df["col01"])
print(type(df["col01"]))
s5=pd.Series({"idx01":10, "idx02":11, "idx03":12})
print(s5)
df["col04"]=s5
print(df)
s6=pd.Series({"idx03":13, "idx04":14, "idx05":15})
df["col05"]=s6
print(df)
dates=pd.date_range("2000/01/01", periods=5, freq="D")
print(dates)
print(type(dates))
s1.index=dates
print(s1)