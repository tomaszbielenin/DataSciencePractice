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
SELECT Pr_Name, CAST(Requested_Date AS DATE) as Req_Date
FROM [Cadworx_Request].[dbo].[tblReqFitting]
UNION ALL
SELECT Pr_Name, CAST(Requested_Date AS DATE) as Req_Date
FROM [Cadworx_Request].[dbo].[tblReqComponent]
UNION ALL
SELECT Pr_Name, CAST(Requested_Date AS DATE) as Req_Date
FROM [Cadworx_Request].[dbo].[tblReqEquipment]
)SubQry

WHERE Pr_Name = 'Bluejay'

Group by Req_Date
ORDER BY Req_Date"""

df = pd.read_sql_query(sql, engine)
df
# Ten blok powinien sumować requesty na tydzień

# df['Req_Date'] = pd.to_datetime(df['Req_Date']) - pd.to_timedelta(7, unit='d')
# df = df.groupby(['Pr_Name', pd.Grouper(key='Req_Date', freq='W-MON')])['Cnt']
#        .sum()
#        .reset_index()
#        .sort_values('Req_Date')
# print(df)

plt.figure(figsize=(10,5))
# plt.xticks(np.arange(1,230,1))
plt.plot_date(pd.to_datetime(df['Req_Date']),df['Cnt'])
plt.savefig('C:/Users/tbieleni/Documents/plots/ProjectPerDay.png')

plt.yticks(np.arange(0,2200,50))
plt.xticks(np.arange(-1,6,1))
plt.tick_params(bottom=False, labelbottom=False)
plt.legend(df['Pr_Name'], loc='upper right')
plt.savefig('C:/Users/tbieleni/Documents/plots/ProjectPerDay.png')



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
