library(ggplot2)

netflix_data <- read.csv("Netflix_file_cleaned.csv")

print(ggplot(netflix_data, aes(x = rating)) +
        geom_bar(fill = "#3f3fd1", color = "black") +
        labs(title = "Netflix Ratings Distribution",
             x = "Ratings",
             y = "Count") +
        theme_minimal() +
        theme(plot.title = element_text(hjust = 0.5)))