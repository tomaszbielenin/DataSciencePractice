import pandas as pd
import numpy as np
import sqlalchemy as sa
from matplotlib import pyplot as plt

engine = sa.create_engine('mssql+pyodbc://PLKTW0-APP001/Cadworx_Request?driver=SQL+Server+Native+Client+11.0', echo=True)

sql = """SELECT Pr_Name, Count(Pr_Name) as Req_No FROM
(
SELECT Pr_Name
FROM [Cadworx_Request].[dbo].[tblReqFitting]
UNION ALL
SELECT Pr_Name
FROM [Cadworx_Request].[dbo].[tblReqComponent]
UNION ALL
SELECT Pr_Name
FROM [Cadworx_Request].[dbo].[tblReqEquipment]
UNION ALL
SELECT Pr_Name
FROM [Cadworx_Request].[dbo].[tblReqPipeSupport]
)SubQry

WHERE Pr_Name != 'Pendleton'

GROUP BY Pr_Name
ORDER BY Req_No DESC"""

df = pd.read_sql_query(sql, engine)
df

N = 1
ind = np.arange(N)
plt.figure(figsize=(4,10))
p0 = plt.bar(ind, df['Req_No'][0], color = 'saddlebrown')
p1 = plt.bar(ind, df['Req_No'][1], bottom = df['Req_No'][0], color = 'peru')
p2 = plt.bar(ind, df['Req_No'][2], bottom = df['Req_No'][0]+df['Req_No'][1], color = 'chocolate')
p3 = plt.bar(ind, df['Req_No'][3], bottom = df['Req_No'][0]+df['Req_No'][1]+df['Req_No'][2], color = 'sandybrown')
p4 = plt.bar(ind, df['Req_No'][4], bottom = df['Req_No'][0]+df['Req_No'][1]+df['Req_No'][2]+df['Req_No'][3], color = 'peachpuff')
p5 = plt.bar(ind, df['Req_No'][5], bottom = df['Req_No'][0]+df['Req_No'][1]+df['Req_No'][2]+df['Req_No'][3]+df['Req_No'][4], color = 'sienna')
plt.yticks(np.arange(0,2200,50))
plt.xticks(np.arange(-1,6,1))
plt.tick_params(bottom=False, labelbottom=False)
plt.legend(df['Pr_Name'], loc='upper right')
plt.savefig('C:/Users/tbieleni/Documents/plots/overallPerProject.png')



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
