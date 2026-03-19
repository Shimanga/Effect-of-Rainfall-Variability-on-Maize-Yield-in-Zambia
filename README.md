<h1>Rainfall Variability and Its Effect on Maize Yield in Zambia (1986–2013)</h1>

A comprehensive analysis examining the relationship between seasonal rainfall patterns and maize yield across nine Zambian provinces from 1986 to 2013.

## 📋 Table of Contents
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

##  Project Overview

This analysis investigates the relationship between seasonal rainfall and maize yield across nine provinces of Zambia from 1986 to 2013. The dataset combines annual rainfall totals with maize production and yield figures to assess how precipitation patterns influence agricultural outcomes.

**Key Finding**  
Rainfall explains approximately 2% of variation in maize yields nationally (R² = 0.019), suggesting that factors beyond total seasonal rainfall, including rainfall timing, soil conditions, and agricultural practices, are the primary drivers of yield variability.

##  Data Summary
<ul>
  <li><strong>Time period:</strong> 1986–2013</li>
  <li><strong>Provinces analyzed:</strong> 9 (Muchinga excluded)</li>
  <li><strong>Observations:</strong> 432</li>
  <li><strong>Rainfall range:</strong> 723 mm – 2498 mm</li>
  <li><strong>Yield range:</strong> 0.19 – 3.58 t/ha</li>
</ul>

### Source
- **Dataset**: Final_maize_production_yield_climate_dataset
- **Observations**: 438 across 10 provinces
- **Note**: Rainfall data originally recorded at 1000× scale, converted to millimeters

### Data Cleaning

### Critical Data Limitations

| Limitation | Impact |
|------------|--------|
| Missing yield data (2008-2010) | All provinces missing 3 years; these years excluded from analysis |
| Muchinga province only 2011-2013 | Excluded from time-series and trend analysis |
| Seasonal totals only | Cannot assess rainfall timing or distribution within growing season |
| No monthly data | Unable to evaluate critical periods (planting, tasseling, grain fill) |

### Dataset Structure

| Column | Description |
|--------|-------------|
| Province | Administrative province (9 analyzed) |
| Year | 1986-2013 |
| Rainfall_mm | Total seasonal rainfall (mm) |
| Yield_t_ha | Maize yield (tons/hectare) |
| Production_tons | Total production (tons) |
| Rain_efficiency | Calculated: Yield per 100mm rainfall |

### Overall Summary Statistics (9 provinces, 1986-2013)

| Metric | Rainfall (mm) | Yield (t/ha) | Production (tons) |
|--------|---------------|--------------|-------------------|
| Mean | 1,542 | 1.76 | 143,871 |
| Min | 723 | 0.19 | 9,216 |
| Max | 2,498 | 3.58 | 745,580 |
| Std Dev | 334 | 0.73 | 136,350 |

### By Province

| Province | Mean Rainfall (mm) | Mean Yield (t/ha) | Rainfall-Yield Correlation |
|----------|-------------------|-------------------|---------------------------|
| Central | 1,491 | 1.86 | 0.294 |
| Copperbelt | 1,365 | 1.70 | 0.315 |
| Eastern | 1,057 | 1.07 | 0.170 |
| Luapula | 1,954 | 2.10 | -0.476 |
| Lusaka | 1,065 | 1.83 | 0.453 |
| North-Western | 1,757 | 1.84 | -0.277 |
| Northern | 1,860 | 2.00 | -0.298 |
| Southern | 1,068 | 0.90 | -0.258 |
| Western | 1,262 | 0.77 | 0.161 |

### Rainfall Efficiency by Province

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

### Optimal Rainfall Range

| Rainfall Range | Observations | Mean Yield (t/ha) | vs. National Avg |
|----------------|--------------|-------------------|------------------|
| <800 mm | 2 | 0.90 | -49% |
| 800-1000 mm | 25 | 1.14 | -35% |
| 1000-1200 mm | 56 | 1.53 | -13% |
| 1200-1400 mm | 89 | 1.83 | +4% |
| 1400-1600 mm | 97 | 1.85 | +5% |
| 1600-1800 mm | 74 | 1.79 | +2% |
| >1800 mm | 89 | 1.84 | +5% |

### Vulnerability to Low Rainfall (≤1,316 mm)

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

### Yield in Extreme Years

| Category | Threshold | Observations | Mean Yield | % vs Normal |
|----------|-----------|--------------|------------|-------------|
| Low rain | ≤1,316 mm | 108 | 1.71 t/ha | 0% |
| Normal | 1,316-1,777 mm | 216 | 1.71 t/ha | baseline |
| High rain | ≥1,777 mm | 108 | 1.89 t/ha | +11% |

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

