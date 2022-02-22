USE KinetEcoDW;
GO

ALTER INDEX IX_CS_FactOrders
   ON Fact.Orders
   REBUILD WITH (ONLINE = ON);