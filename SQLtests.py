import pandas as pd
import sqlalchemy as sa
from matplotlib import pyplot as plt

engine = sa.create_engine('mssql+pyodbc://PLKTW0-APP001/Cadworx_Request?driver=SQL+Server+Native+Client+11.0', echo=True)

sql = """SELECT *
  FROM [Cadworx_Request].[dbo].[tblProjects]"""

df = pd.read_sql_query(sql, engine)
df.head(100)

sqlFittings = """SELECT Req_Office, count(Req_Office) as Reqs 
  FROM [Cadworx_Request].[dbo].[tblReqFitting]
  where Pr_Name = 'Bluejay'
  group by Req_Office
  order by Req_Office"""

sqlSum ="""DECLARE @Project varchar(max)
SET @Project ='Bluejay'

SELECT Req_Office, Count(Req_Office) as Req_No FROM
(
SELECT Req_Office
FROM [Cadworx_Request].[dbo].[tblReqFitting]
UNION ALL
SELECT Req_Office
FROM [Cadworx_Request].[dbo].[tblReqComponent]
UNION ALL
SELECT Req_Office
FROM [Cadworx_Request].[dbo].[tblReqEquipment]
UNION ALL
SELECT Req_Office
FROM [Cadworx_Request].[dbo].[tblReqPipeSupport]
)SubQry

WHERE Req_Office IS NOT NULL

GROUP BY Req_Office"""

df = pd.read_sql_query(sqlSum, engine)
df
plt.bar(df['Req_Office'], df['Req_No'], align = 'center')
plt.title('Bluejay: Overall Number of Requests per Office')
plt.xlabel('Requester Office')
plt.ylabel('Number of Requests')

ReqUsers="""SELECT Requested_By, Count(Requested_By) as Req_No FROM
(
SELECT Requested_By
FROM [Cadworx_Request].[dbo].[tblReqFitting]
UNION ALL
SELECT Requested_By
FROM [Cadworx_Request].[dbo].[tblReqComponent]
UNION ALL
SELECT Requested_By
FROM [Cadworx_Request].[dbo].[tblReqEquipment]
UNION ALL
SELECT Requested_By
FROM [Cadworx_Request].[dbo].[tblReqPipeSupport]
)SubQry

WHERE Requested_By IS NOT NULL

GROUP BY Requested_By"""

dfU = pd.read_sql_query(ReqUsers, engine)
dfU

plt.figure(figsize=(5,24))
plt.barh(dfU['Requested_By'], dfU['Req_No'], align = 'center')
plt.title('Bluejay: Overall Number of Requests per User')
plt.xlabel('Requester login')
plt.ylabel('Number of Requests')
plt.yticks(fontsize=8)
plt.savefig('C:/Users/tbieleni/Documents/Users.png')
