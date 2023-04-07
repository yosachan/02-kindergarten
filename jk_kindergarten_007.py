import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 2, 3], [4, 5, 6],[7, 8, 9]],
                  columns=["col01", "col02", "col03"],
                  index=["idx01", "idx02", "idx03"])
print(df)
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]]),
                  columns=["col01", "col02", "col03"],
                  index=["idx01", "idx02", "idx03"])
print(df)
print(df.index)
print(df.columns)
df = pd.DataFrame({"col01":[1, 2, 3], "col02":[4, 5, 6], "col03":[7, 8, 9]})
print(df)
df.index=["idx01", "idx02", "idx03"]
df = pd.DataFrame({"col01":[1, 2, 3], "col02":[4, 5, 6], "col03":[7, 8, 9]},
                  index=["idx01", "idx02", "idx03"])
print(df)
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(df)
df.columns=["col01", "col02", "col03"]
df.index=["idx01", "idx02", "idx03"]
print(df)
df.columns=["col04", "col05", "col06"]
print(df)
df=df.rename(columns={"col04": "x"})
print(df)
df=df.rename(columns={"col05": "y", "col06":"z"})
print(df)
df=df.rename(index={"idx01": "w"})
print(df)
print(df["x"])
print(type(df["x"]))
print(df[["x"]])
print(type(df[["x"]]))
print(df.loc['w'])
print(df.loc['w', "z"])
print(df.loc[:, "x"])
print(df.iloc[:, 0])
df = pd.DataFrame([[1, 2, 3], [4, 5, 6],[7, 8, 9]],
                  columns=["col01", "col02", "col03"],
                  index=["idx01", "idx02", "idx03"])
print(df)
print(df.loc['idx01'])
print(df.loc['idx01', "col02"])
print(df.loc[:, "col01"])
print(df.iloc[:, 0])
df = pd.DataFrame([[1, 2, 3], [4, 5, 6],[7, 8, 9]],
                  columns=["col01", "col02", "col03"],
                  index=["idx01", "idx02", "idx03"])
df.loc['idx03', "col02"]=100
print(df.loc['idx03', "col02"])
df.loc[:, "col03"]=["tokyo", "osaka", "nagoya"]
print(df)
print(df.loc[:, "col02":"col03"])
print(df.iloc[:, 1:3])
print(df.index.get_loc("idx03"))
print(df.columns.get_loc("col02"))
df.iloc[df.index.get_loc("idx03"), df.columns.get_loc("col02")]=1000
print(df)
print(df.dtypes)
print(df.shape)
print(df.T)





