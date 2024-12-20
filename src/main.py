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


# Affordable Housing Pipeline Dataset

# 1.How many projects are in each project status category?
project_status_counts = affordable_housing_df['Project Status'].value_counts()
# 2.Total number of affordable units per neighborhood
affordable_units_by_neighborhood = affordable_housing_df.groupby('City Analysis Neighborhood')['Affordable Units'].sum()
# 3.Average percentage of affordable units per project
average_affordable_percentage = affordable_housing_df['% Affordable'].mean()

# Craigslist Dataset

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


import matplotlib.pyplot as plt
import seaborn as sns

# Group by Project Status and Neighborhood, summing up Affordable Units
affordable_units_by_status_neighborhood = affordable_housing_df.groupby(['Project Status', 'City Analysis Neighborhood'])['Affordable Units'].sum().unstack()

# Plot stacked bar chart
affordable_units_by_status_neighborhood.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Affordable Units by Project Status and Neighborhood')
plt.xlabel('Project Status')
plt.ylabel('Number of Affordable Units')
plt.legend(title='Neighborhood', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Save the figure
plt.savefig('affordable_units_stacked_bar_chart.png', dpi=300, bbox_inches='tight')

plt.show()

#seaborn


# Group data by Neighborhood and Project Status
trend_data = affordable_housing_df.groupby(['City Analysis Neighborhood', 'Project Status'])['Affordable Units'].sum().reset_index()

# Pivot to create a table suitable for line plot
pivot_data = trend_data.pivot(index='Project Status', columns='City Analysis Neighborhood', values='Affordable Units').fillna(0)

# Plot line chart
plt.figure(figsize=(10, 6))
for column in pivot_data.columns:
    plt.plot(pivot_data.index, pivot_data[column], marker='o', label=column)

plt.title('Trend of Affordable Units by Project Status Across Neighborhoods')
plt.xlabel('Project Status')
plt.ylabel('Number of Affordable Units')
plt.legend(title='Neighborhood', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('trend_affordable_units_line_chart.png', dpi=300, bbox_inches='tight')
plt.show()