import pandas as pd

# Load csv into datasets
affordable_housing_path = '../data/affordable-housing-pipeline.csv'
sf_clean_path = '../data/rents_craigslist_clean.csv'

# Read CSV files into dataframes
affordable_housing_df = pd.read_csv(affordable_housing_path)
sf_clean_df = pd.read_csv(sf_clean_path)

#Displays info
affordable_housing_info = affordable_housing_df.info()
sf_clean_info = sf_clean_df.info()

#Preview the first few rows of each dataset
affordable_housing_head = affordable_housing_df.head()
sf_clean_head = sf_clean_df.head()

affordable_housing_info, affordable_housing_head, sf_clean_info, sf_clean_head



#Works!

# 1.How many projects are in each project status category?
project_status_counts = affordable_housing_df['Project Status'].value_counts()

# 2.Total number of affordable units per neighborhood
affordable_units_by_neighborhood = affordable_housing_df.groupby('City Analysis Neighborhood')['Affordable Units'].sum()

# 3.Average percentage of affordable units per project
average_affordable_percentage = affordable_housing_df['% Affordable'].mean()

# 4.Average price per sq ft in sf_clean.csv
average_price_per_sqft = sf_clean_df['price'].mean() / sf_clean_df['sqft'].mean()

# 5.Average price per bedroom by district
avg_price_per_bedroom_by_district = sf_clean_df.groupby('hood_district')['price'].mean() / sf_clean_df.groupby('hood_district')['beds'].mean()

# Display in terminal
print("Project Status Counts:")
print(project_status_counts)

print("\nAffordable Units by Neighborhood:")
print(affordable_units_by_neighborhood)

print("\nAverage Percentage of Affordable Units:")
print(average_affordable_percentage)

print("\nAverage Price per Square Foot:")
print(average_price_per_sqft)

print("\nAverage Price per Bedroom by District:")
print(avg_price_per_bedroom_by_district)
"""