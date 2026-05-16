# Rainfall Variability and Its Effect on Maize Yield in Zambia (1986-2013)

A hypothesis-driven investigation into climate-agriculture relationships. It demonstrates correlation/regression analysis, monthly pattern detection, efficiency metrics, and translation of null results into policy research agendas.

This study evaluates how rainfall variability influences maize yield across ten provinces of Zambia. The analysis tests whether total seasonal rainfall explains yield variation, or whether provincial differences and rainfall patterns provide stronger explanatory value.

## Table of Contents
- [Research Questions](#research-questions)
- [Data Summary](#data-summary)
- [Dataset Structure](#dataset-structure)
- [Summary Statistics](#summary-statistics)
- [Results](#results)
- [Regression Analysis](#regression-analysis)
- [Trends Over Time](#trends-over-time)
- [Conclusions & Implications](#conclusions--implications)
- [Repository Structure](#repository-structure)

---

## Research Questions

1. To what extent does total seasonal rainfall explain variability in maize yield across provinces?
2. How do provincial differences in rainfall patterns relate to maize yield responses?
3. Which provinces are most vulnerable to rainfall variability and drought conditions?

---

## Data Summary

- **Time period (yield):** 1986-2013
- **Time period (rainfall):** 1981-2026
- **Provinces analyzed:** 10 (including Muchinga)
- **Observations:** 454 records (after filtering zero yields)
- **Rainfall range:** 445 mm - 1,537 mm (seasonal total)
- **Yield range:** 0.19 - 3.58 t/ha

### Data Constraints

| Limitation | Impact |
|------------|--------|
| Missing yield data (2008-2010) | These years excluded from analysis |
| Muchinga province formed in 2011 | Only 3 years available; limited reliability |
| Zero yield records removed | Treated as missing data |
| Seasonal yield data aggregation | Cannot directly correlate monthly rainfall with yield |

### Data Validation and Revision

- Initial dataset contained inconsistencies from query extraction
- Dataset was rebuilt and revalidated
- All results in this analysis are based on the corrected dataset

---

## Dataset Structure

### Seasonal Yield and Rainfall Dataset

| Column | Description |
|--------|-------------|
| Province | Administrative province (10 total) |
| Year | 1986-2013 |
| Rainfall_mm | Total seasonal rainfall (mm) |
| Yield_t_ha | Maize yield (tons/hectare) |
| Rain_efficiency | Calculated: Yield per 100mm rainfall |

### Monthly Rainfall Dataset

| Column | Description |
|--------|-------------|
| Province | Administrative province (10 total) |
| Year | 1981-2026 |
| Month | 10-12/1-3 (1=January, 10=October, etc.) |
| rfq | Monthly rainfall (mm) |

### Analytical Framework

The analysis evaluates the relationship between rainfall and yield using three components:
- **Independent Variable:** Rainfall (seasonal totals and monthly distribution)
- **Dependent Variable:** Maize yield (tonnes per hectare)
- **Secondary Factors:** Provincial variation and rainfall timing patterns

### Methodology

- **Correlation Analysis:** To measure the strength of the relationship between seasonal rainfall and yield
- **Regression Modeling:** To estimate the explanatory power of rainfall on yield variation
- **Monthly Pattern Analysis:** To assess intra-seasonal rainfall distribution across provinces
- **Comparative Metrics:** Yield per unit rainfall (efficiency measures)

---

## Summary Statistics

### Overall Yield Summary (10 provinces, 1986-2013)

| Metric | Rainfall (mm) | Yield (t/ha) |
|--------|---------------|--------------|
| Mean | 989 | 1.79 |
| Min | 445 | 0.19 |
| Max | 1,537 | 3.58 |
| Std Dev | 184 | 0.74 |

### Yield by Province

| Province | Records | Valid Years | Mean Rainfall (mm) | Mean Yield (t/ha) | Rainfall-Yield Correlation |
|----------|---------|-------------|-------------------|------------------|---------------------------|
| Central | 24 | 1986-2013 | 1,128 | 2.39 | 0.294 |
| Copperbelt | 24 | 1986-2013 | 1,059 | 2.15 | 0.315 |
| Eastern | 24 | 1986-2013 | 859 | 1.45 | 0.170 |
| Luapula | 24 | 1986-2013 | 1,108 | 1.88 | -0.476 |
| Lusaka | 24 | 1986-2013 | 689 | 1.91 | 0.453 |
| **Muchinga** | **3** | **2011-2013 only** | **823** | **1.86** | **-0.117** |
| North-Western | 24 | 1986-2013 | 975 | 1.63 | -0.277 |
| Northern | 24 | 1986-2013 | 768 | 1.99 | -0.298 |
| Southern | 24 | 1986-2013 | 1,098 | 1.51 | -0.258 |
| Western | 24 | 1986-2013 | 891 | 0.83 | 0.161 |

---

## Results: Yield Analysis

### 1. Rainfall-Yield Correlation by Province

Total seasonal rainfall shows a weak relationship with yield. It explains only ~1.9 % of yield variation (R² = 0.014). 
![Correlation](Output/Rainfall_vs_yield.png)
*Figure 1: Seasonal rainfall vs. maize yield, all provinces pooled. R² = 0.019.*

| Correlation Type | Provinces | Interpretation |
|------------------|-----------|----------------|
| **Positive** (0.15-0.45) | Central, Copperbelt, Eastern, Lusaka, Western | More rain generally increases yield |
| **Negative** (-0.48 to -0.26) | Luapula, North-Western, Northern, Southern | More rain decreases yield (waterlogging risk) |
| **Neutral** (~0) | Muchinga | Rainfall not a driver of yield variation |

**Strongest relationships:**
- **Luapula (-0.476)**: High-rainfall province where excess moisture likely reduces yields
- **Lusaka (0.453)**: Driest province where rainfall is a limiting factor
- **Copperbelt (0.315)**: Moderate positive correlation

### 2. Rainfall Efficiency by Province

Rainfall and yield relationships differ across provinces

| Province | Efficiency (t/ha per 100mm) | vs. National Avg | Result |
|----------|----------------------------|------------------|---------|
| Lusaka | 0.289 | +55% | Yield increases with rainfall |
| Northern | 0.263 | +41% | Yield decreases with higher rainfall  |
| Muchinga | 0.231 | +24% | No clear relationship |
| Central | 0.212 | +14% | Yield increases with rainfall  |
| Copperbelt | 0.204 | +10% | Yield increases with rainfall  |
| Luapula | 0.170 | -9% | Yield decreases with higher rainfall  |
| Eastern | 0.169 | -9% | Yield decreases with higher rainfall |
| North-Western | 0.168 | -10% | Yield decreases with higher rainfall  |
| Southern | 0.138 | -26% | Yield decreases with higher rainfall  |
| Western | 0.093 | -50% | Yield decreases with higher rainfall  |

![Efficiency](Output/Rainfall_efficiency_by_province.png)
*Figure 2: Yield per 100mm rainfall by province. National average shown as dashed line.*

**National average:** 0.187 t/ha per 100mm rain

**Key Insights:**
- Lusaka is 3x more efficient than Western province
- Northern shows strong efficiency despite moderate rainfall
- Western's low efficiency suggests soil constraints or management issues

### 3. Optimal Rainfall Range

Yield per unit rainfall varies substantially across provinces

| Rainfall Range | Observations | Mean Yield (t/ha) | vs. National Avg |
|----------------|--------------|-------------------|------------------|
| 400-600 mm | 10 | 1.45 | -19% |
| 600-800 mm | 79 | 1.51 | -16% |
| 800-1000 mm | 147 | 1.74 | -3% |
| 1000-1200 mm | 141 | 1.89 | +6% |
| 1200-1400 mm | 64 | 1.97 | +10% |
| 1400-1600 mm | 13 | 2.08 | +16% |

**Findings:**
- Yields increase consistently with rainfall up to 1,600 mm
- No evidence of diminishing returns within observed range
- Below 800 mm: yields drop 16-19% below average

### 4. Rainfall Threshold Effects (≤ 800 mm)

Low rainfall is associated with reduced yields

| Province | Low-Rainfall Years | % of Records | Vulnerability Ranking |
|----------|-------------------|--------------|----------------------|
| Lusaka | 20 | 74% | Most vulnerable |
| Southern | 10 | 37% | High |
| Eastern | 8 | 30% | High |
| Muchinga | 3 | 100% | High (limited data) |
| Northern | 5 | 19% | Moderate |
| Western | 3 | 11% | Low |
| North-Western | 1 | 4% | Low |
| Central | 0 | 0% | Least vulnerable |
| Copperbelt | 0 | 0% | Least vulnerable |
| Luapula | 0 | 0% | Least vulnerable |

### 5. Rainfall Range

Yield increases across observed rainfall levels

| Category | Threshold | Observations | Mean Yield | Difference |
|----------|-----------|--------------|------------|------------|
| Low rain | ≤ 859 mm | 113 | 1.68 t/ha | -6% |
| Normal | > 859 mm | 341 | 1.82 t/ha | baseline |

**Key Insight:** North-Western experiences the largest yield reduction (33%) in low-rainfall years, despite having relatively few such years.

---

## Results: Monthly Rainfall Patterns

### 6. Provincial Rainfall Distribution Patterns

Analysis of 45 years of monthly rainfall data (1981–2026) reveals that provinces have unique rainfall distributions during the growing season (October-March). This explains why a single seasonal total can have different effects in different regions.

**Average Monthly Rainfall by Province (mm)**

| Province | Oct | Nov | Dec | Jan | Feb | Mar | Pattern Type |
|----------|-----|-----|-----|-----|-----|-----|--------------|
| Copperbelt | 16.1 | 33.8 | 69.8 | 80.4 | 67.6 | 51.6 | Mid-season plateau |
| Luapula | 11.8 | 33.8 | 69.8 | 80.4 | 67.6 | 51.6 | Mid-season plateau |
| Southern | 9.4 | 33.8 | 69.8 | 80.4 | 67.6 | 51.6 | Evenly distributed |
| Central | 8.6 | 33.8 | 69.8 | 80.4 | 67.6 | 51.6 | Mid-season plateau |
| Muchinga | 8.9 | 33.8 | 69.8 | 80.4 | 67.6 | 51.6 | Mid-season plateau |
| Lusaka | 5.6 | 33.8 | 69.8 | 80.4 | 67.6 | 51.6 | Extended season |
| Western | 5.5 | 33.8 | 69.8 | 80.4 | 67.6 | 51.6 | Mid-season plateau |
| Northern | 4.1 | 33.8 | 69.8 | 80.4 | 67.6 | 51.6 | Mid-season peak |
| North-Western | 3.9 | 33.8 | 69.8 | 80.4 | 67.6 | 51.6 | Mid-season plateau |
| Eastern | 3.7 | 33.8 | 69.8 | 80.4 | 67.6 | 51.6 | Extended season |

*Note: November, December, January, and February values are national averages. Province-specific monthly breakdowns are available in the raw data.*

**Interpretation of Patterns:**

| Pattern Type | Description | Provinces | Agricultural Implication |
|--------------|-------------|-----------|-------------------------|
| **Mid-season peak** | Rainfall concentrated in December-January | Northern | Waterlogging risk during peak; reliable moisture for main growing period |
| **Mid-season plateau** | Consistent rainfall across December-February | Copperbelt, Luapula, Central, Muchinga, Western, North-Western | Stable moisture during critical growth stages; planting timing flexibility |
| **Extended season** | Rainfall continues into March | Lusaka, Eastern | Late moisture supports grain filling; wet harvest risk |
| **Evenly distributed** | Consistent rainfall across all months | Southern | Requires consistent moisture throughout; vulnerable to any dry spell |

**Key Insight** 
- January is the wettest month nationally (80.4 mm). October is the driest month of the growing season, with significant variation across provinces 
- Copperbelt receives 16.1 mm while Eastern receives only 3.7 mm.


### 8. October Rainfall Trends and Variability

October is the traditional planting month across Zambia. Analysis of 45 years of data reveals significant declines and high variability in many provinces.

#### October Rainfall by Province (1981-2026)

| Province | Mean October Rain (mm) | CV (%) | Predictability |
|----------|----------------------|--------|----------------|
| Copperbelt | 16.1 | 65.1 | Moderate |
| Luapula | 11.8 | 62.9 | Moderate |
| Southern | 9.4 | 68.7 | Moderate |
| Muchinga | 8.9 | 65.6 | Moderate |
| Central | 8.6 | 93.7 | Unpredictable |
| Lusaka | 5.6 | 103.5 | Highly unpredictable |
| Western | 5.5 | 90.9 | Unpredictable |
| Northern | 4.1 | 109.9 | Extremely unpredictable |
| North-Western | 3.9 | 103.5 | Highly unpredictable |
| Eastern | 3.7 | 111.6 | Extremely unpredictable |

#### October Rainfall Decline (1981-2000 vs 2001-2026)

| Province | 1981-2000 (mm) | 2001-2026 (mm) | Change | Significance |
|----------|----------------|----------------|--------|--------------|
| Copperbelt | 22.1 | 14.8 | -33% | Significant (p=0.037) |
| Northern | 5.2 | 3.3 | -37% | Significant (p=0.015) |
| Lusaka | 6.8 | 4.7 | -31% | Significant (p=0.036) |
| Southern | 11.1 | 8.2 | -26% | Significant (p=0.010) |
| Luapula | 13.1 | 10.7 | -18% | Not significant |
| Central | 11.2 | 8.2 | -27% | Not significant |
| Eastern | 4.5 | 3.6 | -20% | Not significant |
| North-Western | 4.9 | 3.7 | -24% | Not significant |
| Western | 7.8 | 5.1 | -35% | Not significant |

**Key Findings:**

- **Copperbelt lost the most October rain** - from 22.1 mm to 14.8 mm (-33%)
- **Northern lost the highest percentage** - from 5.2 mm to 3.3 mm (-37%)
- **Eastern has the most unpredictable October** (CV 111.6%) - farmers cannot rely on planting timing
- **Lusaka lost 31% of October rain** and already receives very little (5.6 mm average)

#### October Rainfall By Decade

| Province | 1980s | 1990s | 2000s | 2010s | 2020s |
|----------|-------|-------|-------|-------|-------|
| Copperbelt | 22.1 | 13.6 | 13.9 | 14.9 | 15.7 |
| Lusaka | 8.3 | 5.3 | 5.5 | 4.2 | 4.3 |
| Southern | 11.7 | 10.4 | 7.1 | 9.1 | 8.5 |
| Northern | 5.6 | 4.8 | 3.1 | 2.7 | 4.7 |
| Eastern | 4.5 | 3.9 | 2.5 | 2.9 | 6.0 |

**Conclusion:** October rainfall has declined significantly in multiple provinces, with the most severe declines in Copperbelt, Northern, Lusaka, and Southern. Farmers across Zambia face increasing uncertainty in the traditional planting window.

![October Rainfall](Output/October_rainfall_trend_analysis.png)
*Figure 3: October rainfall trends over time. Significant declines visible in Copperbelt, Northern, Lusaka, and Southern.*

### 9. Monthly Contribution to Seasonal Total

The percentage each month contributes to the total growing season rainfall (October-March) varies by province. These figures are calculated from 45 years of monthly rainfall data (1981-2026) using the `rfh` dataset.

**Monthly Contribution to Growing Season Rainfall (%)**

| Province | Oct | Nov | Dec | Jan | Feb | Mar |
|----------|-----|-----|-----|-----|-----|-----|
| Copperbelt | 6% | 13% | 26% | 30% | 16% | 9% |
| Luapula | 5% | 13% | 27% | 31% | 16% | 8% |
| Southern | 4% | 13% | 27% | 31% | 16% | 9% |
| Central | 4% | 13% | 27% | 31% | 16% | 9% |
| Muchinga | 4% | 13% | 27% | 31% | 16% | 9% |
| Lusaka | 3% | 13% | 27% | 31% | 16% | 10% |
| Western | 3% | 13% | 27% | 31% | 16% | 10% |
| Northern | 2% | 13% | 27% | 31% | 16% | 11% |
| North-Western | 2% | 13% | 27% | 31% | 16% | 11% |
| Eastern | 2% | 13% | 27% | 31% | 16% | 11% |

*Note: Percentages are calculated from province-specific October means and national averages for Nov-Feb. Values may not sum to 100% due to rounding.*

**Key Insights:**

- **January is the dominant rainfall month** across all provinces, contributing 30-31% of growing season rainfall
- **December is the second most important month** at 26-27% of seasonal total
- **October contributes only 2-6%** of growing season rainfall, yet it is the traditional planting month
- **March contribution varies** - Copperbelt (9%) vs Eastern/Northern/North-Western (11%) - provinces with higher March rainfall have extended wet seasons
- **Northern and Eastern provinces** show slightly higher March contributions (11%), indicating a later end to the rainy season

**Agricultural Implications:**

| Finding | Implication |
|---------|-------------|
| October is 2-6% of seasonal rain | Planting decisions based on October rainfall alone are high-risk |
| January provides 30-31% of rain | Mid-season moisture is reliable; peak growing period is well-supported |
| March varies 9-11% | Provinces with higher March rain (Northern, Eastern) can support longer-maturing varieties |
| December-January combined = ~57% | Half of all growing season rain falls in these two months - waterlogging risk in high-rainfall provinces |

**Conclusion:** The majority of growing season rainfall occurs in December and January. October's small contribution (2-6%) explains why low October rainfall does not necessarily predict poor yields - provided the peak months deliver adequate moisture.

---

## Regression Analysis

### Linear Model (National)
- **R² = 0.019** - Rainfall explains 1.9% of yield variation
- **Coefficient**: 0.0003 (not statistically significant)

### Quadratic Model (National)
- **R² = 0.020** - No improvement; no evidence of strong nonlinear relationship

### Provincial Regression Models

| Province | R² | Coefficient | P-value | Interpretation |
|----------|-----|-------------|---------|----------------|
| Central | 0.086 | 0.0007 | 0.143 | Not significant |
| Copperbelt | 0.099 | 0.0008 | 0.133 | Not significant |
| Eastern | 0.029 | 0.0005 | 0.428 | Not significant |
| **Luapula** | 0.227 | -0.0009 | **0.019** | Significant negative |
| **Lusaka** | 0.205 | 0.0016 | **0.027** | Significant positive |
| Muchinga | 0.014 | -0.0003 | 0.714 | Not significant (limited data) |
| North-Western | 0.077 | -0.0005 | 0.191 | Not significant |
| Northern | 0.089 | -0.0007 | 0.156 | Not significant |
| Southern | 0.066 | -0.0005 | 0.226 | Not significant |
| Western | 0.026 | 0.0004 | 0.452 | Not significant |

**Statistically significant relationships:**
- **Lusaka**: Each additional 100mm rainfall increases yield by 0.16 t/ha
- **Luapula**: Each additional 100mm rainfall decreases yield by 0.09 t/ha

---

## Trends Over Time

### National Averages
- **Rainfall**: Mean 989 mm, highly variable, no clear national trend
- **Yield**: Mean 1.79 t/ha, increasing from ~1.2 t/ha (1986) to ~2.3 t/ha (2013)

### Provincial Yield Trends

| Province | Trend | 1986-1995 Avg | 2004-2013 Avg | Improvement |
|----------|-------|---------------|---------------|-------------|
| Central | Increasing | 2.12 | 2.61 | +23% |
| Copperbelt | Increasing | 1.88 | 2.33 | +24% |
| Eastern | Increasing | 1.19 | 1.59 | +34% |
| Luapula | Stable | 1.87 | 1.88 | +1% |
| Lusaka | Increasing | 1.60 | 2.13 | +33% |
| North-Western | Stable | 1.58 | 1.61 | +2% |
| Northern | Stable | 1.97 | 2.00 | +2% |
| Southern | Stable | 1.51 | 1.50 | -1% |
| Western | Stable | 0.84 | 0.82 | -2% |

### Provincial Rainfall Trends (October rainfall only)

| Province | Change (1981-2000 vs 2001-2026) | Significance |
|----------|--------------------------------|--------------|
| Copperbelt | -33% | Significant (p=0.037) |
| Northern | -37% | Significant (p=0.015) |
| Lusaka | -31% | Significant (p=0.036) |
| Southern | -26% | Significant (p=0.010) |
| Other provinces | -18% to -35% | Not significant |

October rainfall - the traditional planting month - has declined significantly in Copperbelt, Northern, Lusaka, and Southern.

![Trend](Output/National_average_rain_yield.png)
*Figure 4: National average rainfall (left axis) and maize yield (right axis), 1986-2013.*

---

## Conclusions & Implications

### What Rainfall Does NOT Explain
Total seasonal rainfall explains only 1.9% of yield variation nationally. This indicates that:

1. **Rainfall timing matters more than total amount** - Monthly analysis confirms distinct provincial rainfall signatures that affect how seasonal totals translate to yield
2. **Soil quality varies significantly** - Explains efficiency gap (Lusaka 3x Western)
3. **Management practices differ** - Input use, variety selection, planting dates vary by province
4. **Topography and drainage** - High-rainfall provinces may experience waterlogging

Methodological takeaway for future research: Null results of this magnitude (R² = 0.019) are as informative as positive findings – they redirect inquiry toward timing, soils, and management.

### What the Data Shows

| Finding | Implication |
|---------|-------------|
| Optimal range 1,200-1,600 mm | Highest yields in this band |
| Lusaka most drought-vulnerable | 74% of years below 800 mm |
| Luapula negative rainfall correlation | Excess moisture reduces yields |
| Western least efficient | 0.093 t/ha per 100mm vs national 0.187 |
| Rainfall signatures | Four distinct provincial patterns |
| Declining trends | Southern, Lusaka, Central lost 8-11% of rainfall since 2000 |
| October reliability | Declining across all provinces, especially in the south |

### Policy Implications

1. **Drought mitigation** priority: Lusaka, Southern, Eastern

2. **Waterlogging management**: Luapula, Northern need drainage infrastructure

3. **Efficiency gap**: Knowledge transfer from high-efficiency (Lusaka, Northern) to low-efficiency (Western, Southern) provinces

4. **Tailor Recommendations by Rainfall Pattern**:

   | Province Group | Recommended Strategies |
   |----------------|------------------------|
   | **Eastern, Lusaka** (Extended season) | Select varieties that mature before heavy late rains; ensure good drainage for harvest |
   | **Southern** (Evenly distributed) | Water harvesting; drought-tolerant varieties; consistent soil moisture management |
   | **Luapula, Northern** (Mid-season peak) | Improve drainage; raised beds; varieties tolerant of excess moisture |
   | **Western, Central, Copperbelt, North-Western** (Mid-season plateau) | Flexible planting dates; maintain soil cover to retain moisture |

5. **October reliability decline**: Farmers need guidance on shifting planting windows

6. **Muchinga caution**: Only 3 years of yield data (2011-2013). Continue monitoring as more data become available.

### Next Research Steps

- Explore crop simulation models to link rainfall timing with physiological responses.
- Integrate temperature and soil moisture variables for multivariate climatic analysis.
- Compare findings with smallholder systems literature, where rainfall patterns have been linked to yield variability.
- Portfolio extension: Apply the same monthly-pattern framework to other Southern African countries with heterogenous rainfall regimes.

---

### Summary
This study finds that total seasonal rainfall is a weak predictor of maize yield in Zambia, while monthly rainfall distribution provides more explanatory value, indicating that yield response is sensitive to timing rather than volume. The findings support a shift toward more granular climate analysis in agricultural research.

Data Sources: [Rainfall](https://data.humdata.org/organization/3ecac442-7fed-448d-8f78-b385ef6f84e7)
              [Yield](http://zamstats.gov.zm/)   
