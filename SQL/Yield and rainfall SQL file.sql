SELECT *
FROM dbo.[Maize_yield]

--Remove the word province from region column
UPDATE dbo.[Maize_yield]
SET Regions = REPLACE(Regions, ' Province','');

--Rename province  and date column title
EXEC sp_rename
'dbo.Maize_yield.Regions',
'province', 'COLUMN';

EXEC sp_rename
'dbo.Maize_yield.date',
'year', 'COLUMN';

--Combine rainfall to yield data. Rainfall data uses oct-mar, yield data= seasonal data + 1
SELECT
dbo.[rainfall_admlevel1_summary].[province],
dbo.[rainfall_admlevel1_summary].[season_year],
dbo.[rainfall_admlevel1_summary].[rfh_total],
dbo.[Maize_yield].[yield]
INTO dbo.[rainfall_yield]
FROM dbo.[rainfall_admlevel1_summary]
INNER JOIN dbo.[Maize_yield]
ON [rainfall_admlevel1_summary].[province]= dbo.[Maize_yield].[province]
AND [rainfall_admlevel1_summary].[season_year]= dbo.[Maize_yield].[year]-1
ORDER BY [rainfall_admlevel1_summary].[province], [rainfall_admlevel1_summary].[season_year];

SELECT *
FROM dbo.[rainfall_yield]

