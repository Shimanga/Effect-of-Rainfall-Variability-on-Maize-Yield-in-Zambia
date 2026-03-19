
<h1>Rainfall Variability and Its Effect on Maize Yield in Zambia (1986–2013)</h1>

A data analysis project investigating how rainfall affects maize yield across Zambian provinces from 1986-2013

Critical Data Notes

Issue Description Handling
Muchinga Province Created in 2011 from Northern province; only has data for 2011-2013 Excluded from Python time-series analysis; included in Tableau
2008-2010 Data Gap No yield data available from ZamStats for these years Rows removed from analysis; 24 years remain (1986-2007, 2011-2013)
Rainfall Scale Original values were 1000x too large (1.5M instead of 1500mm) Divided by 1000 in data cleaning
Data Structure One row per province-year combination Clean, no duplicates

Final Analysis Dataset:

· 9 provinces (excluding Muchinga)
· 24 years per province (1986-2007, 2011-2013)
· 432 total observations
· Rainfall range: 700-2500mm per season
· Yield range: 0.19-3.58 t/ha

---

Key Findings

1. The Rainfall Threshold

Is there an optimal rainfall range for maize production?

Once rainfall exceeds 700-800mm per season, additional rain provides minimal yield benefit. Zambia's provinces generally receive adequate rainfall (700-2500mm), meaning total rainfall is not the limiting factor in most years.

Rainfall Range Observations Average Yield Note
<800mm 4 1.48 t/ha Below optimal
800-1000mm 45 1.70 t/ha Good
1000-1200mm 115 1.76 t/ha Optimal
1200-1400mm 108 1.80 t/ha Optimal
1400-1600mm 68 1.75 t/ha Plateau
1600mm+ 62 1.71 t/ha Plateau

Insight: The optimal range is 1000-1400mm. Above 1400mm, yields do not increase.

2. Provincial Efficiency

Which provinces use rainfall most effectively?

Province Avg Yield (t/ha) Avg Rainfall (mm) Efficiency (t/ha per 100mm)
Central 2.33 1828 0.13
Southern 1.49 1810 0.08
Northern 1.93 1195 0.16

Key Insight: Northern province is most efficient (0.16 t/ha per 100mm rain). Southern province is least efficient despite similar rainfall to Central. This suggests soil quality, management practices, and seed varieties matter more than total rainfall once minimum thresholds are met.

3. Low-Rainfall Vulnerability

Which provinces are most affected when rainfall is below normal?

Using the bottom 25th percentile as the threshold for "low rainfall years" (≤1150mm):

Province Low-Rainfall Years % of Years
Western 11 46%
Lusaka 10 42%
Southern 9 38%
Central 5 21%
Northern 0 0%

Key Insight: Western, Lusaka, and Southern provinces are most vulnerable to low rainfall. Northern province never experiences low rainfall years by this definition.

4. Yield in Extreme Years

Category Average Yield Difference from Normal
Low rainfall years (≤1150mm) 1.66 t/ha -6%
Normal years (1150-1600mm) 1.76 t/ha baseline
High rainfall years (≥1600mm) 1.76 t/ha 0%

Key Insight: Low rainfall years reduce yields by only 6% on average. This confirms that even "low" rainfall in Zambia (by historical standards) is usually adequate for maize production.

5. Regression Analysis

How much of yield variation does rainfall explain?

· R² = 0.019 (rainfall explains only 1.9% of yield variation)
· This is not a problem with the analysis—it's the key finding

Interpretation: Once a province receives adequate rainfall (which most do, most years), other factors determine yield outcomes. The 98% unexplained variation comes from:

· Soil fertility differences
· Seed varieties used
· Farming practices and technology
· Timing of rainfall within the season
· Pest and disease pressure
· Access to inputs (fertilizer, etc.)

---

1. Rainfall is not the problem: Almost all Zambian provinces receive enough rain (700-2500mm) for maize production in most years.
2. Efficiency varies dramatically: Northern province produces twice as much maize per drop of rain as Southern province, despite similar total rainfall.
3. The real leverage points: With only 2% of yield variation explained by total rainfall, efforts to improve yields should focus on soil health, improved seeds, and better farming practices—not hoping for more rain.

---

Data Limitations

Limitation Impact
No 2008-2010 yield data 3 years missing from all provinces
Muchinga only 2011-2013 Excluded from time-series analysis
Rainfall is seasonal total only Cannot assess timing or distribution within season
No soil or management data Cannot explain the 98% unexplained variation

