# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 13:25:21 2025

@author: khanh
"""

import pandas as pd
#---------------------------
# Task 1: Read in data file
#---------------------------
df = pd.read_csv('flag.data', header=None)
columns = [
    'name', 'landmass', 'zone', 'area', 'population', 'language', 'religion', 'bars', 
    'stripes', 'colours', 'red', 'green', 'blue', 'gold', 'white', 'black', 'orange', 
    'mainhue', 'circles', 'crosses', 'saltires', 'quarters', 'sunstars', 'crescent', 
    'triangle', 'icon', 'animate', 'text', 'topleft', 'botright'
]
df.columns = columns

print('*** Task 2 ***')
print('Number of countries in North America: ' + str(df[df['landmass'] == 1].shape[0]))

print('\n*** Task 3 ***')
print('Using explicit loops')
# Initialize a dictionary to store the counts
landmass_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for index, row in df.iterrows():
    landmass = row['landmass']
    landmass_count[landmass] += 1
for land, count in landmass_count.items():
    print(f"{land}    {count}")
print('\nWithout using explicit loops')
landmass_count = df['landmass'].value_counts().sort_index()
print(landmass_count)

print('\n*** Task 4 ***')
# Print out the total population (in millions) of the countries 
# that speaks each language.
language_population = df.groupby('language')['population'].sum().sort_values(ascending=False)
print(language_population)
# Total population (in millions) of the countries that speak each language 
# whose national populations are less than 50 million.
countries_under_50M = (df[df['population'] < 50]).groupby('language')['population'].sum().sort_values(ascending=False)
print("---")
print(countries_under_50M)

# Conclusions:
#   Language 6 (Other Indo-European) is the most widely spoken language
#   Language 7 (Chinese) is not spoken in many countries with less than 50 million people despite having a large total population
#   Language 10 (Others) is more common in smaller countries

print('\n*** Task 5 ***')
sales_reps = pd.DataFrame({'Rep Name': ['Max',  'Jill', 'Fong', 'Juanita', 'Nya'],
                           'Rep Language': [1, 2, 5, 5, 8]})
# Merge sales data with flags data on the language column
merged_df = pd.merge(sales_reps, df.copy(), left_on='Rep Language',  right_on='language', how='inner')
# Count total number of representative countries (double-count if same language is spoken by multiple reps)
representative_countries = merged_df.groupby('name').size().sum()
print(f"Total Representative-Countries: {representative_countries}")

print('\n*** Task 6 ***')
# Group by 'landmass' and 'language' and sum the area
landmass_language_table = df.copy().groupby(['landmass', 'language'])['area'].sum().unstack()
print(landmass_language_table)
# Meaning of NaN: 
#   NaN values indicate that there are no countries in the dataset for that 
#   specific combination of landmass and language. For example, if no countries in a 
#   particular landmass speak a certain language, the total area for that combination 
#   will be NaN.