USE LandonHotel;
GO

-- view the data
SELECT * FROM HumanResources.Employees;
GO

-- add data masking to the Email field
ALTER TABLE HumanResources.Employees
ALTER COLUMN Email ADD MASKED WITH (Function = 'email()');
								-- (Function = 'default()');
								-- (Function = 'random([start range], [end range])');
								-- (Function = 'partial(prefix, [padding], suffix)');
								-- (Function = 'partial(2, "-----", 1)');

-- view the data again
SELECT * FROM HumanResources.Employees;
GO

-- remove data masking from email column
ALTER TABLE HumanResources.Employees
ALTER COLUMN Email DROP MASKED;

