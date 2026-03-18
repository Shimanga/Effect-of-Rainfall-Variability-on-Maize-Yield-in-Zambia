SELECT *
FROM dbo.[rainfall]

--Separate months from years and arrange by season
SELECT *,
    YEAR([date]) AS year,
    MONTH([date]) AS month,
    CASE 
        WHEN MONTH([date]) >= 10 THEN YEAR([date])
        ELSE YEAR([date]) - 1
    END AS season_year
INTO dbo.[rainfall_from_oct_to_march]
FROM dbo.[rainfall]
WHERE MONTH([date]) IN (10,11,12,1,2,3);

--Confirm all months exist
--SELECT DISTINCT MONTH ([date]) AS month
--FROM dbo.[rainfall]
--ORDER BY month

ALTER TABLE dbo.[rainfall_from_oct_to_march]
ADD province NVARCHAR(50);
--Update PCODE to show province name
UPDATE dbo.[rainfall_from_oct_to_march]
SET province = CASE [PCODE]
        WHEN 'ZM101' THEN 'Western'
        WHEN 'ZM102' THEN 'Central'
        WHEN 'ZM103' THEN 'Eastern'
        WHEN 'ZM104' THEN 'Luapula'
        WHEN 'ZM105' THEN 'Northern'
        WHEN 'ZM106' THEN 'North-Western'
        WHEN 'ZM107' THEN 'Southern'
        WHEN 'ZM108' THEN 'Copperbelt'
        WHEN 'ZM109' THEN 'Lusaka'
        WHEN 'ZM110' THEN 'Muchinga'
        ELSE 'Unknown'
    END

-- Data validation for rainfall checks(rfh)
--SELECT *
--FROM dbo.[rainfall]
--WHERE rfh IS NULL

--SELECT *
--FROM dbo.[rainfall]
--WHERE rfh <0

--SELECT *
--FROM dbo.[rainfall]
--WHERE rfh >500

--Create new table and combine for adm level 1

SELECT dbo.[rainfall_from_oct_to_march].[PCODE], 
dbo.[rainfall_from_oct_to_march].[season_year],
dbo.[rainfall_from_oct_to_march].[province],
dbo.[rainfall].[adm_level],
SUM ([rainfall_from_oct_to_march].[rfh]) AS rfh_total
INTO dbo.[rainfall_admlevel1_summary]
FROM dbo.[rainfall_from_oct_to_march]
JOIN dbo.[rainfall]
ON
dbo.[rainfall_from_oct_to_march].[PCODE] = dbo.[rainfall].[PCODE]
WHERE dbo.[rainfall].[adm_level] = 1
GROUP BY
dbo.[rainfall_from_oct_to_march].[PCODE], 
dbo.[rainfall_from_oct_to_march].[season_year],
dbo.[rainfall_from_oct_to_march].[province],
dbo.[rainfall].[adm_level]

SELECT *
FROM dbo.[rainfall_admlevel1_summary]
ORDER BY season_year

