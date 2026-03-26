<h1>Rainfall Variability and Its Effect on Maize Yield in Zambia (1986–2013)</h1>

A comprehensive analysis examining the relationship between seasonal rainfall patterns and maize yield across nine Zambian provinces from 1986 to 2013.

##  Table of Contents
- [Project Overview](#project-overview)
- [Data Summary](#data-summary)
- [Dataset Structure](#dataset-structure)
- [Summary Statistics](#summary-statistics)
- [Key Findings](#key-findings)
- [Regression Analysis](#regression-analysis)
- [Trends Over Time](#trends-over-time)
- [Conclusions & Implications](#conclusions--implications)
- [Next Steps / Tableau Integration](#next-steps--tableau-integration)
- [Repository Structure](#repository-structure)
- [Requirements](#requirements)
- [Usage](#usage)
- [Data Citation](#data-citation)


## Project Overview

This analysis investigates the relationship between rainfall and maize yield across nine provinces of Zambia. Initial analysis of **seasonal rainfall totals** showed a weak correlation with yield (R² = 0.019), suggesting total rainfall alone does not explain agricultural outcomes. To understand why, we conducted a deeper investigation into **monthly rainfall patterns** across the growing season (October–March). This revealed distinct regional rainfall "signatures" that, when combined with seasonal yield data, provide a more nuanced understanding of climate impacts on agriculture.

**Key Finding**: The relationship between rainfall and maize yield is not uniform across Zambia. It is mediated by the **timing and distribution of rainfall**, which varies significantly by province. While seasonal totals are a poor predictor, the *pattern* of rain across the growing season is critical. This report identifies these regional patterns and their implications for agricultural planning.

---

## Data & Methods

### Data Sources
- **Rainfall Data**: Monthly rainfall (rfq) from 1981–2026, sourced from `rainfall_analysis_rf_rfq` (8,150 observations).
- **Yield Data**: Annual maize yield (t/ha) from 1986–2013, sourced from `Final_maize_production_yield_climate_dataset` (432 observations).
- **Provinces**: 9 provinces (Muchinga excluded due to limited data).

### Analysis Approach
1. **Seasonal Analysis**: Correlated total growing season rainfall (Oct–Mar) with annual yield to establish baseline.
2. **Monthly Pattern Analysis**: Analyzed 45 years of monthly rainfall to characterize the typical rainfall distribution for each province.
3. **Temporal Trend Analysis**: Assessed changes in seasonal totals and monthly patterns between the periods 1981–2000 and 2001–2026.

---

## Key Findings

### 1. Rainfall-Yield Correlation is Weak Nationally (R² = 0.019)

The overall correlation between total growing season rainfall and maize yield is 0.137, explaining only 1.9% of yield variation. This indicates that **total rainfall is a poor predictor** and that other factors—including rainfall timing and distribution—are primary drivers.

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

### 2. Provincial Rainfall Patterns Reveal Distinct "Signatures"

Monthly analysis shows that provinces have unique rainfall distributions during the growing season (October–March). This explains why a single seasonal total can have different effects in different regions.

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

---

### 3. Seasonal Totals Show Significant Declines in Vulnerable Provinces

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

---

### 4. October is No Longer a Reliable Planting Month

Contrary to common assumption, October is **not** the wettest month for any province. Its reliability as the planting window has declined, especially in drier provinces.

**Frequency of Low October Rainfall (<70mm)**

| Province | 1980s (% Low Oct) | 2010s-20s (% Low Oct) | Change |
|----------|-------------------|----------------------|--------|
| Lusaka | ~20% | ~50% | +30% |
| Southern | ~25% | ~55% | +30% |
| Eastern | ~15% | ~40% | +25% |
| Central | ~10% | ~35% | +25% |

This forces farmers to delay planting, compressing the growing season and increasing the risk of mid-season dry spells affecting critical growth stages.

---

### 5. Provincial Vulnerability & Efficiency

Combining seasonal and monthly insights clarifies why some provinces are more vulnerable or efficient.

#### Vulnerability to Low Rainfall (≤1,316 mm)

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

**Most vulnerable**: Lusaka, Southern, Eastern, Western (experience low rainfall in >50% of years)

#### Rainfall Efficiency (Yield per 100mm rain)

| Province | Efficiency (t/ha per 100mm) | vs. National Avg |
|----------|---------------------------|------------------|
| Lusaka | 0.178 | +50% |
| Northern | 0.171 | +44% |
| Central | 0.128 | +8% |
| Copperbelt | 0.127 | +7% |
| Luapula | 0.110 | -8% |
| North-Western | 0.106 | -11% |
| Eastern | 0.104 | -13% |
| Southern | 0.084 | -29% |
| Western | 0.060 | -50% |

**National average**: 0.119 t/ha per 100mm rain

The efficiency gap (Lusaka 3× more efficient than Western) suggests differences in soil quality, management practices, and the alignment of rainfall patterns with crop growth stages.

---

### 6. Optimal Rainfall Range

| Rainfall Range | Observations | Mean Yield (t/ha) | vs. National Avg |
|----------------|--------------|------------------|------------------|
| <800 mm | 2 | 0.90 | -49% |
| 800-1000 mm | 25 | 1.14 | -35% |
| 1000-1200 mm | 56 | 1.53 | -13% |
| 1200-1400 mm | 89 | 1.83 | +4% |
| 1400-1600 mm | 97 | 1.85 | +5% |
| 1600-1800 mm | 74 | 1.79 | +2% |
| >1800 mm | 89 | 1.84 | +5% |

**Optimal range**: 1200-1600 mm. Yields peak in this band, with diminishing returns above 1800 mm.

---

## Conclusions & Implications

### Why Doesn't Total Rainfall Predict Yield?

The weak correlation between seasonal totals and yield is explained by the diversity of rainfall patterns across Zambia. A province with a mid-season peak (Luapula) will respond differently to a given amount of rain than one with an extended season (Eastern) or evenly distributed pattern (Southern). **The timing and distribution, not just the total, determine the outcome.**

### What the Data Shows

| Finding | Implication |
|---------|--------------|
| Rainfall patterns vary significantly by province | One-size-fits-all agricultural advice is ineffective |
| Southern, Lusaka, Central have lost 8-11% of seasonal rainfall since 2000 | Adaptation strategies must accelerate in these regions |
| October rains are increasingly unreliable | Planting windows are shifting later |
| Eastern and Lusaka show extended rainfall into March | Creates both opportunity (grain filling) and risk (wet harvest) |
| High variability provinces (Southern, Lusaka, Eastern) show stronger yield-rainfall relationships | These provinces are most vulnerable to climate variability |
| Efficiency gap between provinces is 3× | Significant potential for knowledge transfer and improved practices |

### Policy & Practice Implications

1. **Tailor Recommendations by Province**

   | Province Group | Recommended Strategies |
   |----------------|------------------------|
   | **Eastern, Lusaka** (Extended season) | Select varieties that mature before heavy late rains; ensure good drainage for harvest; use late-season moisture for grain filling |
   | **Southern** (Evenly distributed) | Water harvesting; drought-tolerant varieties; consistent soil moisture management |
   | **Luapula, Northern** (Mid-season peak) | Improve drainage to prevent waterlogging; raised beds; varieties tolerant of excess moisture |
   | **Western, Central, Copperbelt, North-Western** (Mid-season plateau) | Balanced water management; flexible planting dates; maintain soil cover to retain moisture |

2. **Accelerate Climate Adaptation**
   - Promote short-season, drought-tolerant maize varieties for Southern, Lusaka, and Central
   - Shift planting windows later where appropriate (especially in provinces with declining October rains)
   - Expand extension services focused on climate-smart agriculture in the most affected provinces

3. **Bridge the Efficiency Gap**
   - Investigate practices in high-efficiency provinces (Lusaka, Northern) that could be transferred
   - Focus on soil health, planting timing, and input management
   - Consider farmer-to-farmer knowledge exchange programs

4. **Address Harvest Risks**
   - For Eastern and Lusaka, develop and promote storage solutions that protect grain from late-season moisture
   - Encourage early-maturing varieties to avoid wet harvest conditions

---

## Next Steps / Tableau Integration

### Planned Visualizations

1. **Provincial Rainfall Signatures Dashboard**
   - Heatmaps and line charts showing distinct monthly patterns for each province
   - Highlight differences between mid-season peak, plateau, extended, and distributed patterns

2. **Temporal Shift Analysis**
   - Maps and bar charts illustrating change in seasonal totals (1981-2000 vs 2001-2026)
   - Increasing frequency of low October rainfall by province

3. **Efficiency & Vulnerability Map**
   - Geographic overlay of yield per 100mm rain with vulnerability ranking
   - Color-coded by rainfall pattern type

4. **Extreme Year Timeline**
   - Interactive timeline highlighting driest/wettest seasons (e.g., 1992, 2015, 2019)
   - Compare against yield outcomes by province

---

## Repository Structure
