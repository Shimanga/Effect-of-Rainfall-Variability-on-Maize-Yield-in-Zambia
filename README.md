# Rainfall Variability and Its Effect on Maize Yield in Zambia (1986–2013)

A comprehensive analysis examining the relationship between seasonal rainfall patterns and maize yield across nine Zambian provinces from 1986 to 2013, with new insights from monthly rainfall data (1981–2026).

## Table of Contents
- [Project Overview](#project-overview)
- [Data Summary](#data-summary)
- [Dataset Structure](#dataset-structure)
- [Summary Statistics](#summary-statistics)
- [Key Findings](#key-findings)
- [Monthly Rainfall Analysis (NEW)](#monthly-rainfall-analysis-new)
- [Regression Analysis](#regression-analysis)
- [Trends Over Time](#trends-over-time)
- [Conclusions & Implications](#conclusions--implications)
- [Next Steps / Tableau Integration](#next-steps--tableau-integration)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Usage](#usage)
- [Data Citation](#data-citation)

---

## Project Overview

This analysis investigates the relationship between rainfall and maize yield across nine provinces of Zambia from 1986 to 2013. Initial analysis of **seasonal rainfall totals** showed a weak correlation with yield (R² = 0.019), suggesting total rainfall alone does not explain agricultural outcomes. To understand why, we conducted a deeper investigation into **monthly rainfall patterns** (1981–2026) across the growing season (October–March). This revealed distinct regional rainfall "signatures" that provide a more nuanced understanding of climate impacts on agriculture.

**Key Finding**: The relationship between rainfall and maize yield is not uniform across Zambia. It is mediated by the **timing and distribution of rainfall**, which varies significantly by province. While seasonal totals are a poor predictor, the *pattern* of rain across the growing season is critical. This report identifies these regional patterns and their implications for agricultural planning.

---

## Data Summary

- **Time period (yield):** 1986–2013
- **Time period (rainfall):** 1981–2026
- **Provinces analyzed:** 9 (Muchinga excluded from yield analysis due to limited data)
- **Observations:** 432 (yield), 8,150 (monthly rainfall)
- **Rainfall range:** 723 mm – 2,498 mm (seasonal total)
- **Yield range:** 0.19 – 3.58 t/ha

### Sources
- **Yield Dataset**: `Final_maize_production_yield_climate_dataset` (438 observations across 10 provinces)
- **Rainfall Dataset**: `rainfall_analysis_rf_rfq` (8,150 monthly observations)
- **Note**: Rainfall data originally recorded at 1000× scale, converted to millimeters

### Critical Data Limitations

| Limitation | Impact |
|------------|--------|
| Missing yield data (2008-2010) | All provinces missing 3 years; these years excluded from yield analysis |
| Muchinga province only 2011-2013 | Excluded from time-series and trend analysis for yield |
| Seasonal yield data only | Cannot directly correlate monthly rainfall with yield at monthly resolution |
| Rainfall timing analysis indirect | Monthly patterns inform interpretation of seasonal yield outcomes |

---

## Dataset Structure

### Yield Dataset

| Column | Description |
|--------|-------------|
| Province | Administrative province (9 analyzed) |
| Year | 1986-2013 |
| Rainfall_mm | Total seasonal rainfall (mm) |
| Yield_t_ha | Maize yield (tons/hectare) |
| Production_tons | Total production (tons) |
| Rain_efficiency | Calculated: Yield per 100mm rainfall |

### Monthly Rainfall Dataset

| Column | Description |
|--------|-------------|
| PCODE | Province code |
| Province | Administrative province |
| Year | 1981-2026 |
| Month | 1-12 (1=January, 10=October, etc.) |
| rfq | Monthly rainfall (mm) |

---

## Summary Statistics

### Overall Summary Statistics (9 provinces, 1986-2013)

| Metric | Rainfall (mm) | Yield (t/ha) | Production (tons) |
|--------|---------------|--------------|-------------------|
| Mean | 1,542 | 1.76 | 143,871 |
| Min | 723 | 0.19 | 9,216 |
| Max | 2,498 | 3.58 | 745,580 |
| Std Dev | 334 | 0.73 | 136,350 |

### By Province

| Province | Mean Rainfall (mm) | Mean Yield (t/ha) | Rainfall-Yield Correlation |
|----------|-------------------|------------------|---------------------------|
| Central | 1,491 | 1.86 | 0.294 |
| Copperbelt | 1,365 | 1.70 | 0.315 |
| Eastern | 1,057 | 1.07 | 0.170 |
| Luapula | 1,954 | 2.10 | -0.476 |
| Lusaka | 1,065 | 1.83 | 0.453 |
| North-Western | 1,757 | 1.84 | -0.277 |
| Northern | 1,860 | 2.00 | -0.298 |
| Southern | 1,068 | 0.90 | -0.258 |
| Western | 1,262 | 0.77 | 0.161 |

---

## Key Findings

### 1. Rainfall-Yield Correlation is Weak Nationally

**Overall correlation**: 0.137 (Rainfall explains only 1.9% of yield variation)

This weak relationship indicates that total seasonal rainfall is a poor predictor of maize yields across Zambia. Provincial patterns reveal:

- **Positive correlations** in Lusaka (0.453), Copperbelt (0.315), Central (0.294), where rainfall is generally lower
- **Negative correlations** in Luapula (-0.476), Northern (-0.298), North-Western (-0.277), high-rainfall provinces where more rain may reduce yields

This suggests an optimal rainfall range, beyond which additional precipitation becomes detrimental.

### 2. Rainfall Efficiency by Province

| Province | Efficiency (t/ha per 100mm) | vs. National Avg |
|----------|----------------------------|------------------|
| Lusaka | 0.178 | +50% |
| Northern | 0.171 | +44% |
| Central | 0.128 | +8% |
| Copperbelt | 0.127 | +7% |
| Luapula | 0.110 | -8% |
| North-Western | 0.106 | -11% |
| Eastern | 0.104 | -13% |
| Southern | 0.084 | -29% |
| Western | 0.060 | -50% |

**National average:** 0.119 t/ha per 100mm rain

Lusaka is 3× more efficient than Western province, indicating substantial differences in soil quality, management practices, or other factors.

### 3. Optimal Rainfall Range

| Rainfall Range | Observations | Mean Yield (t/ha) | vs. National Avg |
|----------------|--------------|-------------------|------------------|
| <800 mm | 2 | 0.90 | -49% |
| 800-1000 mm | 25 | 1.14 | -35% |
| 1000-1200 mm | 56 | 1.53 | -13% |
| 1200-1400 mm | 89 | 1.83 | +4% |
| 1400-1600 mm | 97 | 1.85 | +5% |
| 1600-1800 mm | 74 | 1.79 | +2% |
| >1800 mm | 89 | 1.84 | +5% |

**Optimal range:** 1200-1600 mm, yields peak and stabilize in this band.
- Below 1000 mm: yields drop sharply (35% below average)
- Above 1800 mm: no additional yield benefit (diminishing returns)

### 4. Vulnerability to Low Rainfall (≤1,316 mm)

| Province | Low-Rainfall Years (1986-2013) |
|----------|-------------------------------|
| Lusaka | 18 |
| Southern | 17 |
| Eastern | 16 |
| Western | 15 |
| Central | 12 |
| Copperbelt | 9 |
| North-Western | 5 |
| Northern | 4 |
| Luapula | 0 |

**Most vulnerable:** Lusaka, Southern, Eastern, Western - experience low rainfall in >50% of years
**Least vulnerable:** Luapula, Northern - rarely experience drought conditions

### 5. Yield in Extreme Years

| Category | Threshold | Observations | Mean Yield | % vs Normal |
|----------|-----------|--------------|------------|-------------|
| Low rain | ≤1,316 mm | 108 | 1.71 t/ha | 0% |
| Normal | 1,316-1,777 mm | 216 | 1.71 t/ha | baseline |
| High rain | ≥1,777 mm | 108 | 1.89 t/ha | +11% |

Low-rainfall years produce the same average yield as normal years nationally. This masks provincial variation. Some provinces (Lusaka) suffer in dry years, while others (Luapula) may benefit.

---

## Monthly Rainfall Analysis (NEW)

### 6. Provincial Rainfall Patterns Reveal Distinct "Signatures"

Analysis of 45 years of monthly rainfall data (1981–2026) reveals that provinces have unique rainfall distributions during the growing season (October–March). This explains why a single seasonal total can have different effects in different regions.

**Average Monthly Rainfall by Province (mm)**

| Province | Oct | Nov | Dec | Jan | Feb | Mar | Pattern Type |
|----------|-----|-----|-----|-----|-----|-----|--------------|
| **Luapula** | 94 | 109 | 122 | 113 | 98 | 100 | **Mid-season peak (Dec)** |
| **Northern** | 94 | 109 | 118 | 117 | 102 | 94 | **Mid-season peak (Dec-Jan)** |
| **North-Western** | 97 | 92 | 109 | 104 | 97 | 94 | **Mid-season plateau** |
| **Copperbelt** | 97 | 96 | 102 | 105 | 97 | 94 | **Mid-season plateau** |
| **Central** | 97 | 88 | 95 | 102 | 97 | 95 | **Mid-season plateau** |
| **Western** | 87 | 88 | 97 | 99 | 95 | 88 | **Mid-season plateau** |
| **Eastern** | 90 | 88 | 91 | 92 | 93 | 98 | **Extended season** |
| **Lusaka** | 84 | 85 | 89 | 92 | 89 | 96 | **Extended season** |
| **Southern** | 85 | 87 | 91 | 90 | 86 | 90 | **Evenly distributed** |

**Interpretation of Patterns:**

| Pattern Type | Description | Provinces | Agricultural Implication |
|--------------|-------------|-----------|-------------------------|
| **Mid-season peak** | Rainfall concentrated in December-January | Luapula, Northern | Waterlogging risk during peak; reliable moisture for main growing period |
| **Mid-season plateau** | Consistent rainfall across December-February | North-Western, Copperbelt, Central, Western | Stable moisture during critical growth stages; planting timing flexibility |
| **Extended season** | Rainfall continues into March | Eastern, Lusaka | Late moisture supports grain filling; wet harvest risk; requires varieties that mature before heavy late rains |
| **Evenly distributed** | Consistent rainfall across all months | Southern | Requires consistent moisture throughout; vulnerable to any dry spell |

**Key Insight**: October is **not** the wettest month for any province. The timing of peak rainfall varies from December (Luapula, Northern) to a gradual extension into March (Eastern, Lusaka).

### 7. Seasonal Totals Show Significant Declines in Vulnerable Provinces

A comparison of the periods 1981–2000 and 2001–2026 shows significant declines in total growing season rainfall for the driest and most variable provinces.

| Province | 1981–2000 (mm) | 2001–2026 (mm) | Change (mm) | Change (%) | Statistical Significance |
|----------|----------------|----------------|-------------|------------|-------------------------|
| **Southern** | 932 | 831 | **-101** | **-11%** | **Significant** (p=0.015) |
| **Lusaka** | 939 | 841 | **-98** | **-10%** | **Significant** (p=0.023) |
| **Central** | 1,057 | 972 | **-85** | **-8%** | **Significant** (p=0.041) |
| Eastern | 939 | 888 | -51 | -5% | Not Significant |
| Copperbelt | 1,075 | 1,021 | -54 | -5% | Not Significant |
| Western | 968 | 946 | -22 | -2% | Not Significant |
| North-Western | 1,086 | 1,029 | -57 | -5% | Not Significant |
| Northern | 1,165 | 1,133 | -32 | -3% | Not Significant |
| Luapula | 1,206 | 1,184 | -22 | -2% | Not Significant |

**Conclusion**: The provinces already facing the greatest rainfall stress (Southern, Lusaka, Central) are experiencing the most significant reductions in seasonal rainfall.

### 8. October is No Longer a Reliable Planting Month

Contrary to common assumption, October is **not** the wettest month for any province. Its reliability as the planting window has declined, especially in drier provinces.

**Frequency of Low October Rainfall (<70mm)**

| Province | 1980s (% Low Oct) | 2010s-20s (% Low Oct) | Change |
|----------|-------------------|----------------------|--------|
| Lusaka | ~20% | ~50% | +30% |
| Southern | ~25% | ~55% | +30% |
| Eastern | ~15% | ~40% | +25% |
| Central | ~10% | ~35% | +25% |

This forces farmers to delay planting, compressing the growing season and increasing the risk of mid-season dry spells affecting critical growth stages.

### 9. Monthly Contribution to Seasonal Total

| Province | Oct | Nov | Dec | Jan | Feb | Mar |
|----------|-----|-----|-----|-----|-----|-----|
| Luapula | 8% | 9% | 10% | 9% | 8% | 8% |
| Northern | 8% | 9% | 10% | 10% | 9% | 8% |
| North-Western | 9% | 9% | 10% | 10% | 9% | 9% |
| Copperbelt | 9% | 9% | 10% | 10% | 9% | 9% |
| Central | 10% | 9% | 9% | 10% | 10% | 9% |
| Western | 9% | 9% | 10% | 10% | 10% | 9% |
| Eastern | 10% | 10% | 10% | 10% | 10% | 11% |
| Lusaka | 9% | 10% | 10% | 10% | 10% | 11% |
| Southern | 10% | 10% | 10% | 10% | 10% | 10% |

**Key Insights:**
- Eastern and Lusaka show a more **extended rainfall profile**, with March contributing a slightly higher share of seasonal total
- This reflects the gradual end of the rainy season rather than a true peak
- Northern provinces concentrate rainfall in December-January (30% of seasonal total in those two months)

---

## Regression Analysis

### Linear Model (National)
- **R² = 0.019** — Rainfall explains only 1.9% of yield variation
- **Coefficient**: 0.0003 (essentially flat)

### Quadratic Model (National)
- **R² = 0.020** — No improvement; no evidence of strong nonlinear relationship
- **Rainfall² coefficient**: effectively zero

### Provincial Regression Models

| Province | R² | Coefficient | P-value |
|----------|-----|-------------|---------|
| Central | 0.086 | 0.0007 | 0.163 |
| Copperbelt | 0.099 | 0.0008 | 0.133 |
| Eastern | 0.029 | 0.0005 | 0.428 |
| Luapula | 0.227 | -0.0009 | 0.019 |
| Lusaka | 0.205 | 0.0016 | 0.027 |
| North-Western | 0.077 | -0.0005 | 0.191 |
| Northern | 0.089 | -0.0007 | 0.156 |
| Southern | 0.066 | -0.0005 | 0.226 |
| Western | 0.026 | 0.0004 | 0.452 |

**Statistically significant relationships (p<0.05):**
- **Lusaka**: Positive relationship. Each 100mm rain increases yield by 0.16 t/ha
- **Luapula**: Negative relationship. Each 100mm rain decreases yield by 0.09 t/ha

---

## Trends Over Time

### National Averages
- **Rainfall**: Highly variable, no clear trend nationally
- **Yield**: Increased from ~1.2 t/ha (1986) to ~2.0 t/ha (2013), likely due to improved varieties and inputs
- **Production**: Peak at 2.4 million tons (2011), up from 0.8 million (1986)

### Provincial Yield Trends
- All provinces show gradual yield increases over the period
- Luapula and Northern consistently highest-yielding
- Southern and Western consistently lowest

### Provincial Rainfall Trends (NEW)
- **Southern, Lusaka, Central**: Significant declines (-8% to -11%) since 2000
- **Other provinces**: No statistically significant change
- **October rainfall**: Declining reliability across all provinces, especially in the south

---

## Conclusions & Implications

### What Rainfall Does NOT Explain
Total seasonal rainfall is not the primary driver of maize yields in Zambia. The weak correlation (0.137) and low R² (0.019) indicate that:

1. **Rainfall timing matters more than total amount** — The monthly analysis confirms that provinces have distinct rainfall signatures that affect how seasonal totals translate to yield
2. **Soil quality varies significantly** — This explains efficiency differences (Lusaka 3× Western)
3. **Management practices differ** — Input use, variety selection, planting dates vary by province
4. **Topography and drainage** — High-rainfall provinces may experience waterlogging

### What the Data Shows
- **Optimal range**: 1200-1600 mm produces highest yields
- **Diminishing returns**: Above 1800 mm provides no additional benefit
- **Vulnerability pattern**: Southern and Lusaka provinces most drought-prone
- **Efficiency leaders**: Lusaka and Northern convert rainfall to grain most effectively
- **Rainfall signatures**: Four distinct provincial patterns (mid-season peak, mid-season plateau, extended season, evenly distributed)
- **Declining trends**: Southern, Lusaka, and Central have lost 8-11% of growing season rainfall since 2000

### Policy Implications

1. **Drought mitigation** should focus on Lusaka, Southern, Eastern, Western

2. **Waterlogging management** (drainage, raised beds) relevant for Luapula, Northern

3. **Tailor Recommendations by Rainfall Pattern**:

   | Province Group | Recommended Strategies |
   |----------------|------------------------|
   | **Eastern, Lusaka** (Extended season) | Select varieties that mature before heavy late rains; ensure good drainage for harvest; use late-season moisture for grain filling |
   | **Southern** (Evenly distributed) | Water harvesting; drought-tolerant varieties; consistent soil moisture management |
   | **Luapula, Northern** (Mid-season peak) | Improve drainage to prevent waterlogging; raised beds; varieties tolerant of excess moisture |
   | **Western, Central, Copperbelt, North-Western** (Mid-season plateau) | Balanced water management; flexible planting dates; maintain soil cover to retain moisture |

4. **Efficiency gap** suggests potential for knowledge transfer from high- to low-efficiency provinces

5. **October reliability decline** means farmers need guidance on shifting planting windows

---

## Next Steps / Tableau Integration

### Planned Visualizations

1. **Rainfall vulnerability dashboard** — Provincial ranking by low-rainfall frequency

2. **Provincial Rainfall Signatures Dashboard**
   - Heatmaps and line charts showing distinct monthly patterns for each province
   - Highlight differences between pattern types

3. **Temporal Shift Analysis**
   - Maps and bar charts illustrating change in seasonal totals (1981-2000 vs 2001-2026)
   - Increasing frequency of low October rainfall by province

4. **Efficiency mapping** — Geographic visualization of yield per 100mm rain

5. **Extreme Year Timeline**
   - Interactive timeline highlighting driest/wettest seasons (e.g., 1992, 2015, 2019)
   - Compare against yield outcomes by province

6. **Time-series animation** — 45 years of rainfall patterns

---

## Repository Structure

├── DATA/                       # Raw and processed datasets
│   ├── Final_maize_production_yield_climate_dataset.csv
│   └── rainfall_analysis_rf_rfq.csv
├── PYTHON/                     # Analysis scripts
│   ├── 01_seasonal_analysis.py
│   ├── 02_monthly_patterns.py
│   └── 03_temporal_trends.py
├── REPORTS/                    # Outputs
│   └── README.md (this file)
└── SQL/                        # Data cleaning scripts (if any)


### File Descriptions

| File | Description | Key Outputs |
|------|-------------|-------------|
| `Final_maize_production_yield_climate_dataset.csv` | Maize yield and seasonal rainfall data (1986-2013) | Province-level yield, production, seasonal rainfall totals |
| `rainfall_analysis_rf_rfq.csv` | Monthly rainfall data (1981-2026) | Monthly rainfall (rfq) by province, year, month |
| `01_seasonal_analysis.py` | Yield data analysis | Correlation tables, efficiency metrics, regression models |
| `02_monthly_patterns.py` | Monthly rainfall analysis | Provincial rainfall signatures, monthly averages, heatmaps |
| `03_temporal_trends.py` | Trend analysis | Pre/post-2000 comparisons, significance tests, extreme years |

