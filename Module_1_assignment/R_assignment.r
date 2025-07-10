first_names_male <- c("Kwame", "John", "Kofi", "Antonio", "Tony", "Nii", "Kojo", "Edem", "Bruce", "Steven")
first_names_female <- c("Mary", "Linda", "Patricia", "Jennifer", "Elizabeth", "Susan", "Jessica", "Sarah", "Karen", "Nancy")
last_names <- c("Wayne", "Banner", "Stark", "Brown", "Jones", "Mensah", "Larteh", "Agbodza", "Lartey", "Gbotsu")

n_workers <- 400
genders <- sample(c("Male", "Female"), n_workers, replace = TRUE)
first_names <- ifelse(genders == "Male",
                      sample(first_names_male, n_workers, replace = TRUE),
                      sample(first_names_female, n_workers, replace = TRUE))
last_names_sample <- sample(last_names, n_workers, replace = TRUE)
names <- paste(first_names, last_names_sample)
worker_ids <- sprintf("W%04d", 1:n_workers)
salaries <- sample(5000:32000, n_workers, replace = TRUE)

workers <- data.frame(
  id = worker_ids,
  name = names,
  gender = genders,
  salary = salaries,
  stringsAsFactors = FALSE
)

for (i in 1:nrow(workers)) {
  worker <- workers[i, ]
  level <- ""
  if (worker$salary > 10000 & worker$salary < 20000) {
    level <- "A1"
  }
  if (worker$gender == "Female" & worker$salary > 7500 & worker$salary < 30000) {
    level <- "A5-F"
  }
  cat(sprintf("Payment Slip for %s (ID: %s)\n", worker$name, worker$id))
  cat(sprintf("Gender: %s\n", worker$gender))
  cat(sprintf("Salary: $%d\n", worker$salary))
  cat(sprintf("Employee Level: %s\n", ifelse(level != "", level, "N/A")))
  cat(strrep("-", 40), "\n")
}
