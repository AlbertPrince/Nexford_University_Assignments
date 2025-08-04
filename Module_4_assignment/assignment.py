import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('Netflix_shows_movies.csv')

print("number of missing values in each column:")
print(file.isnull().sum())
print("number of rows in the dataset: ", len(file))

file['director'] = file['director'].fillna('Unknown')

file['cast'] = file['cast'].fillna('Not entered')
file['country'] = file['country'].fillna('Unknown')

file_cleaned = file.dropna(subset=['rating', 'date_added'])

file = file_cleaned
print("number of rows after removing missing values: ", len(file))
print("number of missing values in each column after cleaning:")
print(file.isnull().sum())


print(f'The dataset contains {file.shape[0]} rows and {file.shape[1]} columns.')
print(f"Quick file overview: {file.head()}")
print(f"Column names: {file.columns.tolist()}")
print(f"Data types of each column: {file.dtypes}")
print(f"Random sample of 5 rows:\n{file.sample(5)}")
print(f"Summary of file: {file.info()}")
print(f"Descriptive statistics:\n{file.describe()}")

genres = file['listed_in'].str.split(', ').explode().str.strip()
print(f"Unique genres: {genres.unique()}")

#Finding the number of the top 10 most watched genres
print(f"Number of unique genres: {genres.nunique()}")

top_ten_genres = genres.value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.barh(top_ten_genres.index, top_ten_genres.to_numpy(), color='skyblue')
plt.xlabel('count')
plt.ylabel('Genre')
plt.title('Top 10 Most Watched Genres on Netflix')
plt.tight_layout()
plt.show()

ratings_count = file['rating'].value_counts()
plt.figure(figsize=(10, 6))
ratings_count.plot(kind='bar', color='lightgreen')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.title('Distribution of Ratings on Netflix')
plt.tight_layout()
plt.show()