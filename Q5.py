import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# The Question We Are Asking Here Is "What Is The Average Life Expectancy Across All Six Nations?"

# Reads The CSV File.
df = pd.read_csv('all_data.csv')

# Rename The Column Of Life Expectancy At Birth (Years)
df = df.rename({"Life expectancy at birth (years)":"LEABY"}, axis = "columns")

# Creates A DataFrame For All Countries
china_df = df[df['Country'] == 'China']
chile_df = df[df['Country'] == 'Chile']
germany_df = df[df['Country'] == 'Germany']
mexico_df = df[df['Country'] == 'Mexico']
zimbabwe_df = df[df['Country'] == 'Zimbabwe']
usa_df = df[df['Country'] == 'United States of America']

# Converts The Ages In China Dataframe To Integers
china_df['LEABY'] = china_df['LEABY'].astype(int)
chile_df['LEABY'] = chile_df['LEABY'].astype(int)
germany_df['LEABY'] = germany_df['LEABY'].astype(int)
mexico_df['LEABY'] = mexico_df['LEABY'].astype(int)
zimbabwe_df['LEABY'] = zimbabwe_df['LEABY'].astype(int)
usa_df['LEABY'] = usa_df['LEABY'].astype(int)

# Create Histogram For Each Country In The Figure.
plt.figure()
plt.subplot(2, 3, 1)
sns.histplot(china_df['LEABY'], bins=range(min(china_df['LEABY']), max(china_df['LEABY']) + 1), discrete=True, color='#0072B2')
plt.xlabel('Life Expectancy (Years)')
plt.ylabel('Frequency')
plt.title('China Life Expectancy Spread')

plt.subplot(2, 3, 2)
sns.histplot(chile_df['LEABY'], bins=range(min(chile_df['LEABY']), max(chile_df['LEABY']) + 1), discrete=True, color='#E69F00')
plt.xlabel('Life Expectancy (Years)')
plt.ylabel('Frequency')
plt.xticks(range(min(chile_df['LEABY']), max(chile_df['LEABY']) + 1))
plt.title('Chile Life Expectancy Spread')

plt.subplot(2, 3, 3)
sns.histplot(germany_df['LEABY'], bins=range(min(germany_df['LEABY']), max(germany_df['LEABY']) + 1), discrete=True, color='#56B4E9')
plt.xlabel('Life Expectancy (Years)')
plt.ylabel('Frequency')
plt.xticks(range(min(germany_df['LEABY']), max(germany_df['LEABY']) + 1))
plt.title('Germany Life Expectancy Spread')

plt.subplot(2, 3, 4)
sns.histplot(mexico_df['LEABY'], bins=range(min(mexico_df['LEABY']), max(mexico_df['LEABY']) + 1), discrete=True, color='#009E73')
plt.xlabel('Life Expectancy (Years)')
plt.ylabel('Frequency')
plt.xticks(range(min(mexico_df['LEABY']), max(mexico_df['LEABY']) + 1))
plt.title('Mexico Life Expectancy Spread')

plt.subplot(2, 3, 5)
sns.histplot(zimbabwe_df['LEABY'], bins=range(min(zimbabwe_df['LEABY']), max(zimbabwe_df['LEABY']) + 1), discrete=True, color="#01413D")
plt.xlabel('Life Expectancy (Years)')
plt.ylabel('Frequency')
plt.xticks(sorted(zimbabwe_df['LEABY'].unique()))
plt.title('Zimbabwe Life Expectancy Spread')

plt.subplot(2, 3, 6)
sns.histplot(usa_df['LEABY'], bins=range(min(usa_df['LEABY']), max(usa_df['LEABY']) + 1), discrete=True, color="#904308")
plt.xlabel('Life Expectancy (Years)')
plt.ylabel('Frequency')
plt.xticks(range(min(usa_df['LEABY']), max(usa_df['LEABY']) + 1))
plt.title('USA Life Expectancy Spread')

plt.show()

# Calculate The Standard Deviation Of All Countries
print("China Standard Deviation:", china_df['LEABY'].std())
print("Chile Standard Deviation:", chile_df['LEABY'].std())
print("Germany Standard Deviation:", germany_df['LEABY'].std())
print("Mexico Standard Deviation:", mexico_df['LEABY'].std())
print("Zimbabwe Standard Deviation:", zimbabwe_df['LEABY'].std())
print("USA Standard Deviation:", usa_df['LEABY'].std())

# Calculate The Mean Of All Countries
print("China Mean:", china_df['LEABY'].mean())
print("Chile Mean:", chile_df['LEABY'].mean())
print("Germany Mean:", germany_df['LEABY'].mean())
print("Mexico Mean:", mexico_df['LEABY'].mean())
print("Zimbabwe Mean:", zimbabwe_df['LEABY'].mean())
print("USA Mean:", usa_df['LEABY'].mean())

# Calculate The Median Of All Countries
print("China Median:", china_df['LEABY'].median())
print("Chile Median:", chile_df['LEABY'].median())
print("Germany Median:", germany_df['LEABY'].median())
print("Mexico Median:", mexico_df['LEABY'].median())
print("Zimbabwe Median:", zimbabwe_df['LEABY'].median())
print("USA Median:", usa_df['LEABY'].median())