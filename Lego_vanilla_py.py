import csv

csv_file_path = 'sets.csv'

# Load the entire CSV data into a list of lists
with open(csv_file_path) as file:
    csv_reader = csv.reader(file)
    csv_data = [row for row in csv_reader]

# 1. How many sets have been released during the year 2000?
# Find the index of the 'Year' column
column_headers = csv_data[0]
release_year_index = column_headers.index('Year')

# Count the sets released in the year 2000
sets_in_2000 = sum(1 for row in csv_data[1:] if row[release_year_index] == '2000')

print(f"Number of sets released in 2000: {sets_in_2000}")

# 2. Which theme has more sets - City or Star Wars?
# Find the index of the 'Theme' column
theme_index = column_headers.index('Theme')

# Count the number of rows where 'Theme' is 'City'
city_count = sum(1 for row in csv_data[1:] if row[theme_index] == 'City')
# Count the number of rows where 'Theme' is 'Star Wars'
star_wars_count = sum(1 for row in csv_data[1:] if row[theme_index] == 'Star Wars')
print(f"Number of sets in 'City' theme: {city_count} , Number of sets in 'Star Wars' theme: {star_wars_count}")

# Bonus
# 1. What is the average (mean) amount of pieces in a set (excluding sets without pieces)?
# Find the index of the 'Pieces' column
pieces_index = column_headers.index('Pieces')

# Initialize variables for calculating the average
total_pieces = 0
num_sets_with_pieces = 0

# Iterate over each row
for row in csv_data[1:]:
    pieces_str = row[pieces_index]

    # Check if the 'Pieces' value is not empty
    if pieces_str:
        try:
            # Try converting the 'Pieces' value to a float
            pieces = float(pieces_str)

            # Increment the total pieces and the count of sets with pieces
            total_pieces += pieces
            num_sets_with_pieces += 1
        except ValueError:
            # Handle the case where the conversion to float fails
            print(f"Invalid 'Pieces' value: {pieces_str}")

# Calculate the average (mean) amount of pieces
if num_sets_with_pieces > 0:
    average_pieces = total_pieces / num_sets_with_pieces
    print("Average pieces in a set (excluding sets without pieces):", average_pieces)
else:
    print("No sets with pieces found.")


# 2. What are the top 10 themes containing the most sets?
from collections import Counter
# Initialize a Counter to count the occurrences of each theme
theme_counter = Counter()

# Iterate over each row
for row in csv_data[1:]:
    theme = row[theme_index]

    # Increment the count for the current theme
    theme_counter[theme] += 1

# Print the top 10 themes with the most sets
top_10_themes = theme_counter.most_common(10)
for theme, count in top_10_themes:
    print(f"Theme: {theme}, Number of Sets: {count}")