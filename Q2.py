# Importing The Libraries.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# The Question We Are Asking Here Is "Has GDP Increased Over Time In The Six Nations"

# Reads The CSV File.
df = pd.read_csv('all_data.csv')

# Creates A DataFrame For All Countries
china_df = df[df['Country'] == 'China']
chile_df = df[df['Country'] == 'Chile']
germany_df = df[df['Country'] == 'Germany']
mexico_df = df[df['Country'] == 'Mexico']
zimbabwe_df = df[df['Country'] == 'Zimbabwe']
usa_df = df[df['Country'] == 'United States of America']

# Plot Individual Countries On Their Own Graph
plt.figure()
plt.subplot(2, 3, 1)
plt.plot(china_df['Year'], china_df['GDP'], color='#0072B2')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.title('China Yearly GDP')
plt.subplot(2, 3, 2)
plt.plot(chile_df['Year'], chile_df['GDP'], color='#E69F00')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.title('Chile Yearly GDP')
plt.subplot(2, 3, 3)
plt.plot(germany_df['Year'], germany_df['GDP'], color='#56B4E9')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.title('Germany Yearly GDP')
plt.subplot(2, 3, 4)
plt.plot(mexico_df['Year'], mexico_df['GDP'], color='#009E73')
plt.xlabel('Years')
plt.ylabel('GDP')
plt.title('Mexico Yearly GDP')
plt.subplot(2, 3, 5)
plt.plot(zimbabwe_df['Year'], zimbabwe_df['GDP'], color="#01413D")
plt.xlabel('Years')
plt.ylabel('GDP')
plt.title('Zimbabwe Yearly GDP')
plt.subplot(2, 3, 6)
plt.plot(usa_df['Year'], usa_df['GDP'], color="#904308")
plt.xlabel('Years')
plt.ylabel('GDP')
plt.title('USA Yearly GDP')
plt.show()
