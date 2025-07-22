library(utils)

zipped_file <- "C:/Users/apmen/Documents/Nexford Uni/Module_2_assignment/Employee_Profile.zip"

unzip(zipped_file, exdir = "C:/Users/apmen/Documents/Nexford Uni/Module_2_assignment")

contents <- readLines(unz(zipped_file, "GARY_JIMENEZ_employee_details.csv"))

print(contents)