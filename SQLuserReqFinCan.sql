/****** Script for SelectTopNRows command from SSMS  ******/


DECLARE @Project varchar(max)
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

ON Q11.Requested_By = Q21.Requested_By