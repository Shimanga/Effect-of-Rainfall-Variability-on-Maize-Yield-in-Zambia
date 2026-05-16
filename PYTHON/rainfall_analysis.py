!pip install gspread pandas google-auth

import pandas as pd
import numpy as np
import gspread
from google.colab import auth
from google.auth import default
import matplotlib.pyplot as plt

# Authenticate with Google
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)
sheet_name = "rfh_rainfall"
try:
    spreadsheet = gc.open(sheet_name)
    worksheet = spreadsheet.get_worksheet(0)
    print(f"   Worksheet name: {worksheet.title}")
    data = worksheet.get_all_values()
    df = pd.DataFrame(data[1:], columns=data[0])
    print(f" Loaded {len(df)} rows with {len(df.columns)} columns")
except Exception as e:
    print(f" Error opening spreadsheet: {e}")

numeric_columns = ['year', 'month', 'rfh']
for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna(subset=['rfh', 'year', 'month'])
print(f"\n After cleaning: {len(df)} rows")


# AGGREGATE 3 DEKADS TO MONTHLY TOTALS

df_monthly = (
    df.groupby(['province', 'year', 'month'])['rfh']
    .sum()
    .reset_index()
)
print(f" After dekad aggregation: {len(df_monthly)} monthly rows")

# ASSIGN SEASON LABEL & DROP INCOMPLETE SEASONS

df_monthly['season'] = df_monthly.apply(
    lambda r: r['year'] if r['month'] in [10, 11, 12] else r['year'] - 1, axis=1
)
df_monthly = df_monthly[df_monthly['season'].between(1981, 2024)].copy()
print(f" Complete seasons: 1981–2024 ({df_monthly['season'].nunique()} seasons)\n")

LOW_PERCENTILE = 30
HIGH_PERCENTILE = 70

print(f"\nClassification thresholds:")
print(f"  - Low rainfall: Below {LOW_PERCENTILE}th percentile")
print(f"  - High rainfall: Above {HIGH_PERCENTILE}th percentile")
print(f"  - Normal rainfall: Between these values")

# Global thresholds (monthly rfh)
global_low = np.percentile(df_monthly['rfh'].dropna(), LOW_PERCENTILE)
global_high = np.percentile(df_monthly['rfh'].dropna(), HIGH_PERCENTILE)
print(f"\n=== GLOBAL THRESHOLDS ===")
print(f"Low threshold: {global_low:.2f}")
print(f"High threshold: {global_high:.2f}")

# Province-specific thresholds
province_thresholds = df_monthly.groupby('province')['rfh'].agg([
    ('low_threshold', lambda x: np.percentile(x.dropna(), LOW_PERCENTILE)),
    ('high_threshold', lambda x: np.percentile(x.dropna(), HIGH_PERCENTILE))
]).reset_index()
print(f"\n=== PROVINCE THRESHOLDS ===")
print(province_thresholds)

# Province + Month-specific thresholds
monthly_thresholds = df_monthly.groupby(['province', 'month'])['rfh'].agg([
    ('low_threshold', lambda x: np.percentile(x.dropna(), LOW_PERCENTILE)),
    ('high_threshold', lambda x: np.percentile(x.dropna(), HIGH_PERCENTILE))
]).reset_index()
print(f"\n=== MONTHLY THRESHOLDS ===")
print(monthly_thresholds.head(10))

df_classified = df_monthly.copy()

# Global classification
df_classified['rainfall_class_global'] = 'Normal'
df_classified.loc[df_classified['rfh'] < global_low, 'rainfall_class_global'] = 'Low'
df_classified.loc[df_classified['rfh'] > global_high, 'rainfall_class_global'] = 'High'

# Monthly classification
df_classified = df_classified.merge(monthly_thresholds, on=['province', 'month'], how='left')
df_classified['rainfall_class_monthly'] = 'Normal'
df_classified.loc[df_classified['rfh'] < df_classified['low_threshold'], 'rainfall_class_monthly'] = 'Low'
df_classified.loc[df_classified['rfh'] > df_classified['high_threshold'], 'rainfall_class_monthly'] = 'High'
df_classified = df_classified.rename(columns={
    'low_threshold': 'low_threshold_monthly',
    'high_threshold': 'high_threshold_monthly'
})

print("\n=== CLASSIFICATION DISTRIBUTION ===")
print("\nGlobal Classification:")
print(df_classified['rainfall_class_global'].value_counts())
print(f"\n{df_classified['rainfall_class_global'].value_counts(normalize=True) * 100}")
print("\nMonthly Classification:")
print(df_classified['rainfall_class_monthly'].value_counts())
print(f"\n{df_classified['rainfall_class_monthly'].value_counts(normalize=True) * 100}")

# Save to Google Sheets
try:
    try:
        classified_worksheet = spreadsheet.worksheet("Classified_Data")
        print(f"\nWorksheet 'Classified_Data' already exists. Clearing and updating...")
        classified_worksheet.clear()
    except gspread.exceptions.WorksheetNotFound:
        classified_worksheet = spreadsheet.add_worksheet(title="Classified_Data", rows=1000, cols=20)
        print(f"\n Created new sheet: 'Classified_Data'")

    classified_data = [df_classified.columns.tolist()] + df_classified.astype(str).values.tolist()
    classified_worksheet.update(classified_data, value_input_option='USER_ENTERED')
    print(f" Saved classified data to sheet: 'Classified_Data'")

    try:
        thresholds_worksheet = spreadsheet.worksheet("Thresholds")
        print(f"Worksheet 'Thresholds' already exists. Clearing and updating...")
        thresholds_worksheet.clear()
    except gspread.exceptions.WorksheetNotFound:
        thresholds_worksheet = spreadsheet.add_worksheet(title="Thresholds", rows=1000, cols=10)
        print(f" Created new sheet: 'Thresholds'")

    thresholds_data = [monthly_thresholds.columns.tolist()] + monthly_thresholds.astype(str).values.tolist()
    thresholds_worksheet.update(thresholds_data, value_input_option='USER_ENTERED')
    print(f" Saved thresholds to sheet: 'Thresholds'")

except Exception as e:
    print(f" Could not create or update sheets: {e}")

# Quick classification plot
plt.figure(figsize=(15, 6))
sample_province = df_classified['province'].unique()[0]
sample_data = df_classified[df_classified['province'] == sample_province].copy()
sample_data['Date'] = pd.to_datetime(
    sample_data['year'].astype(str) + '-' + sample_data['month'].astype(str), format='%Y-%m')
sample_data = sample_data.sort_values('Date')
color_map = {'Low': 'red', 'Normal': 'green', 'High': 'blue'}
colors = sample_data['rainfall_class_monthly'].map(color_map)
plt.scatter(sample_data['Date'], sample_data['rfh'], c=colors, alpha=0.6, s=20)
plt.title(f'Rainfall Classification - {sample_province} (Monthly Method)')
plt.xlabel('Date')
plt.ylabel('rfh (mm)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Check provinces
print(" ALL PROVINCES IN DATA \n")
provinces = sorted(df_classified['province'].unique())
print(f"Total provinces: {len(provinces)}")
print(provinces)
if 'Muchinga' in provinces:
    print("\n Muchinga province is included")

provinces_to_plot = [p for p in provinces if p != 'Muchinga']
print(f"\nProvinces to plot: {len(provinces_to_plot)}")

print("\n MONTHLY RAINFALL STATISTICS ")
monthly_stats = df_classified.groupby('month')['rfh'].agg(['count', 'mean', 'std', 'min', 'max']).round(2)
print(monthly_stats)

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

df_classified.boxplot(column='rfh', by='month', ax=axes[0,0])
axes[0,0].set_title('Monthly Rainfall Distribution (All Provinces)')
axes[0,0].set_xlabel('Month')
axes[0,0].set_ylabel('rfh (mm)')
axes[0,0].grid(True, alpha=0.3)

monthly_means = df_classified.groupby('month')['rfh'].mean()
monthly_std = df_classified.groupby('month')['rfh'].std()
axes[0,1].bar(monthly_means.index, monthly_means.values, yerr=monthly_std.values,
              capsize=5, alpha=0.7, color='steelblue')
axes[0,1].set_title('Average Monthly Rainfall (±1 Std Dev)')
axes[0,1].set_xlabel('Month')
axes[0,1].set_ylabel('Mean rfh (mm)')
axes[0,1].grid(True, alpha=0.3)

key_months = [10, 11, 12, 1, 2, 3]
for month in key_months:
    month_data = df_classified[df_classified['month'] == month]
    monthly_avg = month_data.groupby('year')['rfh'].mean()
    axes[1,0].plot(monthly_avg.index, monthly_avg.values,
                   label=f'Month {month}', alpha=0.7, linewidth=1.5)
axes[1,0].set_title('Rainfall Trends by Month (Growing Season)')
axes[1,0].set_xlabel('Year')
axes[1,0].set_ylabel('rfh (mm)')
axes[1,0].legend()
axes[1,0].grid(True, alpha=0.3)

df_for_heatmap = df_classified[df_classified['province'] != 'Muchinga']
pivot_rain = df_for_heatmap.pivot_table(values='rfh', index='province', columns='month', aggfunc='mean')
im = axes[1,1].imshow(pivot_rain.values, aspect='auto', cmap='YlGnBu')
axes[1,1].set_xticks(range(len(pivot_rain.columns)))
axes[1,1].set_xticklabels(pivot_rain.columns)
axes[1,1].set_yticks(range(len(pivot_rain.index)))
axes[1,1].set_yticklabels(pivot_rain.index)
axes[1,1].set_title('Average Rainfall by Province and Month (mm)')
plt.colorbar(im, ax=axes[1,1])
plt.tight_layout()
plt.show()

# Provincial monthly patterns
print("\n PROVINCE-SPECIFIC MONTHLY PATTERNS \n")
n_provinces = len(provinces_to_plot)
n_cols = 3
n_rows = (n_provinces + n_cols - 1) // n_cols
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 4 * n_rows))
axes = axes.flatten() if n_rows > 1 else [axes]

for idx, province in enumerate(provinces_to_plot):
    province_data = df_classified[df_classified['province'] == province]
    monthly_mean = province_data.groupby('month')['rfh'].mean()
    monthly_std = province_data.groupby('month')['rfh'].std()
    axes[idx].bar(monthly_mean.index, monthly_mean.values, yerr=monthly_std.values,
                  capsize=5, alpha=0.7, color='steelblue')
    axes[idx].set_title(f'{province}')
    axes[idx].set_xlabel('Month')
    axes[idx].set_ylabel('Mean rfh (mm)')
    axes[idx].set_xticks(range(1, 13))
    axes[idx].grid(True, alpha=0.3)
for idx in range(len(provinces_to_plot), len(axes)):
    axes[idx].set_visible(False)
plt.tight_layout()
plt.show()

# Rainfall classification plots
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
class_by_month = pd.crosstab(df_classified['month'], df_classified['rainfall_class_monthly'], normalize='index')
class_by_month.plot(kind='bar', stacked=True, ax=axes[0], color=['red', 'green', 'blue'], alpha=0.7)
axes[0].set_title('Rainfall Classification by Month')
axes[0].set_xlabel('Month')
axes[0].set_ylabel('Proportion')
axes[0].legend(title='Class')
axes[0].grid(True, alpha=0.3)

df_for_province = df_classified[df_classified['province'] != 'Muchinga']
class_by_province = pd.crosstab(df_for_province['province'], df_for_province['rainfall_class_monthly'], normalize='index')
class_by_province.plot(kind='bar', stacked=True, ax=axes[1], color=['red', 'green', 'blue'], alpha=0.7)
axes[1].set_title('Rainfall Classification by Province')
axes[1].set_xlabel('Province')
axes[1].set_ylabel('Proportion')
axes[1].legend(title='Class')
axes[1].grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Rainfall variability
cv_data = df_classified[df_classified['province'] != 'Muchinga']
cv_by_month = cv_data.groupby(['province', 'month'])['rfh'].agg(
    lambda x: x.std() / x.mean() * 100 if x.mean() > 0 else 0
).reset_index()

print("\n RAINFALL VARIABILITY (Coefficient of Variation %) \n")
print("Most variable months by province:")
for province in sorted(cv_by_month['province'].unique()):
    province_cv = cv_by_month[cv_by_month['province'] == province]
    if not province_cv.empty:
        max_cv = province_cv.loc[province_cv['rfh'].idxmax()]
        print(f"{province:15s}: Most variable month = {max_cv['month']:.0f} (CV = {max_cv['rfh']:.1f}%)")

pivot_cv = cv_by_month.pivot(index='province', columns='month', values='rfh')
plt.figure(figsize=(12, 8))
im = plt.imshow(pivot_cv.values, aspect='auto', cmap='RdYlBu_r')
plt.colorbar(im, label='Coefficient of Variation (%)')
plt.xticks(range(len(pivot_cv.columns)), pivot_cv.columns)
plt.yticks(range(len(pivot_cv.index)), pivot_cv.index)
plt.title('Rainfall Variability (CV%) by Province and Month')
plt.xlabel('Month')
plt.ylabel('Province')
plt.show()

# SEASONAL TOTALS

seasonal = (
    df_classified.groupby(['province', 'season'])['rfh']
    .sum()
    .reset_index()
    .rename(columns={'rfh': 'seasonal_total_mm'})
)

df_classified['Wet_Month'] = df_classified['rfh'] > 50
wet_counts = df_classified.groupby(['province', 'year'])['Wet_Month'].sum().reset_index()
wet_counts_avg = wet_counts.groupby('province')['Wet_Month'].mean().round(1).sort_values(ascending=False)
print("\n AVERAGE NUMBER OF WET MONTHS PER YEAR (>50mm) ")
print(wet_counts_avg)

print("\n TYPICAL WET SEASON PATTERNS ")
for province in sorted([p for p in provinces if p != 'Muchinga']):
    province_data = df_classified[df_classified['province'] == province]
    wet_prob = province_data.groupby('month')['Wet_Month'].mean() * 100
    wet_months = wet_prob[wet_prob > 50].index.tolist()
    if wet_months:
        print(f"{province:15s}: Wet season months: {wet_months}")
    else:
        print(f"{province:15s}: No clear wet season pattern")

# Time series for key provinces
key_provinces = ['Lusaka', 'Northern', 'Western', 'Luapula', 'Southern']
key_provinces = [p for p in key_provinces if p in provinces]

if key_provinces:
    fig, axes = plt.subplots(len(key_provinces), 1, figsize=(14, 3 * len(key_provinces)))
    if len(key_provinces) == 1:
        axes = [axes]

    for idx, province in enumerate(key_provinces):
        province_data = df_classified[df_classified['province'] == province].copy()
        province_data['Date'] = pd.to_datetime(
            province_data['year'].astype(str) + '-' + province_data['month'].astype(str), format='%Y-%m')
        province_data = province_data.sort_values('Date')
        axes[idx].plot(province_data['Date'], province_data['rfh'], color='steelblue', alpha=0.7, linewidth=1)
        axes[idx].axhline(y=50, color='orange', linestyle='--', alpha=0.5, linewidth=1)
        colors = {'Low': 'lightcoral', 'Normal': 'lightgreen', 'High': 'lightblue'}
        for i, row in province_data.iterrows():
            if i < len(province_data) - 1:
                axes[idx].axvspan(row['Date'], province_data.iloc[i+1]['Date'],
                                  alpha=0.2, color=colors.get(row['rainfall_class_monthly'], 'white'), zorder=0)
        axes[idx].set_title(f'{province} - Monthly Rainfall (1981-2024)', fontsize=12)
        axes[idx].set_ylabel('rfh (mm)')
        axes[idx].grid(True, alpha=0.3)
        axes[idx].set_xlim(province_data['Date'].min(), province_data['Date'].max())
    plt.tight_layout()
    plt.show()

# Summary
print("\n SUMMARY STATISTICS BY PROVINCE \n")
summary_by_province = df_classified[df_classified['province'] != 'Muchinga'].groupby('province').agg({
    'rfh': ['mean', 'std', 'min', 'max'],
    'rainfall_class_monthly': lambda x: (x == 'Low').sum() / len(x) * 100
}).round(2)
summary_by_province.columns = ['rfh_mean', 'rfh_std', 'rfh_min', 'rfh_max', 'pct_low']
summary_by_province = summary_by_province.sort_values('rfh_mean', ascending=False)
print(summary_by_province)

print("\n EXPLORATION COMPLETE!")
print(f"\nKey observations from the data:")
print(f"• Months: {list(monthly_stats.index)}")
print(f"• Wettest month average: {monthly_stats['mean'].max():.1f} mm (Month {monthly_stats['mean'].idxmax()})")
print(f"• Driest month average: {monthly_stats['mean'].min():.1f} mm (Month {monthly_stats['mean'].idxmin()})")

# OCTOBER RAINFALL ANALYSIS BY PROVINCE

october_data = df_classified[df_classified['month'] == 10].copy()

print(" OCTOBER RAINFALL STATISTICS BY PROVINCE \n")
october_stats = october_data.groupby('province')['rfh'].agg(
    ['count', 'mean', 'median', 'std', 'min', 'max']).round(2)
october_stats = october_stats.sort_values('mean', ascending=False)
print(october_stats)

plt.figure(figsize=(14, 8))
october_data.boxplot(column='rfh', by='province', figsize=(14, 8))
plt.title('October Rainfall Distribution by Province', fontsize=14)
plt.suptitle('')
plt.xlabel('Province', fontsize=12)
plt.ylabel('October Rainfall (mm)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 8))
sorted_provinces = october_stats.index.tolist()
means = october_stats['mean'].values
stds = october_stats['std'].values
colors = plt.cm.Blues(means / means.max())
bars = plt.bar(range(len(sorted_provinces)), means, yerr=stds,
               capsize=5, alpha=0.8, edgecolor='black')
plt.xticks(range(len(sorted_provinces)), sorted_provinces, rotation=45, ha='right')
plt.xlabel('Province', fontsize=12)
plt.ylabel('Mean October Rainfall (mm)', fontsize=12)
plt.title('Average October Rainfall by Province (±1 Std Dev)', fontsize=14)
plt.grid(True, alpha=0.3, axis='y')
for i, (province, mean_val) in enumerate(zip(sorted_provinces, means)):
    plt.text(i, mean_val + 2, f'{mean_val:.1f}', ha='center', fontsize=9)
plt.tight_layout()
plt.show()

key_provinces = ['Luapula', 'Northern', 'North-Western', 'Lusaka', 'Southern', 'Western']
october_key = october_data[october_data['province'].isin(key_provinces)]
plt.figure(figsize=(15, 8))
for province in key_provinces:
    province_data = october_key[october_key['province'] == province]
    plt.plot(province_data['year'], province_data['rfh'],
             marker='o', markersize=4, linewidth=1.5, alpha=0.7, label=f'{province}')
plt.xlabel('Year', fontsize=12)
plt.ylabel('October Rainfall (mm)', fontsize=12)
plt.title('October Rainfall Trends by Province (1981-2024)', fontsize=14)
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

october_low = np.percentile(october_data['rfh'], 30)
october_high = np.percentile(october_data['rfh'], 70)
october_data['october_class'] = 'Normal'
october_data.loc[october_data['rfh'] < october_low, 'october_class'] = 'Low'
october_data.loc[october_data['rfh'] > october_high, 'october_class'] = 'High'

october_class_summary = pd.crosstab(october_data['province'], october_data['october_class'])
october_class_pct = october_class_summary.div(october_class_summary.sum(axis=1), axis=0) * 100
print("\n OCTOBER RAINFALL CLASSIFICATION (% of years) \n")
print(october_class_pct.round(1))

fig, ax = plt.subplots(figsize=(12, 6))
october_class_pct.sort_values('High', ascending=False).plot(
    kind='bar', stacked=True, ax=ax, color=['red', 'green', 'blue'], alpha=0.7)
ax.set_title('October Rainfall Classification by Province', fontsize=14)
ax.set_xlabel('Province', fontsize=12)
ax.set_ylabel('Percentage of Years (%)', fontsize=12)
ax.legend(title='October Rainfall Class')
ax.grid(True, alpha=0.3, axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

october_pivot = october_data.pivot_table(values='rfh', index='year', columns='province', aggfunc='mean')
plt.figure(figsize=(14, 10))
im = plt.imshow(october_pivot.values, aspect='auto', cmap='YlOrRd')
plt.colorbar(im, label='October Rainfall (mm)')
plt.xticks(range(len(october_pivot.columns)), october_pivot.columns, rotation=45, ha='right')
plt.yticks(range(0, len(october_pivot.index), 5), october_pivot.index[::5])
plt.xlabel('Province', fontsize=12)
plt.ylabel('Year', fontsize=12)
plt.title('October Rainfall Heatmap (1981-2024)', fontsize=14)
plt.tight_layout()
plt.show()

print("\n EXTREME OCTOBER RAINFALL YEARS \n")
for province in sorted(october_data['province'].unique()):
    province_oct = october_data[october_data['province'] == province]
    if len(province_oct) > 0:
        wettest = province_oct.nlargest(3, 'rfh')[['year', 'rfh']]
        driest = province_oct.nsmallest(3, 'rfh')[['year', 'rfh']]
        print(f"\n{province}:")
        print(f"  Wettest Octobers: {', '.join([f'{y} ({r:.1f}mm)' for y, r in zip(wettest['year'], wettest['rfh'])])}")
        print(f"  Driest Octobers:  {', '.join([f'{y} ({r:.1f}mm)' for y, r in zip(driest['year'], driest['rfh'])])}")

october_cv = october_data.groupby('province')['rfh'].agg(
    lambda x: (x.std() / x.mean() * 100) if x.mean() > 0 else 0
).round(1).sort_values(ascending=False)
print("\n OCTOBER RAINFALL VARIABILITY (CV%) \n")
print(october_cv)

plt.figure(figsize=(12, 6))
bars = plt.bar(october_cv.index, october_cv.values, color='coral', alpha=0.7)
plt.axhline(y=october_cv.mean(), color='red', linestyle='--',
            label=f'Average CV = {october_cv.mean():.1f}%')
plt.xlabel('Province', fontsize=12)
plt.ylabel('Coefficient of Variation (%)', fontsize=12)
plt.title('October Rainfall Variability by Province', fontsize=14)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

print("\n SUMMARY: OCTOBER RAINFALL INSIGHTS \n")
wettest_oct = october_stats.iloc[0]
driest_oct = october_stats.iloc[-1]
print(f"Wettest October province: {wettest_oct.name} ({wettest_oct['mean']:.1f} mm average)")
print(f"Driest October province: {driest_oct.name} ({driest_oct['mean']:.1f} mm average)")
print(f"National October average: {october_stats['mean'].mean():.1f} mm")
print(f"Most variable October: {october_cv.index[0]} (CV = {october_cv.iloc[0]:.1f}%)")
print(f"Least variable October: {october_cv.index[-1]} (CV = {october_cv.iloc[-1]:.1f}%)")

summary_october = pd.DataFrame({
    'Mean (mm)': october_stats['mean'],
    'CV (%)': october_cv,
    '% Low Octobers': october_class_pct['Low'],
    '% High Octobers': october_class_pct['High']
}).round(1)
print("\n=== DETAILED OCTOBER SUMMARY ===\n")
print(summary_october.sort_values('Mean (mm)', ascending=False))

# OCTOBER TREND ANALYSIS

october_data = df_classified[df_classified['month'] == 10].copy()
october_data['Decade'] = pd.cut(october_data['year'],
                                 bins=[1980, 1990, 2000, 2010, 2020, 2030],
                                 labels=['1980s', '1990s', '2000s', '2010s', '2020s'])

decade_stats = october_data.groupby(['province', 'Decade'])['rfh'].agg(
    ['mean', 'std', 'count']).round(2).reset_index()

print("=== OCTOBER RAINFALL BY DECADE ===\n")
for province in sorted(october_data['province'].unique()):
    province_decade = decade_stats[decade_stats['province'] == province]
    if len(province_decade) > 0:
        print(f"\n{province}:")
        for _, row in province_decade.iterrows():
            print(f"  {row['Decade']}: {row['mean']:.1f} mm (±{row['std']:.1f})")

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

national_october = october_data.groupby('year')['rfh'].mean().reset_index()
axes[0,0].plot(national_october['year'], national_october['rfh'],
               marker='o', markersize=4, linewidth=1.5, color='blue', alpha=0.7)
z = np.polyfit(national_october['year'], national_october['rfh'], 1)
p = np.poly1d(z)
axes[0,0].plot(national_october['year'], p(national_october['year']),
               color='red', linestyle='--', linewidth=2,
               label=f'Trend: {z[0]:.2f} mm/year')
axes[0,0].axhline(y=national_october['rfh'].mean(), color='gray', linestyle=':', alpha=0.5)
axes[0,0].set_xlabel('Year')
axes[0,0].set_ylabel('National Average October Rainfall (mm)')
axes[0,0].set_title('National October Rainfall Trend (1981-2024)')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)

rolling_avg = national_october.set_index('year')['rfh'].rolling(window=10, center=True).mean()
axes[0,1].plot(national_october['year'], national_october['rfh'],
               color='lightblue', alpha=0.5, linewidth=1, label='Annual')
axes[0,1].plot(rolling_avg.index, rolling_avg.values,
               color='darkblue', linewidth=2, label='10-Year Rolling Average')
axes[0,1].set_xlabel('Year')
axes[0,1].set_ylabel('National Average October Rainfall (mm)')
axes[0,1].set_title('October Rainfall: 10-Year Rolling Average')
axes[0,1].legend()
axes[0,1].grid(True, alpha=0.3)

key_provinces = ['Lusaka', 'Southern', 'Luapula', 'Northern']
colors_map = {'Lusaka': 'red', 'Southern': 'orange', 'Luapula': 'green', 'Northern': 'blue'}
for province in key_provinces:
    province_data = october_data[october_data['province'] == province]
    province_annual = province_data.groupby('year')['rfh'].mean().reset_index()
    axes[1,0].plot(province_annual['year'], province_annual['rfh'],
                   marker='o', markersize=3, linewidth=1, alpha=0.6,
                   label=province, color=colors_map[province])
    z = np.polyfit(province_annual['year'], province_annual['rfh'], 1)
    p = np.poly1d(z)
    axes[1,0].plot(province_annual['year'], p(province_annual['year']),
                   linestyle='--', linewidth=2, color=colors_map[province],
                   label=f'{province} trend ({z[0]:.1f} mm/yr)')
axes[1,0].set_xlabel('Year')
axes[1,0].set_ylabel('October Rainfall (mm)')
axes[1,0].set_title('October Rainfall Trends by Province')
axes[1,0].legend(loc='upper right', fontsize=8)
axes[1,0].grid(True, alpha=0.3)

october_data['Period'] = october_data['year'].apply(lambda x: '1981-2000' if x <= 2000 else '2001-2024')
period_comparison = october_data.groupby(['province', 'Period'])['rfh'].mean().unstack()
period_comparison['Change'] = period_comparison['2001-2024'] - period_comparison['1981-2000']
period_comparison = period_comparison.sort_values('Change')
change_colors = ['red' if x < 0 else 'green' for x in period_comparison['Change']]
axes[1,1].barh(period_comparison.index, period_comparison['Change'], color=change_colors, alpha=0.7)
axes[1,1].axvline(x=0, color='black', linewidth=1)
axes[1,1].set_xlabel('Change in October Rainfall (mm)')
axes[1,1].set_title('Change in October Rainfall: 2001-2024 vs 1981-2000')
axes[1,1].grid(True, alpha=0.3, axis='x')
for i, (province, change) in enumerate(period_comparison['Change'].items()):
    axes[1,1].text(change + (0.5 if change >= 0 else -0.5), i,
                   f'{change:+.1f} mm', va='center', fontsize=9)
plt.tight_layout()
plt.show()

from scipy import stats

print("\n STATISTICAL ANALYSIS: OCTOBER RAINFALL CHANGE \n")
for province in key_provinces:
    province_data = october_data[october_data['province'] == province]
    before = province_data[province_data['year'] <= 2000]['rfh']
    after = province_data[province_data['year'] > 2000]['rfh']
    if len(before) > 5 and len(after) > 5:
        t_stat, p_value = stats.ttest_ind(before, after)
        mean_change = after.mean() - before.mean()
        print(f"\n{province}:")
        print(f"  1981-2000 mean: {before.mean():.1f} mm")
        print(f"  2001-2024 mean: {after.mean():.1f} mm")
        print(f"  Change: {mean_change:+.1f} mm ({mean_change/before.mean()*100:+.1f}%)")
        print(f"  p-value: {p_value:.4f} {'(SIGNIFICANT)' if p_value < 0.05 else '(not significant)'}")

print("\n LINEAR TREND ANALYSIS (mm/year) \n")
trend_results = []
for province in sorted(october_data['province'].unique()):
    province_data = october_data[october_data['province'] == province]
    province_annual = province_data.groupby('year')['rfh'].mean().reset_index()
    if len(province_annual) > 10:
        slope, intercept, r_value, p_value, std_err = stats.linregress(
            province_annual['year'], province_annual['rfh'])
        trend_results.append({
            'Province': province,
            'Trend_mm_per_year': slope,
            'R_squared': r_value**2,
            'P_value': p_value,
            'Significant': p_value < 0.05
        })
        print(f"{province:15s}: {slope:+.2f} mm/year  (R²={r_value**2:.3f}, p={p_value:.4f})")

trend_df = pd.DataFrame(trend_results).sort_values('Trend_mm_per_year')
plt.figure(figsize=(12, 6))
colors = ['red' if x < 0 else 'green' for x in trend_df['Trend_mm_per_year']]
plt.barh(trend_df['Province'], trend_df['Trend_mm_per_year'], color=colors, alpha=0.7)
plt.axvline(x=0, color='black', linewidth=1)
plt.xlabel('Trend (mm/year)')
plt.title('October Rainfall Trends by Province')
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

print("\n DETECTING SHIFT IN OCTOBER RAINFALL \n")
for province in key_provinces:
    province_data = october_data[october_data['province'] == province]
    province_annual = province_data.groupby('year')['rfh'].mean().reset_index()
    province_annual = province_annual.sort_values('year')
    mean_val = province_annual['rfh'].mean()
    province_annual['cum_dev'] = (province_annual['rfh'] - mean_val).cumsum()
    max_dev_year = province_annual.loc[province_annual['cum_dev'].idxmax(), 'year']
    plt.figure(figsize=(10, 4))
    plt.plot(province_annual['year'], province_annual['cum_dev'], marker='o', markersize=3)
    plt.axvline(x=max_dev_year, color='red', linestyle='--', label=f'Shift point: ~{max_dev_year}')
    plt.xlabel('Year')
    plt.ylabel('Cumulative Deviation from Mean')
    plt.title(f'{province}: October Rainfall Shift Detection')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
    print(f"{province}: Most likely shift around {max_dev_year}")

october_data['Low_October'] = october_data['rfh'] < 70
low_frequency = october_data.groupby(['province', 'Decade'])['Low_October'].mean() * 100
low_frequency = low_frequency.reset_index()
low_pivot = low_frequency.pivot(index='province', columns='Decade', values='Low_October')

plt.figure(figsize=(12, 8))
im = plt.imshow(low_pivot.values, aspect='auto', cmap='YlOrRd', vmin=0, vmax=100)
plt.colorbar(im, label='% of Years with Low October Rain (<70mm)')
plt.xticks(range(len(low_pivot.columns)), low_pivot.columns)
plt.yticks(range(len(low_pivot.index)), low_pivot.index)
plt.title('Frequency of Low October Rainfall by Decade', fontsize=14)
plt.xlabel('Decade')
plt.ylabel('Province')
for i in range(len(low_pivot.index)):
    for j in range(len(low_pivot.columns)):
        if not pd.isna(low_pivot.iloc[i, j]):
            plt.text(j, i, f'{low_pivot.iloc[i, j]:.0f}%',
                    ha='center', va='center',
                    color='white' if low_pivot.iloc[i, j] > 50 else 'black')
plt.tight_layout()
plt.show()

print("\n LOW OCTOBER RAIN FREQUENCY (%) \n")
print(low_pivot.round(1))

print("\n SUMMARY: OCTOBER RAINFALL SHIFT \n")
overall_before = october_data[october_data['year'] <= 2000]['rfh'].mean()
overall_after = october_data[october_data['year'] > 2000]['rfh'].mean()
print(f"NATIONAL OCTOBER RAINFALL:")
print(f"  1981-2000 average: {overall_before:.1f} mm")
print(f"  2001-2024 average: {overall_after:.1f} mm")
print(f"  CHANGE: {overall_after - overall_before:+.1f} mm ({(overall_after - overall_before)/overall_before*100:+.1f}%)")

print("\nPROVINCES WITH SIGNIFICANT DECLINE:")
declining = trend_df[trend_df['Trend_mm_per_year'] < -0.5]
for _, row in declining.iterrows():
    print(f"  {row['Province']}: {row['Trend_mm_per_year']:.2f} mm/year decline (p={row['P_value']:.3f})")

print("\nPROVINCES WITH INCREASING OCTOBER RAIN:")
increasing = trend_df[trend_df['Trend_mm_per_year'] > 0.5]
for _, row in increasing.iterrows():
    print(f"  {row['Province']}: {row['Trend_mm_per_year']:.2f} mm/year increase (p={row['P_value']:.3f})")

print("\nCRITICAL INSIGHT:")
print("If October rainfall has declined, the traditional planting window may no longer be reliable.")
print("Farmers may need to:")
print("  • Delay planting until November/December")
print("  • Use drought-tolerant varieties")
print("  • Consider supplemental irrigation for early season")

# MEAN TOTAL SEASONAL RAINFALL PER PROVINCE (1981-2024)

mean_seasonal = (
    seasonal.groupby('province')['seasonal_total_mm']
    .agg(Seasons='count', Mean_mm='mean', Median_mm='median',
         Std_mm='std', Min_mm='min', Max_mm='max')
    .round(1)
    .sort_values('Mean_mm', ascending=False)
    .reset_index()
)

print("\n" + "=" * 68)
print("  MEAN TOTAL SEASONAL RAINFALL BY PROVINCE — 1981–2024 (44 Seasons)")
print("=" * 68)
print(mean_seasonal.to_string(index=False))
print(f"\nNational mean: {mean_seasonal['Mean_mm'].mean():.1f} mm")

fig, axes = plt.subplots(1, 2, figsize=(16, 6))
colors = plt.cm.Blues(mean_seasonal['Mean_mm'] / mean_seasonal['Mean_mm'].max())
bars = axes[0].bar(mean_seasonal['province'], mean_seasonal['Mean_mm'],
                   yerr=mean_seasonal['Std_mm'], capsize=5,
                   color=colors, edgecolor='black', alpha=0.85)
national_mean = mean_seasonal['Mean_mm'].mean()
axes[0].axhline(y=national_mean, color='red', linestyle='--', linewidth=1.5,
                label=f'National Mean = {national_mean:.1f} mm')
for bar, val in zip(bars, mean_seasonal['Mean_mm']):
    axes[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10,
                 f'{val:.0f}', ha='center', fontsize=9)
axes[0].set_title('Mean Total Seasonal Rainfall by Province\n(1981–2024, 44 Seasons)', fontsize=13)
axes[0].set_xlabel('Province')
axes[0].set_ylabel('Mean Seasonal Rainfall (mm)')
axes[0].set_xticklabels(mean_seasonal['province'], rotation=45, ha='right')
axes[0].legend()
axes[0].grid(True, alpha=0.3, axis='y')

for province in mean_seasonal['province']:
    pdata = seasonal[seasonal['province'] == province].sort_values('season')
    axes[1].plot(pdata['season'], pdata['seasonal_total_mm'],
                 alpha=0.6, linewidth=1.2, label=province)
axes[1].set_title('Seasonal Rainfall Over Time by Province\n(1981–2024)', fontsize=13)
axes[1].set_xlabel('Season (start year)')
axes[1].set_ylabel('Total Seasonal Rainfall (mm)')
axes[1].legend(fontsize=8, loc='upper right')
axes[1].grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# MEAN TOTAL SEASONAL RAINFALL PER PROVINCE (1981–2024)

# Step 1: Assign season label to every row
def assign_season(row):
    return row['year'] if row['month'] in [10, 11, 12] else row['year'] - 1

df['season'] = df.apply(assign_season, axis=1)

# Step 2: Sum ALL rows (3 pixels × 6 months) per province per season
seasonal = (
    df.groupby(['province', 'season'])['rfh']
    .sum()
    .reset_index()
    .rename(columns={'rfh': 'seasonal_total_mm'})
)

# Step 3: Drop incomplete boundary seasons
# Season 1980: missing Oct/Nov/Dec 1980 (data starts Jan 1981)
# Season 2025: missing Mar 2026
seasonal = seasonal[seasonal['season'].between(1981, 2024)]

print(f"Seasons: {seasonal['season'].min()} – {seasonal['season'].max()} "
      f"({seasonal['season'].nunique()} complete seasons)\n")

# Step 4: Mean seasonal total per province across 44 seasons
mean_seasonal = (
    seasonal.groupby('province')['seasonal_total_mm']
    .agg(Seasons='count', Mean_mm='mean', Median_mm='median',
         Std_mm='std', Min_mm='min', Max_mm='max')
    .round(1)
    .sort_values('Mean_mm', ascending=False)
    .reset_index()
)

print("=" * 68)
print("  MEAN TOTAL SEASONAL RAINFALL BY PROVINCE — 1981–2024 (44 Seasons)")
print("=" * 68)
print(mean_seasonal.to_string(index=False))
print(f"\nNational mean: {mean_seasonal['Mean_mm'].mean():.1f} mm")

# ── Charts ─────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Left: mean ± std bar chart
colors = plt.cm.Blues(mean_seasonal['Mean_mm'] / mean_seasonal['Mean_mm'].max())
bars = axes[0].bar(mean_seasonal['province'], mean_seasonal['Mean_mm'],
                   yerr=mean_seasonal['Std_mm'], capsize=5,
                   color=colors, edgecolor='black', alpha=0.85)

national_mean = mean_seasonal['Mean_mm'].mean()
axes[0].axhline(y=national_mean, color='red', linestyle='--', linewidth=1.5,
                label=f'National Mean = {national_mean:.1f} mm')

for bar, val in zip(bars, mean_seasonal['Mean_mm']):
    axes[0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10,
                 f'{val:.0f}', ha='center', fontsize=9)

axes[0].set_title('Mean Total Seasonal Rainfall by Province\n(1981–2024, 44 Seasons)', fontsize=13)
axes[0].set_xlabel('Province')
axes[0].set_ylabel('Mean Seasonal Rainfall (mm)')
axes[0].set_xticklabels(mean_seasonal['province'], rotation=45, ha='right')
axes[0].legend()
axes[0].grid(True, alpha=0.3, axis='y')

# Right: time series per province
for province in mean_seasonal['province']:
    pdata = seasonal[seasonal['province'] == province].sort_values('season')
    axes[1].plot(pdata['season'], pdata['seasonal_total_mm'],
                 alpha=0.6, linewidth=1.2, label=province)

axes[1].set_title('Seasonal Rainfall Over Time by Province\n(1981–2024)', fontsize=13)
axes[1].set_xlabel('Season (start year)')
axes[1].set_ylabel('Total Seasonal Rainfall (mm)')
axes[1].legend(fontsize=8, loc='upper right')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
