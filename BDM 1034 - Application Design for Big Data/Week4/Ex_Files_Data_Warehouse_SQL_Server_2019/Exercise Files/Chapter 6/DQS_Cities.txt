USE KinetEcoDW
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [Dimension].[DQS_Cities](
    [City] [nvarchar](50) NOT NULL,
    [State] [nvarchar](50) NOT NULL,
    [Country] [nvarchar](60) NOT NULL,
    [Sales Territory] [nvarchar](50) NOT NULL,
    [Latest Recorded Population] [bigint] NOT NULL
)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'New York', N'New York', N'United States', N'Mideast', 8175133)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Chicago', N'Illinois', N'United States', N'Great Lakes', 2695598)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Queens', N'New York', N'United States', N'Mideast', 2272771)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Manhattan', N'New York', N'United States', N'Mideast', 1619090)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Phoenix', N'Arizona', N'United States', N'Southwest', 1445632)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'SanAntonio', N'Texas', N'United States', N'Southwest', 1327407)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Dallas', N'Texas', N'United States', N'Southwest', 1197816)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Jacksonville', N'Florida', N'United States', N'Southeast', 821784)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'San Francisco', N'California', N'United States', N'Far West', 805235)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Columbus', N'Ohio', N'United States', N'Great Lakes', 787033)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Charlotte', N'North Carolin', N'United States', N'Southeast', 731424)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'El Paso', N'Texas', N'United States', N'Southwest', 649121)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Baltimore', N'Maryland', N'United States', N'Mideast', 620961)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Seattle', N'Washington', N'United States', N'Far West', 608660)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Nashville', N'Tennessee', N'United States', N'Southeast', 601222)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Louisville', N'Kentucky', N'United States', N'Southeast', 597337)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Portland', N'Oregano', N'United States', N'Far West', 583776)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Oklahoma City', N'Oklahoma', N'United States', N'Southwest', 579999)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Tucson', N'Arizona', N'United States', N'Southwest', 520116)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Staten Island', N'New York', N'United States', N'Mideast', 470728)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Long Beach', N'Califronia', N'United States', N'Far West', 462257)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Mesa', N'Arizona', N'United States', N'Southwest', 439041)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Atlanta', N'Georgia', N'United States', N'Southeast', 420003)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Omaha', N'Nebraska', N'United States', N'Plains', 408958)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Miami', N'Florida', N'United States', N'Southeast', 399457)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Tulsa', N'Oklahoma', N'United States', N'Southwest', 391906)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Minneapolis', N'Minnesota', N'United States', N'Plains', 382578)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Arlington', N'Texas', N'United States', N'Southwest', 365438)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'New Orleans', N'Louisiana', N'United States', N'Southeast', 343829)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Tampa', N'Florida', N'United States', N'Southeast', 335709)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Santa Ana', N'California', N'United States', N'Far West', 324528)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Pittsburgh', N'Pennsylvania', N'United States', N'Mideast', 305704)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Riverside', N'California', N'United States', N'Far West', 303871)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Lexington', N'Kentucky', N'United States', N'Southeast', 295803)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Stockton', N'California', N'United States', N'Far West', 291707)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Saint Paul', N'Minnesota', N'United States', N'Plains', 285068)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Greensboro', N'North Carolina', N'United States', N'Southeast', 269666)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Plano', N'Texas', N'United States', N'Southwest', 259841)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Henderson', N'Nevada', N'United States', N'Far West', 257729)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Jersey City', N'New Jersey', N'United States', N'Mideast', 247597)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Chula Vista', N'California', N'United States', N'Far West', 243916)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Orlando', N'Florida', N'United States', N'Southeast', 238300)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Laredo', N'Texas', N'United States', N'Southwest', 236091)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Winston-Salem', N'North Carolina', N'United States', N'Southeast', 229617)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Baton Rouge', N'Louisiana', N'United States', N'Southeast', 229493)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Garland', N'Texas', N'United States', N'Southwest', 226876)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Reno', N'Nevada', N'United States', N'Far West', 225221)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Chesapeake', N'Virginia', N'United States', N'Southeast', 222209)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'North Las Vegas', N'Nevada', N'United States', N'Far West', 216961)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Fremont', N'California', N'United States', N'Far West', 214089)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Los Angeles', N'California', N'United States', N'Far West', 3792621)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Brooklyn', N'New York', N'United States', N'Mideast', 2565635)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Houston', N'Texas', N'United States', N'Southwest', 2099451)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Philadelphia', N'Pennsylvania', N'United States', N'Mideast', 1526006)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'The Bronx', N'New York', N'United States', N'Mideast', 1408473)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'San Diego', N'California', N'United States', N'Far West', 1307402)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'San Jose', N'California', N'United States', N'Far West', 945942)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Indianapolis', N'Indiana', N'United States', N'Great Lakes', 820445)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Austin', N'Texas', N'United States', N'Southwest', 790390)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Fort Worth', N'Texas', N'United States', N'Southwest', 741206)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Detroit', N'Michigan', N'United States', N'Great Lakes', 713777)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Memphis', N'Tennessee', N'United States', N'Southeast', 646889)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Boston', N'Massachusetts[E]', N'United States', N'New England', 617594)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Washington', N'District of Columbia', N'United States', N'Mideast', 601723)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Denver', N'Colorado', N'United States', N'Rocky Mountain', 600158)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Milwaukee', N'Wisconsin', N'United States', N'Great Lakes', 594833)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Las Vegas', N'Nevada', N'United States', N'Far West', 583756)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Albuquerque', N'New Mexico', N'United States', N'Southwest', 545852)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Fresno', N'California', N'United States', N'Far West', 494665)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Sacramento', N'California', N'United States', N'Far West', 466488)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Kansas City', N'Missouri', N'United States', N'Plains', 459787)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Virginia Beach', N'Virginia', N'United States', N'Southeast', 437994)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Colorado Springs', N'Colorado', N'United States', N'Rocky Mountain', 416427)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Raleigh', N'North Carolina', N'United States', N'Southeast', 403892)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Cleveland', N'Ohio', N'United States', N'Great Lakes', 396815)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Oakland', N'California', N'United States', N'Far West', 390724)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Wichita', N'Kansas', N'United States', N'Plains', 382368)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Bakersfield', N'California', N'United States', N'Far West', 347483)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Anaheim', N'California', N'United States', N'Far West', 336265)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Aurora', N'Colorado', N'United States', N'Rocky Mountain', 325078)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Saint Louis', N'Missouri', N'United States', N'Plains', 319294)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Corpus Christi', N'Texas', N'United States', N'Southwest', 305215)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Cincinnati', N'Ohio', N'United States', N'Great Lakes', 296943)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Anchorage', N'Alaska', N'United States', N'Far West', 291826)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Toledo', N'Ohio', N'United States', N'Great Lakes', 287208)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Newark', N'New Jersey', N'United States', N'Mideast', 277140)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Buffalo', N'New York', N'United States', N'Mideast', 261310)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Lincoln', N'Nebraska', N'United States', N'Plains', 258379)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Fort Wayne', N'Indiana', N'United States', N'Great Lakes', 253691)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Saint Petersburg', N'Florida', N'United States', N'Southeast', 244769)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Norfolk', N'Virginia', N'United States', N'Southeast', 242803)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Chandler', N'Arizona', N'United States', N'Southwest', 236123)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Madison', N'Wisconsin', N'United States', N'Great Lakes', 233209)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Lubbock', N'Texas', N'United States', N'Southwest', 229573)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Durham', N'North Carolina', N'United States', N'Southeast', 228330)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Glendale', N'Arizona', N'United States', N'Southwest', 226721)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Hialeah', N'Florida', N'United States', N'Southeast', 224669)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Scottsdale', N'Arizona', N'United States', N'Southwest', 217385)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Irving', N'Texas', N'United States', N'Southwest', 216290)
GO
INSERT [Dimension].[DQS_Cities] ([City], [State], [Country], [Sales Territory], [Latest Recorded Population]) VALUES (N'Irvine', N'California', N'United States', N'Far West', 212375)
GO
