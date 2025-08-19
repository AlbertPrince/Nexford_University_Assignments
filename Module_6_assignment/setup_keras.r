# Remove older keras package (optional, if already done)
if ("keras" %in% rownames(installed.packages())) {
  remove.packages("keras")
}

install.packages("keras3")
install.packages("tensorflow")

library(keras3)
library(tensorflow)

install_tensorflow()
