/****** Script for SelectTopNRows command from SSMS  ******/
SELECT Equipment.ID_Num
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
  ORDER BY Requested_Date