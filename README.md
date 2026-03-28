# Rainfall Variability and Its Effect on Maize Yield in Zambia (1986-2013)

This analysis examines how seasonal rainfall influences maize yield across ten provinces of Zambia. The analysis includes Muchinga province, which was previously excluded due to data limitations but now has sufficient yield data for inclusion.

## Table of Contents
- [Research Questions](#research-questions)
- [Data Summary](#data-summary)
- [Dataset Structure](#dataset-structure)
- [Summary Statistics](#summary-statistics)
- [Key Findings](#key-findings)
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

- **Time period:** 1986-2013
- **Provinces analyzed:** 10 (including Muchinga)
- **Observations:** 454 records (after filtering zero yields)
- **Rainfall range:** 445 mm - 1,537 mm (seasonal total)
- **Yield range:** 0.19 - 3.58 t/ha

### Data Quality Notes

| Note | Description |
|------|-------------|
| Zero yields removed | Records with yield = 0 were excluded (assumed missing data) |
| Muchinga included | Now has sufficient data for analysis (2003-2013) |
| Complete coverage | All 10 provinces represented |

---

## Dataset Structure

| Column | Description |
|--------|-------------|
| Province | Administrative province (10 total) |
| Year | 1986-2013 |
| Rainfall_mm | Total seasonal rainfall (mm) |
| Yield_t_ha | Maize yield (tons/hectare) |
| Rain_efficiency | Calculated: Yield per 100mm rainfall |

---

## Summary Statistics

### Overall Summary Statistics (10 provinces, 1986-2013)

| Metric | Rainfall (mm) | Yield (t/ha) |
|--------|---------------|--------------|
| Mean | 989 | 1.79 |
| Min | 445 | 0.19 |
| Max | 1,537 | 3.58 |
| Std Dev | 184 | 0.74 |

### By Province

| Province | Records | Mean Rainfall (mm) | Mean Yield (t/ha) | Rainfall-Yield Correlation |
|----------|---------|-------------------|------------------|---------------------------|
| Central | 27 | 1,128 | 2.39 | 0.294 |
| Copperbelt | 27 | 1,059 | 2.15 | 0.315 |
| Eastern | 27 | 859 | 1.45 | 0.170 |
| Luapula | 27 | 1,108 | 1.88 | -0.476 |
| Lusaka | 27 | 689 | 1.91 | 0.453 |
| Muchinga | 12 | 823 | 1.86 | -0.117 |
| North-Western | 27 | 975 | 1.63 | -0.277 |
| Northern | 27 | 768 | 1.99 | -0.298 |
| Southern | 27 | 1,098 | 1.51 | -0.258 |
| Western | 27 | 891 | 0.83 | 0.161 |

**Key Observations:**
- Central and Copperbelt have highest yields (>2.1 t/ha)
- Western has lowest yields (0.83 t/ha) despite moderate rainfall
- Muchinga yields (1.86 t/ha) are above national average

---

## Key Findings

### 1. Rainfall-Yield Correlation Varies by Province

**Overall correlation**: 0.137 (rainfall explains 1.9% of yield variation nationally)

| Correlation Type | Provinces | Interpretation |
|------------------|-----------|----------------|
| **Positive** (0.15-0.45) | Central, Copperbelt, Eastern, Lusaka, Western | More rain generally increases yield |
| **Negative** (-0.48 to -0.26) | Luapula, North-Western, Northern, Southern | More rain decreases yield (waterlogging risk) |
| **Neutral** (~0) | Muchinga | Rainfall not a driver of yield variation |

**Strongest relationships:**
- **Luapula (-0.476)**: High-rainfall province where excess moisture likely reduces yields
- **Lusaka (0.453)**: Driest province where rainfall is a limiting factor
- **Copperbelt (0.315)**: Moderate correlation

### 2. Rainfall Efficiency by Province

| Province | Efficiency (t/ha per 100mm) | vs. National Avg | Ranking |
|----------|----------------------------|------------------|---------|
| Lusaka | 0.289 | +55% | 1 |
| Central | 0.212 | +14% | 2 |
| Copperbelt | 0.204 | +10% | 3 |
| Northern | 0.263 | +41% | 4 |
| Muchinga | 0.231 | +24% | 5 |
| Eastern | 0.169 | -9% | 6 |
| North-Western | 0.168 | -10% | 7 |
| Luapula | 0.170 | -9% | 8 |
| Southern | 0.138 | -26% | 9 |
| Western | 0.093 | -50% | 10 |

**National average:** 0.187 t/ha per 100mm rain

**Key Insights:**
- Lusaka is 3× more efficient than Western province
- Northern shows strong efficiency despite high rainfall
- Western's low efficiency suggests soil constraints or management issues

### 3. Optimal Rainfall Range

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

### 4. Vulnerability to Low Rainfall (≤ 800 mm)

| Province | Low-Rainfall Years | % of Records | Vulnerability Ranking |
|----------|-------------------|--------------|----------------------|
| Lusaka | 20 | 74% | Most vulnerable |
| Southern | 10 | 37% | High |
| Eastern | 8 | 30% | High |
| Northern | 5 | 19% | Moderate |
| Muchinga | 3 | 25% | Moderate |
| Western | 3 | 11% | Low |
| North-Western | 1 | 4% | Low |
| Central | 0 | 0% | Least vulnerable |
| Copperbelt | 0 | 0% | Least vulnerable |
| Luapula | 0 | 0% | Least vulnerable |

**Drought threshold (25th percentile):** ≤ 859 mm

**Most vulnerable:** Lusaka (74% of years below 800 mm)
**Least vulnerable:** Central, Copperbelt, Luapula (no low-rainfall years)

### 5. Yield in Low vs Normal Rainfall Years

| Category | Threshold | Observations | Mean Yield | Difference |
|----------|-----------|--------------|------------|------------|
| Low rain | ≤ 859 mm | 113 | 1.68 t/ha | -6% |
| Normal | > 859 mm | 341 | 1.82 t/ha | baseline |

**By Province:**

| Province | Low Rain Yield | Normal Yield | Difference |
|----------|----------------|--------------|------------|
| Central | N/A | 2.39 | - |
| Copperbelt | N/A | 2.15 | - |
| Eastern | 1.39 | 1.48 | -6% |
| Luapula | N/A | 1.88 | - |
| Lusaka | 1.83 | 2.14 | -14% |
| Muchinga | 1.61 | 1.94 | -17% |
| North-Western | 1.10 | 1.65 | -33% |
| Northern | 1.79 | 2.04 | -12% |
| Southern | 1.44 | 1.55 | -7% |
| Western | 0.79 | 0.83 | -5% |

**Key Insight:** North-Western experiences the largest yield reduction (33%) in low-rainfall years, despite having relatively few such years.

---

## Regression Analysis

### Linear Model (National)
- **R² = 0.019** - Rainfall explains 1.9% of yield variation
- **Coefficient**: 0.0003 (not statistically significant)

### Provincial Regression Models

| Province | R² | Coefficient | P-value | Interpretation |
|----------|-----|-------------|---------|----------------|
| Central | 0.086 | 0.0007 | 0.143 | Not significant |
| Copperbelt | 0.099 | 0.0008 | 0.133 | Not significant |
| Eastern | 0.029 | 0.0005 | 0.428 | Not significant |
| **Luapula** | 0.227 | -0.0009 | **0.019** | Significant negative |
| **Lusaka** | 0.205 | 0.0016 | **0.027** | Significant positive |
| North-Western | 0.077 | -0.0005 | 0.191 | Not significant |
| Northern | 0.089 | -0.0007 | 0.156 | Not significant |
| Southern | 0.066 | -0.0005 | 0.226 | Not significant |
| Western | 0.026 | 0.0004 | 0.452 | Not significant |
| Muchinga | 0.014 | -0.0003 | 0.714 | Not significant |

**Statistically significant relationships:**
- **Lusaka**: Each additional 100mm rainfall increases yield by 0.16 t/ha
- **Luapula**: Each additional 100mm rainfall decreases yield by 0.09 t/ha

---

## Trends Over Time

### National Averages
- **Rainfall**: Mean 989 mm, range 445-1,537 mm
- **Yield**: Mean 1.79 t/ha, increasing trend over time
- **Yield improvement**: From ~1.2 t/ha (1986) to ~2.3 t/ha (2013)

### Provincial Yield Trends
| Province | Trend | 1986-1995 Avg | 2004-2013 Avg | Improvement |
|----------|-------|---------------|---------------|-------------|
| Central | Increasing | 2.12 | 2.61 | +23% |
| Copperbelt | Increasing | 1.88 | 2.33 | +24% |
| Eastern | Increasing | 1.19 | 1.59 | +34% |
| Luapula | Stable | 1.87 | 1.88 | +1% |
| Lusaka | Increasing | 1.60 | 2.13 | +33% |
| Muchinga | - | - | 1.86 | - |
| North-Western | Stable | 1.58 | 1.61 | +2% |
| Northern | Stable | 1.97 | 2.00 | +2% |
| Southern | Stable | 1.51 | 1.50 | -1% |
| Western | Stable | 0.84 | 0.82 | -2% |

**Key Observations:**
- Eastern and Lusaka show strongest yield growth (>30% improvement)
- Western and Southern show no improvement over time
- Luapula yields stable despite high rainfall

---

## Conclusions & Implications

### What Rainfall Does NOT Explain
Total seasonal rainfall explains only 1.9% of yield variation nationally. This indicates that:

1. **Rainfall timing matters** - Seasonal totals alone insufficient
2. **Soil quality varies** - Explains efficiency gap (Lusaka 3× Western)
3. **Management practices differ** - Input use, variety selection, planting dates
4. **Topography and drainage** - Waterlogging in high-rainfall provinces

### What the Data Shows

| Finding | Implication |
|---------|-------------|
| Optimal range 1,200-1,600 mm | Highest yields in this band |
| Lusaka most drought-vulnerable | 74% of years below 800 mm |
| Luapula negative rainfall correlation | Excess moisture reduces yields |
| Western least efficient | 0.093 t/ha per 100mm vs national 0.187 |
| Muchinga yields above average | Performs well despite limited data |
| Yield growth varies | Eastern (+34%), Western (-2%) |

### Policy Implications

1. **Drought mitigation** priority: Lusaka, Southern, Eastern

2. **Waterlogging management**: Luapula, Northern need drainage infrastructure

3. **Efficiency gap**: Knowledge transfer from Lusaka/Central to Western/Southern

4. **Muchinga**: Include in future analysis; shows promising yields

5. **Variety selection**: Match to provincial rainfall patterns

---

## Repository Structure

| Folder | File | Description |
|--------|------|-------------|
| DATA/ | Final_rainfall_and_yield_data.xlsx | Raw data: province, year, seasonal rainfall total (mm), yield (t/ha) |
| PYTHON/ | rainfall_yield_analysis.py | Complete analysis script: data preparation, EDA, correlation, regression, efficiency metrics, drought vulnerability |
| REPORTS/ | README.md | This report with all findings and interpretations |

### Data Citation

Maize yield and rainfall data for Zambian provinces, 1986-2013. Cleaned dataset includes 454 records across 10 provinces.