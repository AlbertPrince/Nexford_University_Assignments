👨‍💻 Project Description
This project analyzes a dataset of Netflix shows and movies to extract meaningful insights. The analysis includes data cleaning, exploration, and visualization using Python and R, with a focus on viewer trends such as the distribution of ratings and popular genres.

📂 Files Included
File Name	Description
Netflix_shows_movies.csv	Original dataset (renamed after unzipping)
Assignment.py	Main Python script for data analysis
Netflix_cleaned.csv	Cleaned dataset used in R
ratings_chart_r.R	R script to reproduce ratings distribution chart
README.md	Project overview and instructions (this file)

🧼 1. Data Preparation
The dataset was unzipped and renamed to Netflix_shows_movies.csv.

Missing values were handled as follows:

director and country filled with "Unknown".

cast filled with "Not entered".

Rows missing rating or date_added were dropped.

📊 2. Data Exploration
Dataset contains 6,214 rows and 12 columns after cleaning.

Explored structure, data types, and summary statistics.

Analyzed common content types and frequent ratings.

📈 3. Visualizations (Python)
✅ A. Most Watched Genres
Extracted individual genres from the listed_in column.

Visualized the Top 10 Genres using a horizontal bar chart (Matplotlib).

✅ B. Ratings Distribution
Counted occurrences of each rating (e.g., TV-MA, PG, etc.).

Visualized using a vertical bar chart (Matplotlib).

📊 4. Visualization in R
Used ggplot2 in R to recreate the distribution of ratings chart.


🛠️ How to Run
▶️ Python:
Run Assignment.py in a Python 3.12 virtual environment.

Requires: pandas, matplotlib, seaborn

▶️ R:
Open Netflix_assignment.R in RStudio or R terminal.

Requires: ggplot2

📌 Notes
All visualizations are labeled and styled for clarity.

The cleaned dataset (Netflix_cleaned.csv) was used for both Python and R charts.

The R chart reproduces the Python ratings chart using native R syntax and style.