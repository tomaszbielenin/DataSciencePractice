/****** Script for SelectTopNRows command from SSMS  ******/
SELECT Pr_Name, Requested_By, Request_Status, Comments
  FROM [Cadworx_Request].[dbo].[tblReqComponent]
  WHERE Request_Status = 'Cancelled' and Pr_Name = 'Bluejay' --and Comments like '%duplicate%'