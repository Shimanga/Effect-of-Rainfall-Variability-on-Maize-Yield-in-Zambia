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
    dbo.[seasonal_rainfall_totals].province,
    dbo.[seasonal_rainfall_totals].season_year,
    dbo.[seasonal_rainfall_totals].seasonal_total_mm,
    dbo.[Maize_yield].yield
INTO dbo.[final_rainfall_yield]
FROM dbo.[seasonal_rainfall_totals]
INNER JOIN dbo.[Maize_yield]
    ON dbo.[seasonal_rainfall_totals].province = dbo.[Maize_yield].province
    AND dbo.[seasonal_rainfall_totals].season_year = dbo.[Maize_yield].year-1
ORDER BY dbo.[seasonal_rainfall_totals].province, 
         dbo.[seasonal_rainfall_totals].season_year;
SELECT *
FROM dbo.[final_rainfall_yield]

