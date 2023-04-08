import pandas as pd

# pd.set_option("display.max_rows", 10)
# df_csv = pd.read_csv("c01.csv", encoding="shift-jis")
# print(df_csv)
# df_csv = pd.read_csv("c01.csv", encoding="shift-jis" ,names=["area-code", "area", "GG", "gg", "yyyy", "YYYY", "tyu", "population", "man", "woman"])
# print(df_csv)
# df_csv = pd.read_csv("c01.csv", encoding="shift-jis", index_col=1)
# print(df_csv)
# print(type(df_csv.index))
# df_csv = pd.read_csv("c01.csv", encoding="shift-jis", index_col=[0, 1, 2, 3, 4, 5])
# print(df_csv.head())
# print(type(df_csv.index))
# print(df_csv.dtypes)
# df_csv.to_csv("c04.csv", encoding="shift-jis")
# print(df_csv)

# df_excel = pd.read_excel("data.xlsx")
# print(df_excel)
# df_excel = pd.read_excel("data.xlsx", skiprows=5)
# print(df_excel)
# df_excel = pd.read_excel("data.xlsx", skiprows=5, header=[1])
# print(df_excel)
# df_excel = pd.read_excel("data.xlsx", skiprows=6, header=None)
# print(df_excel)
# df_excel = pd.read_excel("data.xlsx", index_col=0)
# print(df_excel)
# df_excel.to_excel("data_out.xlsx")
# print(df_excel)
# df_cp = pd.read_clipboard()
# print(df_cp)

import sqlite3
df_csv = pd.read_csv("c01.csv", encoding="shift-jis")
print(df_csv)
dbname = "TEST.db"
conn = sqlite3.connect(dbname)
conn.close()
conn= sqlite3.connect(dbname)
df_csv.to_sql("test_table", conn, if_exists="replace")
conn.close()
conn= sqlite3.connect(dbname)
df_db = pd.read_sql("SELECT * FROM test_table", conn)
conn.close()
print(df_db)
sql = """
select * 
from test_table
where 都道府県名 == '東京都'
"""
conn = sqlite3.connect(dbname)
df_db = pd.read_sql(sql, conn)
conn.close()
print(df_db)
conn =sqlite3.connect(dbname)
for i in range(10):
    df_csv.to_sql("test_table_10", conn, if_exists="append")
conn.close()
sql = '''
select count(*) as cnt
from test_table_10
'''    
conn = sqlite3.connect(dbname)
df_db =pd.read_sql(sql, conn)
conn.close()
print(df_db)
sql = """
select * 
from test_table_100
where 都道府県名 == '東京都' and 西暦（年） == '1920.0'
"""
conn = sqlite3.connect(dbname)
df_db = pd.read_sql(sql, conn)
conn.close()
print(df_db)

















