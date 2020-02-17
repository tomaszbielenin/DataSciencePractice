import pandas as pd
import numpy as np
import sqlalchemy as sa
from matplotlib import pyplot as plt

engine = sa.create_engine('mssql+pyodbc://PLKTW0-APP001/Cadworx_Request?driver=SQL+Server+Native+Client+11.0', echo=True)

# sql = """SELECT Pr_Name, Req_Date, COUNT(Req_Date) as Cnt FROM
# (
# SELECT Pr_Name, CAST(Requested_Date AS DATE) as Req_Date
# FROM [Cadworx_Request].[dbo].[tblReqFitting]
# UNION ALL
# SELECT Pr_Name, CAST(Requested_Date AS DATE) as Req_Date
# FROM [Cadworx_Request].[dbo].[tblReqComponent]
# UNION ALL
# SELECT Pr_Name, CAST(Requested_Date AS DATE) as Req_Date
# FROM [Cadworx_Request].[dbo].[tblReqEquipment]
# )SubQry

# WHERE Pr_Name = 'Bluejay'

# GROUP BY Req_Date
# ORDER BY Req_Date"""
sql = """SELECT Req_Date, COUNT(Req_Date) as Cnt FROM
(
SELECT Pr_Name, Requested_Date as Req_Date
FROM [Cadworx_Request].[dbo].[tblReqFitting]
UNION ALL
SELECT Pr_Name, Requested_Date as Req_Date
FROM [Cadworx_Request].[dbo].[tblReqComponent]
UNION ALL
SELECT Pr_Name, Requested_Date as Req_Date
FROM [Cadworx_Request].[dbo].[tblReqEquipment]
)SubQry

WHERE Pr_Name = 'Bluejay'

GROUP BY Req_Date
ORDER BY Req_Date"""

df = pd.read_sql_query(sql, engine)
df

df.set_index('Req_Date', inplace=True)
df_weekly = df.resample('W').sum().reset_index()
df_weekly

x = df_weekly.index
y = df_weekly['Cnt']
z = np.polyfit(x, y, 2) # how to add trendline
p = np.poly1d(z)
plt.figure(figsize=(10,5))
plt.scatter(df_weekly.index,df_weekly['Cnt'])
plt.plot(x,p(x),"r--")
plt.savefig('C:/Users/tbieleni/Documents/plots/ProjectPerWeekTline.png')
# plt.scatter(df_weekly.index,df_weekly['Cnt'])
# plt.xticks(df_weekly['Req_Date'])
# plt.legend(df['Pr_Name'], loc='upper right')




# plt.bar(df['Req_Office'], df['Req_No'], align = 'center')
# plt.title('Bluejay: Overall Number of Requests per Office')
# plt.xlabel('Requester Office')
# plt.ylabel('Number of Requests')

# plt.figure(figsize=(5,24))
# plt.barh(dfU['Requested_By'], dfU['Req_No'], align = 'center')
# plt.title('Bluejay: Overall Number of Requests per User')
# plt.xlabel('Requester login')
# plt.ylabel('Number of Requests')
# plt.yticks(fontsize=8)
# plt.savefig('C:/Users/tbieleni/Documents/Users.png')
