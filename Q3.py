# Importing The Libraries.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# The Question We Are Asking Is If There Is A Correlation Between Life And GDP.

# Reads The CSV File.
df = pd.read_csv('all_data.csv')

# Rename The Column Of Life Expectancy
df = df.rename({"Life expectancy at birth (years)":"LEABY"}, axis = "columns")

# Creates A DataFrame For All Countries
china_df = df[df['Country'] == 'China'].copy()
chile_df = df[df['Country'] == 'Chile'].copy()
germany_df = df[df['Country'] == 'Germany'].copy()
mexico_df = df[df['Country'] == 'Mexico'].copy()
zimbabwe_df = df[df['Country'] == 'Zimbabwe'].copy()
usa_df = df[df['Country'] == 'United States of America'].copy()

# Converts All Age Floats Into Integers
china_df['LEABY'] = china_df['LEABY'].astype(int)
chile_df['LEABY'] = chile_df['LEABY'].astype(int)
germany_df['LEABY'] = germany_df['LEABY'].astype(int)
mexico_df['LEABY'] = mexico_df['LEABY'].astype(int)
zimbabwe_df['LEABY'] = zimbabwe_df['LEABY'].astype(int)
usa_df['LEABY'] = usa_df['LEABY'].astype(int)

# Create Six Scatterplots In A Single Figure To Analyze The Trend.
plt.figure()

# China Scatter
plt.subplot(2, 3, 1)
plt.scatter(china_df['GDP'] / 1_000_000_000, china_df['LEABY'], color='#0072B2')
plt.ylabel('Life Expectancy')
plt.title('China GDP vs Life Expectancy')

# Chile Scatter
plt.subplot(2, 3, 2)
plt.scatter(chile_df['GDP'] / 1_000_000_000, chile_df['LEABY'], color='#E69F00')
plt.xlabel('GDP (In Billions)')
plt.ylabel('Life Expectancy')
plt.title('Chile GDP vs Life Expectancy')

# Germany Scatter
plt.subplot(2, 3, 3)
plt.scatter(germany_df['GDP'] / 1_000_000_000, germany_df['LEABY'], color='#56B4E9')
plt.xlabel('GDP (In Billions)')
plt.ylabel('Life Expectancy')
plt.title('Germany GDP vs Life Expectancy')

# Mexico Scatter
plt.subplot(2, 3, 4)
plt.scatter(mexico_df['GDP'] / 1_000_000_000, mexico_df['LEABY'], color='#009E73')
plt.xlabel('GDP (In Billions)')
plt.ylabel('Life Expectancy')
plt.title('Mexico GDP vs Life Expectancy')

# Zimbabwe Scatter
plt.subplot(2, 3, 5)
plt.scatter(zimbabwe_df['GDP'] / 1_000_000_000, zimbabwe_df['LEABY'], color="#01413D")
plt.xlabel('GDP (In Billions)')
plt.ylabel('Life Expectancy')
plt.title('Zimbabwe GDP vs Life Expectancy')

# USA Scatter
plt.subplot(2, 3, 6)
plt.scatter(usa_df['GDP'] / 1_000_000_000, usa_df['LEABY'], color="#904308")
plt.xlabel('GDP (In Billions)')
plt.ylabel('Life Expectancy')
plt.title('USA GDP vs Life Expectancy')
plt.show()