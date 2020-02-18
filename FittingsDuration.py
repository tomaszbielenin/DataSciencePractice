import pandas as pd
import numpy as np
import sqlalchemy as sa
from matplotlib import pyplot as plt

engine = sa.create_engine('mssql+pyodbc://PLKTW0-APP001/Cadworx_Request?driver=SQL+Server+Native+Client+11.0', echo=True)

###Fittings

sql = """SELECT Fittings.ID_Num
, Fittings.Requested_Date
, AuditTrail.FinishedDate
, DATEDIFF(d, Fittings.Requested_Date, AuditTrail.FinishedDate) as Duration
FROM
	(SELECT [ID_Num]
      ,[Requested_Date]
  FROM [Cadworx_Request].[dbo].[tblReqFitting])Fittings

  RIGHT JOIN

	(SELECT A.RecordID, A.NewValue, B.FinishedDate from 
		(SELECT DISTINCT
      [FormName]
      ,[RecordID]
      ,[FieldName]
      ,[NewValue]
  FROM [Cadworx_Request].[dbo].[tblAuditTrail]
  where FormName like '%Fitting%' and FieldName = 'Request_Status' and NewValue = 'Finished')A

  LEFT JOIN 

		(SELECT RecordID, MAX(DateTime) AS FinishedDate from[Cadworx_Request].[dbo].[tblAuditTrail]
  where FormName like '%Fitting%' and FieldName = 'Request_Status' and NewValue = 'Finished'
  group by RecordID)B
  on A.RecordID = B.RecordID)AuditTrail
  on AuditTrail.RecordID = Fittings.ID_Num
  ORDER BY Requested_Date"""

df = pd.read_sql_query(sql, engine)
df

x = df.index
y = df['Duration']
y_mean=[df['Duration'].mean()]*len(df.index)
y_median=[df['Duration'].median()]*len(df.index)
z = np.polyfit(x, y, 2) # how to add trendline
p = np.poly1d(z)
plt.figure(figsize=(20,20))
p0 = plt.scatter(df.index,df['Duration'],s=5,color='purple')
p1 = plt.plot(x,p(x),"--",color='orange')
p2 = plt.plot(x,y_mean,"--",color='red')
# plt.plot(x,y_median,"--",color='deeppink')
plt.title('Fittings: Request Duration')
plt.xlabel('Reqests sorted by date')
plt.ylabel('Duriation [Days]')
plt.yticks(np.arange(0,130,10))
plt.legend((p0,p1[0],p2[0]), ('Duration', 'Trend', ('Mean: '+str(round(df['Duration'].mean(),2)))))
plt.savefig('C:/Users/tbieleni/Documents/plots/FittingsDuration.png')

###Components

sql = """SELECT Component.ID_Num
, Component.Requested_Date
, AuditTrail.FinishedDate
, DATEDIFF(d, Component.Requested_Date, AuditTrail.FinishedDate) as Duration
FROM
	(SELECT [ID_Num]
      ,[Requested_Date]
  FROM [Cadworx_Request].[dbo].[tblReqComponent])Component

  RIGHT JOIN

	(SELECT A.RecordID, A.NewValue, B.FinishedDate from 
		(SELECT DISTINCT
      [FormName]
      ,[RecordID]
      ,[FieldName]
      ,[NewValue]
  FROM [Cadworx_Request].[dbo].[tblAuditTrail]
  where FormName like '%Component%' and FieldName = 'Request_Status' and NewValue = 'Finished')A

  LEFT JOIN 

		(SELECT RecordID, MAX(DateTime) AS FinishedDate from[Cadworx_Request].[dbo].[tblAuditTrail]
  where FormName like '%Component%' and FieldName = 'Request_Status' and NewValue = 'Finished'
  group by RecordID)B
  on A.RecordID = B.RecordID)AuditTrail
  on AuditTrail.RecordID = Component.ID_Num
  ORDER BY Requested_Date"""

df = pd.read_sql_query(sql, engine)
df

x = df.index
y = df['Duration']
y_mean=[df['Duration'].mean()]*len(df.index)
y_median=[df['Duration'].median()]*len(df.index)
z = np.polyfit(x, y, 2) # how to add trendline
p = np.poly1d(z)
plt.figure(figsize=(20,20))
p0 = plt.scatter(df.index,df['Duration'],s=5,color='purple')
p1 = plt.plot(x,p(x),"--",color='orange')
p2 = plt.plot(x,y_mean,"--",color='red')
# plt.plot(x,y_median,"--",color='deeppink')
plt.title('Components: Request Duration')
plt.xlabel('Reqests sorted by date')
plt.ylabel('Duriation [Days]')
plt.yticks(np.arange(0,130,10))
plt.legend((p0,p1[0],p2[0]), ('Duration', 'Trend', ('Mean: '+str(round(df['Duration'].mean(),2)))))
plt.savefig('C:/Users/tbieleni/Documents/plots/ComponentsDuration.png')

###Equipment

sql = """SELECT Equipment.ID_Num
, Equipment.Requested_Date
, AuditTrail.FinishedDate
, DATEDIFF(d, Equipment.Requested_Date, AuditTrail.FinishedDate) as Duration
FROM
	(SELECT [ID_Num]
      ,[Requested_Date]
  FROM [Cadworx_Request].[dbo].[tblReqEquipment])Equipment

  RIGHT JOIN

	(SELECT A.RecordID, A.NewValue, B.FinishedDate from 
		(SELECT DISTINCT
      [FormName]
      ,[RecordID]
      ,[FieldName]
      ,[NewValue]
  FROM [Cadworx_Request].[dbo].[tblAuditTrail]
  where FormName like '%Equipment%' and FieldName = 'Request_Status' and NewValue = 'Finished')A

  LEFT JOIN 

		(SELECT RecordID, MAX(DateTime) AS FinishedDate from[Cadworx_Request].[dbo].[tblAuditTrail]
  where FormName like '%Equipment%' and FieldName = 'Request_Status' and NewValue = 'Finished'
  group by RecordID)B
  on A.RecordID = B.RecordID)AuditTrail
  on AuditTrail.RecordID = Equipment.ID_Num
  ORDER BY Requested_Date"""

df = pd.read_sql_query(sql, engine)
df
# df['Duration'].mean()
# df['Duration'].median()

x = df.index
y = df['Duration']
y_mean=[df['Duration'].mean()]*len(df.index)
y_median=[df['Duration'].median()]*len(df.index)
z = np.polyfit(x, y, 2) # how to add trendline
p = np.poly1d(z)
plt.figure(figsize=(20,20))
p0 = plt.scatter(df.index,df['Duration'],s=5,color='purple')
p1 = plt.plot(x,p(x),"--",color='orange')
p2 = plt.plot(x,y_mean,"--",color='red')
# plt.plot(x,y_median,"--",color='deeppink')
plt.title('Equipment: Request Duration')
plt.xlabel('Reqests sorted by date')
plt.ylabel('Duriation [Days]')
plt.yticks(np.arange(0,130,10))
plt.legend((p0,p1[0],p2[0]), ('Duration', 'Trend', ('Mean: '+str(round(df['Duration'].mean(),2)))))
plt.savefig('C:/Users/tbieleni/Documents/plots/EquipmentDuration.png')

# plt.annotate('str(df['Duration'].mean()),(400,10))