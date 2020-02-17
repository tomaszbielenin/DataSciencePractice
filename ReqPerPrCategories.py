import pandas as pd
import numpy as np
import sqlalchemy as sa
from matplotlib import pyplot as plt

engine = sa.create_engine('mssql+pyodbc://PLKTW0-APP001/Cadworx_Request?driver=SQL+Server+Native+Client+11.0', echo=True)

sql = """SELECT Pr_Name, [TableName], Count([TableName]) as 'ReqCnt' FROM
(
SELECT Pr_Name, 'Fittings' AS [TableName]
FROM [Cadworx_Request].[dbo].[tblReqFitting]
UNION ALL
SELECT Pr_Name, 'Component' AS [TableName]
FROM [Cadworx_Request].[dbo].[tblReqComponent]
UNION ALL
SELECT Pr_Name, 'Equipment' AS [TableName]
FROM [Cadworx_Request].[dbo].[tblReqEquipment]
UNION ALL
SELECT Pr_Name, 'PipeSupport' AS [TableName]
FROM [Cadworx_Request].[dbo].[tblReqPipeSupport]
)SubQry

WHERE Pr_Name != 'Pendleton'

GROUP BY Pr_Name, [TableName]
ORDER BY Pr_Name, [TableName]"""

df = pd.read_sql_query(sql, engine)
df

Component = df['ReqCnt'].loc[df['TableName'] == 'Component'].tolist()
Equipment = df['ReqCnt'].loc[df['TableName'] == 'Equipment'].tolist() #append 0 for missing records manually
Fittings = df['ReqCnt'].loc[df['TableName'] == 'Fittings'].tolist()
PipeSupport = df['ReqCnt'].loc[df['TableName'] == 'PipeSupport'].tolist() #append 0 for missing records manually

N = 6
ind = np.arange(N)
plt.figure(figsize=(10,10))
p0 = plt.bar(ind, Component)
p1 = plt.bar(ind, Equipment, bottom = np.array(Component))
p2 = plt.bar(ind, Fittings, bottom = np.array(Component)+np.array(Equipment)) #, color = 'chocolate')
p3 = plt.bar(ind, PipeSupport, bottom = np.array(Component)+np.array(Equipment)+np.array(Fittings)) #, color = 'sandybrown')
plt.xticks(ind, ('Bluejay', 'Blueridge', 'Joseph', 'OCOC', 'OOC', 'ST Agrate'))
plt.legend((p0[0], p1[0],p2[0],p3[0]), ('Component', 'Equipment', 'Fittings', 'PipeSupport'), loc='upper right')
plt.savefig('C:/Users/tbieleni/Documents/plots/ReqPerPrCategories.png')

########

sql = """SELECT Pr_Name, Request_Status, COUNT(Request_Status)  as 'ReqCnt'
FROM [Cadworx_Request].[dbo].[tblReqFitting]


WHERE Pr_Name != 'Pendleton'

GROUP BY Pr_Name, Request_Status
ORDER BY Pr_Name"""

df = pd.read_sql_query(sql, engine)
df

Finished = df['ReqCnt'].loc[df['Request_Status'] == 'Finished'].tolist()
Cancelled = df['ReqCnt'].loc[df['Request_Status'] == 'Cancelled'].tolist() 
Hold = df['ReqCnt'].loc[df['Request_Status'] == 'On hold'].tolist() #append 0 for missing records manually

N = 6
ind = np.arange(N)
plt.figure(figsize=(10,10))
p0 = plt.bar(ind, Finished, color='green')
p1 = plt.bar(ind, Cancelled, bottom = np.array(Finished), color='orange')
p2 = plt.bar(ind, Hold, bottom = np.array(Finished)+np.array(Cancelled), color='royalblue')
plt.title('Fittings Requests per Status')
plt.xticks(ind, ('Bluejay', 'Blueridge', 'Joseph', 'OCOC', 'OOC', 'ST Agrate'))
plt.legend((p0[0],p1[0],p2[0]), ('Finished', 'Cancelled', 'On hold'), loc='upper right')
plt.savefig('C:/Users/tbieleni/Documents/plots/FittingsRequestStatus.png')

########

sql = """SELECT Pr_Name, Request_Status, COUNT(Request_Status)  as 'ReqCnt'
FROM [Cadworx_Request].[dbo].[tblReqComponent]


WHERE Pr_Name != 'Pendleton'

GROUP BY Pr_Name, Request_Status
ORDER BY Pr_Name"""

df = pd.read_sql_query(sql, engine)
df

Finished = df['ReqCnt'].loc[df['Request_Status'] == 'Finished'].tolist()
Cancelled = df['ReqCnt'].loc[df['Request_Status'] == 'Cancelled'].tolist() #append 0 for missing records manually
Hold = df['ReqCnt'].loc[df['Request_Status'] == 'On hold'].tolist()

N = 6
ind = np.arange(N)
plt.figure(figsize=(10,10))
p0 = plt.bar(ind, Finished, color='green')
p1 = plt.bar(ind, Cancelled, bottom = np.array(Finished), color='orange')
p2 = plt.bar(ind, Hold, bottom = np.array(Finished)+np.array(Cancelled), color='royalblue')
plt.title('Components Requests per Status')
plt.xticks(ind, ('Bluejay', 'Blueridge', 'Joseph', 'OCOC', 'OOC', 'ST Agrate'))
plt.legend((p0[0],p1[0],p2[0]), ('Finished', 'Cancelled', 'On hold'), loc='upper right')
plt.savefig('C:/Users/tbieleni/Documents/plots/ComponentsRequestStatus.png')

########

sql = """SELECT Pr_Name, Request_Status, COUNT(Request_Status)  as 'ReqCnt'
FROM [Cadworx_Request].[dbo].[tblReqEquipment]


WHERE Pr_Name != 'Pendleton'

GROUP BY Pr_Name, Request_Status
ORDER BY Pr_Name"""

df = pd.read_sql_query(sql, engine)
df

Finished = df['ReqCnt'].loc[df['Request_Status'] == 'Finished'].tolist()
Cancelled = df['ReqCnt'].loc[df['Request_Status'] == 'Cancelled'].tolist()
Hold = df['ReqCnt'].loc[df['Request_Status'] == 'On hold'].tolist() #append 0 for missing records manually
#Finished,Cancelled,Hold

N = 5
ind = np.arange(N)
plt.figure(figsize=(10,10))
p0 = plt.bar(ind, Finished, color='green')
p1 = plt.bar(ind, Cancelled, bottom = np.array(Finished), color='orange')
p2 = plt.bar(ind, Hold, bottom = np.array(Finished)+np.array(Cancelled), color='royalblue')
plt.title('Equipment Requests per Status')
plt.xticks(ind, ('Bluejay', 'Blueridge', 'Joseph', 'OCOC', 'OOC', 'ST Agrate'))
plt.legend((p0[0],p1[0],p2[0]), ('Finished', 'Cancelled', 'On hold'), loc='upper right')
plt.savefig('C:/Users/tbieleni/Documents/plots/EquipmentRequestStatus.png')

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
