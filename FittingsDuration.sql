/****** Script for SelectTopNRows command from SSMS  ******/
SELECT Fittings.ID_Num
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
  ORDER BY Duration