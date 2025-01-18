import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Netflix dataset
dataset_path = 'netflix_titles.csv'  # Replace with your dataset path
netflix_data = pd.read_csv(dataset_path)

# Data Cleaning: Handle missing values
netflix_data['country'].fillna('Unknown', inplace=True)
netflix_data['director'].fillna('Unknown', inplace=True)
netflix_data['cast'].fillna('Unknown', inplace=True)
netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'], errors='coerce')

# Insights Preparation
# Distribution of Content Types
content_type_distribution = netflix_data['type'].value_counts()

# Content Over the Years
content_by_year = netflix_data['release_year'].value_counts().sort_index()

# Top Directors
top_directors = netflix_data['director'].value_counts().head(10)

# Top Actors (split and count)
actors = netflix_data['cast'].str.split(',').explode().str.strip()
top_actors = actors.value_counts().head(10)

# Top Countries
top_countries = netflix_data['country'].value_counts().head(10)

# Visualization of Insights
sns.set(style="whitegrid")
plt.figure(figsize=(16, 12))

# 1. Distribution of Content Types
plt.subplot(2, 2, 1)
content_type_distribution.plot(kind='bar', color=['skyblue', 'salmon'], edgecolor='black')
plt.title('Distribution of Content Types', fontsize=14)
plt.xlabel('Type', fontsize=12)
plt.ylabel('Count', fontsize=12)

# 2. Content Over the Years
plt.subplot(2, 2, 2)
content_by_year.plot(kind='line', color='green', marker='o', linestyle='-', linewidth=2)
plt.title('Content Over the Years', fontsize=14)
plt.xlabel('Release Year', fontsize=12)
plt.ylabel('Number of Releases', fontsize=12)

# 3. Top 10 Directors
plt.subplot(2, 2, 3)
top_directors.plot(kind='barh', color='purple', edgecolor='black')
plt.title('Top 10 Directors', fontsize=14)
plt.xlabel('Count', fontsize=12)
plt.ylabel('Director', fontsize=12)

# 4. Top 10 Actors
plt.subplot(2, 2, 4)
top_actors.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Top 10 Actors', fontsize=14)
plt.xlabel('Actor', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Adjust layout
plt.tight_layout()
plt.show()

# 5. Additional Insight: Top 10 Countries
plt.figure(figsize=(10, 6))
top_countries.plot(kind='bar', color='cornflowerblue', edgecolor='black')
plt.title('Top 10 Countries Producing Content', fontsize=14)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
plt.show()
