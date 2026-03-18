SELECT *
FROM dbo.[Maize_production]

--Remove the word province from region column
UPDATE dbo.[Maize_production]
SET Regions = REPLACE(Regions, ' Province','');

--Rename province and date column title
EXEC sp_rename
'dbo.Maize_production.Regions',
'province', 'COLUMN';

EXEC sp_rename
'dbo.Maize_production.date',
'year', 'COLUMN';

EXEC sp_rename
'dbo.Maize_production.Units',
'production', 'COLUMN';

--Combine rainfall and yield data to production data. Rainfall data uses oct-mar, production data= seasonal data + 1
SELECT
dbo.[rainfall_yield].[province],
dbo.[rainfall_yield].[season_year],
dbo.[rainfall_yield].[rfh_total],
dbo.[rainfall_yield].[yield],
dbo.[Maize_production].[production]
INTO dbo.[rainfall_production_yield]
FROM [rainfall_yield]
INNER JOIN dbo.[Maize_production]
ON [rainfall_yield].[province]= dbo.[Maize_production].[province]
AND [rainfall_yield].[season_year]= dbo.[Maize_production].[year]-1
ORDER BY [rainfall_yield].[province], [rainfall_yield].[season_year];

SELECT *
FROM dbo.[rainfall_production_yield]

