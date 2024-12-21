import pandas as pd

# DATA SOURCE ATTRIBUTION
"""
I use both for the RESEARCH QUESTIONS section.
SF Affordable Housing Pipeline Dataset: https://www.kaggle.com/datasets/san-francisco/sf-affordable-housing-pipeline
Housing Prices in San Francisco (Craigslist): https://www.kaggle.com/datasets/thedevastator/scraping-apartments-off-of-craigslist-in-san-fra

However, the affordable housing one will be the main one analyzed in the  DATA VISUALIZATION and SLIDE DECK.
"""
#load csv into datasets
affordable_housing_path = '../data/affordable-housing-pipeline.csv'#Affordable Housing Pipeline Dataset
sf_clean_path = '../data/rents_craigslist_clean.csv' #Craigslist Dataset

affordable_housing_df = pd.read_csv(affordable_housing_path)
sf_clean_df = pd.read_csv(sf_clean_path)

#Displays info
affordable_housing_info = affordable_housing_df.info()
sf_clean_info = sf_clean_df.info()

#Preview
affordable_housing_head = affordable_housing_df.head()
sf_clean_head = sf_clean_df.head()

affordable_housing_info, affordable_housing_head, sf_clean_info, sf_clean_head





#RESEARCH QUESTIONS
# Affordable Housing Pipeline Dataset

# 1.How many projects are in each project status category?
project_status_counts = affordable_housing_df['Project Status'].value_counts()
# 2.Total number of affordable units per neighborhood
affordable_units_by_neighborhood = affordable_housing_df.groupby('City Analysis Neighborhood')['Affordable Units'].sum()
# 3.Average percentage of affordable units per project
average_affordable_percentage = affordable_housing_df['% Affordable'].mean()

# Craigslist Dataset
# 4.Average price per sqft in sf_clean.csv
average_price_per_sqft = sf_clean_df['price'].mean() / sf_clean_df['sqft'].mean()
# 5.Average price per bedroom by district
avg_price_per_bedroom_by_district = sf_clean_df.groupby('hood_district')['price'].mean() / sf_clean_df.groupby('hood_district')['beds'].mean()

# Displays in terminal
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


# DATA VISUALIZATION
"""
My tool and library of choice is matplot. There is essentially one set of variables 
(Project Status, Neighborhood, sum of Affordable Units) that I am visualizing in two
different plots: a Stacked Bar chart and Line 

P.S. I know dependencies defined not at the top of the program is bad practice, 
but it helps separate my work for grading
"""
import matplotlib.pyplot as plt 

# Group by project status and  neighborhood, summing affordable units
affordable_units_by_status_neighborhood = affordable_housing_df.groupby(['Project Status', 'City Analysis Neighborhood'])['Affordable Units'].sum().unstack()

# Stacked bar chart
affordable_units_by_status_neighborhood.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Affordable Units by Project Status and Neighborhood')
plt.xlabel('Project Status')
plt.ylabel('Number of Affordable Units')
plt.legend(title='Neighborhood', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

#Saves the figure
plt.savefig('affordable_units_stacked_bar_chart.png', dpi=300, bbox_inches='tight')
plt.show()


#Groups by neighborhood and project status
trend_data = affordable_housing_df.groupby(['City Analysis Neighborhood', 'Project Status'])['Affordable Units'].sum().reset_index()
#Creates a table suited for diff plot
pivot_data = trend_data.pivot(index='Project Status', columns='City Analysis Neighborhood', values='Affordable Units').fillna(0)

# Line chart
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