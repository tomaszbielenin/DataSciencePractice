import pandas as pd
import sqlalchemy as sa
from matplotlib import pyplot as plt

engine = sa.create_engine('mssql+pyodbc://PLKTW0-APP001/Cadworx_Request?driver=SQL+Server+Native+Client+11.0', echo=True)

sql = """DECLARE @Project varchar(max)
SET @Project ='Bluejay'

SELECT Q11.Requested_By, Q11.Finished, COALESCE(Q21.Cancelled, 0) AS Cancelled FROM
(
SELECT Requested_By, Count(Requested_By) as Finished FROM
(
SELECT Requested_By, Request_Status
FROM [Cadworx_Request].[dbo].[tblReqFitting]
WHERE Pr_Name = @Project AND Request_Status = 'Finished'
UNION ALL
SELECT Requested_By, Request_Status
FROM [Cadworx_Request].[dbo].[tblReqComponent]
WHERE Pr_Name = @Project AND Request_Status = 'Finished'
UNION ALL
SELECT Requested_By, Request_Status
FROM [Cadworx_Request].[dbo].[tblReqEquipment]
WHERE Pr_Name = @Project AND Request_Status = 'Finished'
UNION ALL
SELECT Requested_By, Request_Status
FROM [Cadworx_Request].[dbo].[tblReqPipeSupport]
WHERE Pr_Name = @Project AND Request_Status = 'Finished'
)Q1

WHERE Requested_By IS NOT NULL

GROUP BY Requested_By)Q11

LEFT JOIN

(
SELECT Requested_By, Count(Requested_By) as Cancelled FROM
(
SELECT Requested_By
FROM [Cadworx_Request].[dbo].[tblReqFitting]
WHERE Pr_Name = @Project AND Request_Status = 'Cancelled'
UNION ALL
SELECT Requested_By
FROM [Cadworx_Request].[dbo].[tblReqComponent]
WHERE Pr_Name = @Project AND Request_Status = 'Cancelled'
UNION ALL
SELECT Requested_By
FROM [Cadworx_Request].[dbo].[tblReqEquipment]
WHERE Pr_Name = @Project AND Request_Status = 'Cancelled'
UNION ALL
SELECT Requested_By
FROM [Cadworx_Request].[dbo].[tblReqPipeSupport]
WHERE Pr_Name = @Project AND Request_Status = 'Cancelled'
)Q2

WHERE Requested_By IS NOT NULL

GROUP BY Requested_By)Q21

ON Q11.Requested_By = Q21.Requested_By"""

df = pd.read_sql_query(sql, engine)
df.head()

ind = np.arange(len(df))
width = 0.04

fig, ax = plt.subplots()
ax.barh(df['Requested_By'], df['Finished'], width, color='red', label='Finished')
ax.barh(df['Requested_By'] + width, df['Cancelled'], width, color='green', label='Cancelled')
plt.show()
ax.set(yticks=ind + width, yticklabels=df.graph, ylim=[2*width - 1, len(df)])
ax.legend()

plt.show()

plt.figure(figsize=(5,24))
plt.barh(dfU['Requested_By'], dfU['Req_No'], align = 'center')
plt.title('Bluejay: Overall Number of Requests per User')
plt.xlabel('Requester login')
plt.ylabel('Number of Requests')
plt.yticks(fontsize=8)
plt.savefig('C:/Users/tbieleni/Documents/Users.png')