import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

# Calculate The Mean Age Of All Countries
china_age_mean = np.mean(china_df['LEABY'])
chile_age_mean = np.mean(chile_df['LEABY'])
germany_age_mean = np.mean(germany_df['LEABY'])
mexico_age_mean = np.mean(mexico_df['LEABY'])
zimbabwe_age_mean = np.mean(zimbabwe_df['LEABY'])
usa_age_mean = np.mean(usa_df['LEABY'])

# Plot Bar Chart To Compare Average Life Expectancies
plt.bar(['CHNA', 'CHLE', 'GRMNY', 'MXCO', 'US', 'ZBW'], [china_age_mean, chile_age_mean, germany_age_mean, mexico_age_mean, usa_age_mean, zimbabwe_age_mean], color=['#0072B2', '#E69F00', '#009E73', '#D55E00', '#F0E442', '#56B4E9'])
plt.xlabel('Countries')
plt.ylabel('Average Life Expectancy (Years)')
plt.title('Average Life Expectancy Over The Years')
plt.show()