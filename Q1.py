# Importing The Libraries.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# The Question We Are Asking Is If There Is A Correlation Between Life And GDP.

# First Lets Look At Country's Individual GDP's In Comparison To One Another.

# Reads The CSV File.
df = pd.read_csv('all_data.csv')

# Creates A DataFrame For All Countries
china_df = df[df['Country'] == 'China']
chile_df = df[df['Country'] == 'Chile']
germany_df = df[df['Country'] == 'Germany']
mexico_df = df[df['Country'] == 'Mexico']
zimbabwe_df = df[df['Country'] == 'Zimbabwe']
usa_df = df[df['Country'] == 'United States of America']

# Plot Individual Countries On The Graph.
plt.plot(china_df['Year'], china_df['Life expectancy at birth (years)'], color='#0072B2')
plt.plot(chile_df['Year'], chile_df['Life expectancy at birth (years)'], color='#E69F00')
plt.plot(germany_df['Year'], germany_df['Life expectancy at birth (years)'], color='#56B4E9')
plt.plot(mexico_df['Year'], mexico_df['Life expectancy at birth (years)'], color='#009E73')
plt.plot(zimbabwe_df['Year'], zimbabwe_df['Life expectancy at birth (years)'], color="#01413D")
plt.plot(usa_df['Year'], usa_df['Life expectancy at birth (years)'], color="#904308")

# Label The Graph
plt.xlabel('Years')
plt.ylabel('Life Expectancy')
plt.title('Life Expectancy Over The Years')
plt.legend(['CHNA', 'CHL', 'GMNY', 'MXCO', 'ZMBWE', 'USA'], loc='center left', bbox_to_anchor=(1, 0.5))

# Display The Graph
plt.show()


# Calculate The Mean Of All Country's GDP.
china_mean = np.mean(china_df['GDP']) / 1_000_000_000
chile_mean = np.mean(chile_df['GDP']) / 1_000_000_000
germany_mean = np.mean(germany_df['GDP']) / 1_000_000_000
mexico_mean = np.mean(mexico_df['GDP']) / 1_000_000_000
zimbabwe_mean = np.mean(zimbabwe_df['GDP']) / 1_000_000_000
usa_mean = np.mean(usa_df['GDP']) / 1_000_000_000

# Plot A Bar Chart To Show
plt.bar(['CHNA', 'CHL', 'GMNY', 'MXCO', 'ZMBWE', 'USA'], [china_mean, chile_mean, germany_mean, mexico_mean, zimbabwe_mean, usa_mean], color=['#0072B2', '#E69F00', '#009E73', '#D55E00', '#F0E442', '#56B4E9'])
plt.xlabel('Country')
plt.ylabel('GDP (Converted To Billions)')
plt.title('GDP Over The Years')
plt.show()



