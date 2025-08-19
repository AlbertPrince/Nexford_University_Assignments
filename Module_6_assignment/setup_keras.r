# Remove older keras package (optional, if already done)
if ("keras" %in% rownames(installed.packages())) {
  remove.packages("keras")
}

# Install newer Keras and TensorFlow interface for R
install.packages("keras3")
install.packages("tensorflow")

# Load the libraries
library(keras3)
library(tensorflow)

# Install TensorFlow backend (you can add version = "2.15.0" if needed)
install_tensorflow()
