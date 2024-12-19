import pandas as pd
import sqlite3

csv_file='LakeCounty_Health.csv'
data=pd.read_csv(csv_file)

db_file='./database/obesity.db'
connection=sqlite3.connect(db_file)

table_name='obesity_data'
data.to_sql(table_name,connection,if_exists='replace',index=False)

result=pd.read_sql(f"select * from {table_name} LIMIT 5",connection)
print(result)
