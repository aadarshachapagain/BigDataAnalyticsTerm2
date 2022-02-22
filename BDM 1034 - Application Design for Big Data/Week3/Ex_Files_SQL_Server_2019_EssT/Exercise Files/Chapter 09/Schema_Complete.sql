USE LandonHotel;
GO

-- create a new schema in the database
CREATE SCHEMA HumanResources;
GO


-- move an existing table into the new schema
ALTER SCHEMA HumanResources TRANSFER dbo.Employees;
GO


-- elevate Marcus' permissions within the schema 
GRANT INSERT ON SCHEMA :: HumanResources TO Marcus;  -- can also GRANT UPDATE or GRANT DELETE
GO