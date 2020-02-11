/****** Script for SelectTopNRows command from SSMS  ******/
DECLARE @Project varchar(max)
SET @Project ='Bluejay'


SELECT Requested_By, COUNT(Requested_By) as Req_Cancelled FROM
(
SELECT Requested_By, Request_Status
FROM [Cadworx_Request].[dbo].[tblReqFitting]
WHERE Pr_Name = @Project AND Request_Status = 'Cancelled'
UNION ALL
SELECT Requested_By, Request_Status
FROM [Cadworx_Request].[dbo].[tblReqComponent]
WHERE Pr_Name = @Project AND Request_Status = 'Cancelled'
UNION ALL
SELECT Requested_By, Request_Status
FROM [Cadworx_Request].[dbo].[tblReqEquipment]
WHERE Pr_Name = @Project AND Request_Status = 'Cancelled'
UNION ALL
SELECT Requested_By, Request_Status
FROM [Cadworx_Request].[dbo].[tblReqPipeSupport]
WHERE Pr_Name = @Project AND Request_Status = 'Cancelled'
)SubQry
WHERE Requested_By IS NOT NULL
GROUP BY Requested_By