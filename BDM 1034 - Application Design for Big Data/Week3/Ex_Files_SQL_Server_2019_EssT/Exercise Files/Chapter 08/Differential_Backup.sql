USE LandonHotel;
GO

INSERT INTO Guests (FirstName, LastName, Address, City, State, PostalCode, Country)
	VALUES ('Emily','Hayes','9 South Crossing','Cleveland','OH','44101','United States'),
		('Dennis','Bishop','33 Victoria Circle','El Paso','TX','79821','United States'),
		('Frank','Rogers','9 Tomscot Place','Dallas','TX','75001','United States'),
		('Dorothy','Tucker','7715 Havey Center','Los Angeles','CA','90001','United States'),
		('Steven','Jenkins','772 Eagle Crest Court','Seattle','WA','98101','United States')
;

SELECT *
FROM Guests;
