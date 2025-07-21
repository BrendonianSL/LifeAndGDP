# Project Introduction

Hey everyone! This data analysis project was created to help us find if any comparisons exist between the gross domestic product (GDP) of a country versus the life expectancy the country has. We have several questions that we want to answer throughout the course of the project. There are several questions we are seeking to answer throughout this project.

- Has life expectancy increased over time in the six nations?
- Has GDP increased over time in the six nations?
- Is there a correlation between the GDP and the life expectancy of a country?
- What is the average life expectancies across all nations
- What is the distribution of that life expectancy?

As we answer these questions, we may dive a TINY bit deeper with some numbers to back up some of our answers and predict why certain things are the case. All code for each question is labeled based on the order of the question's displayed above.

```python
# Reads The CSV File.
df = pd.read_csv('all_data.csv')

# Creates A DataFrame For All Countries
china_df = df[df['Country'] == 'China']
chile_df = df[df['Country'] == 'Chile']
germany_df = df[df['Country'] == 'Germany']
mexico_df = df[df['Country'] == 'Mexico']
zimbabwe_df = df[df['Country'] == 'Zimbabwe']
usa_df = df[df['Country'] == 'United States of America']
```

## Question 1: Has Life Expectancy Increased Over Time?
The simple answer to this question is yes! Over time across all nations, we can see a steady increase in life expectancy except for one country, Zimbabwe. Not only that, Zimbabwe starts at a lower point than all the other listed countries.

<img width="1287" height="840" alt="test" src="https://github.com/user-attachments/assets/26b0c678-a753-48ff-b3cd-cdef02559167" />

Why is this the case? This can be attributed to the fact that Zimbabwe has a lower GDP out of all the countries listed. We could display this on a line graph, but a lot of the nuance is lost when doing so. So let's calculate averages
instead. Below is a bar chart that displays average GDP per country. You can visibly see that Zimbabwe is almost non-existent on the chart compared to the other countries. Lower GDP means a lackluster healthcare system, limited education, less infrastructure, and most importantly of all, higher mortality rates. Zimbabwe's Average GDP was nearly $50 Billion
compared to other listed countries whose GDP exceed the trillions like China and the USA which were 4.65 Trillion and 14 Trillion Respectively.
<img width="100%" height="623" alt="image" src="https://github.com/user-attachments/assets/300f8e15-ecb5-4aa8-a991-ea90abc333ea" />

So, we know Zimbabwe has a lower GDP on average by a drastic amount. So how has it's GDP been moving and what was affecting it's rise during the mid 2010s? Zimbabwe's GDP dropped by 17.63% from 2009 to 2010! As a result, Life expectancy actually increased by 1.6 years. This actually goes against our previous assumption that GDP and life 
expectancy are correlated to one another. Around this time, Zimbabwe had printed out more money than was actually needed which caused one of the worst cases of hyperinflation in the world. The government kept printing money as a result of the currency drop. Citizens eventaully started relying on the US dollar and South African rand to survive. Hospitals, 
infrastructure, and food all were in short supply.

## Question 2: Has GDP increased over time in the six nations?
Yes! GDP has actually increased over time in all six nations. However, plotting it all on the same chart can cause issues in determining the amount of increase for other lesser fortunate nations. So the best way to look at this is to view all six nation's increase in seperate plots. However, while the trend has been a steady increase, Chile, Mexico, 
and Germany all experienced a dip at the same time. Let's talk about what happened before analyzing the drops.

<img width="2560" height="1327" alt="Figure_1" src="https://github.com/user-attachments/assets/fea3a4c2-fccc-4134-ace2-c6889e1e9122" />

## Question 3: Is there a correlation between the GDP and the life expectancy of a country?
Here is what we innately know about GDP. The lower the GDP of a country, the lower the quality of living. This results in worse infrastructure, health care, education, etc. A scatterplot would best serve the purpose of discovering this correlation. This question assumes that there will be a positive correlation found between life expectancy and age. When
plotting all six countries on a scatterplot, we can see an increase in all countries the further down the scatter we go. While outliers are present, they aren't consistent enough across all graphs to deny the correlation present.

<img width="2560" height="1327" alt="scatter" src="https://github.com/user-attachments/assets/682e8e87-1bb4-4ddd-bd31-c93c19097a3a" />

## Question 4: What Is The Average Life Expectancies Across All Nations
One of the best ways for us to look at the average life expectancy across all nations is to use a bar graph. We will use this to compare data side by side and this will help us understand the differences between them all. We can see that for 5/6 countries, the average life expectancy is over 70 years! However we once again see Zimbabwea at the lower end of the
spectrum. As discussed earlier, hyperinflation that occured in Zimbabwe during this time played a major role in the life expectancy drop within the country. This results in a lower overall average thanks to lower overall mortality rates.

<img width="2560" height="1327" alt="Figure_1" src="https://github.com/user-attachments/assets/a579b1ec-8f11-41c2-b822-619293e76dfc" />

## Question 5: What Is The Distribution Of That Life Expectancy 
To analyze the distribution, we need to create histograms for each country. This will allow for us to analyze how spread out the ages are and how frequently they show up. The amount of ages shown varies from country to country as not each of them have the same age spread. When looking at the data we can tell the following.

- China's spread is tends to be slightly left skewed, but not by a lot. We can tell this because the median age is 74 while the mean is 73. This results in a left skewed graph with a spread of 1.37 years from the mean on average.
- Chile's spread is approximately symmetrical. Contrary to what is shown on the graph, the mean age is 78 while the median age is also 78. There is a spread of 1.09 years from the mean.
- Germany's spread is also symmetrical with a mean and median of 79. There is a spread of .93 years from the mean.
- Mexico's spread continues this trend with a symmertical skew of 75 for the mean and median. There is a spread of 0.62 years from the mean.
- Zimbabwe's spread is heavily right skewed with a mean of 49 and a median on 47. There is a spread of 5.94 years from the mean. This is a result of the hyperinflation that was mentioned earlier in the article, resulting in a lower mortality rate.
- United States's spread tends to be slightly left skewed with a mean of 77 and a median of 78. The spread is .89 years.

The spreads that are more left skewed shows a higher life expectancy, which is great! More people are living longer! However, those who are right skewed shows a lower life expectancy, which may be reflective of deeper issues within the country. However, the ones that aren't heavily skewed aren't bad by any means. It just communincates the idea that more people
are living closer to the average age which is to be expected!

<img width="2560" height="1327" alt="Q5" src="https://github.com/user-attachments/assets/401e1c85-8895-4c83-9613-39928262a860" />
