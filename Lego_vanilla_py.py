# import required libraries

import csv
from collections import Counter

# Read the CSV file to a list of dictionaries
with open('sets.csv', encoding="utf-8") as csvfile:
    data = list(csv.DictReader(csvfile))

# Question 1: How many sets have been released during the year 2000?
num_set_2000 = sum(1 for lego in data if lego['Year'] == "2000")
print(f"There are {num_set_2000} LEGO sets released during the year 2000.")

# Question 2: Which theme has more sets - City or Star Wars?
city_count = sum(1 for lego in data if lego['Theme'] == 'City')
star_wars_count = sum(1 for lego in data if lego['Theme'] == 'Star Wars')
print(f"There are {city_count} LEGO sets with the City theme and {star_wars_count} LEGO sets with the Star Wars theme.")

# Bonus Question 1: What is the average (mean) amount of pieces in a set (excluding sets without pieces)?
total = sum(float(lego['Pieces']) for lego in data if lego.get('Pieces', ''))
count = sum(1 for lego in data if lego.get('Pieces', ''))
avg = total / count if count > 0 else 0  # Avoid division by zero
print(f'Average amount of pieces in a set: {avg}')

# Bonus Question 2: What are the top 10 themes containing the most sets?
theme_counter = Counter()
for lego in data:
    theme = lego['Theme']
    theme_counter[theme] += 1

top_10_themes = theme_counter.most_common(10)
for theme, count in top_10_themes:
    print(f"Theme: {theme}, Number of Sets: {count}")
