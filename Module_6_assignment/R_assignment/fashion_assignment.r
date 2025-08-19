library(keras3)
library(tensorflow)

# Load Fashion MNIST
fashion_mnist <- dataset_fashion_mnist()
x_train <- fashion_mnist$train$x
y_train <- fashion_mnist$train$y
x_test <- fashion_mnist$test$x
y_test <- fashion_mnist$test$y

# Normalize
x_train <- x_train / 255
x_test <- x_test / 255

# Reshape
x_train <- array_reshape(x_train, c(nrow(x_train), 28, 28, 1))
x_test <- array_reshape(x_test, c(nrow(x_test), 28, 28, 1))

# Model
model <- keras_model_sequential() |>
  layer_conv_2d(filters = 32, kernel_size = c(3,3), activation = "relu", input_shape = c(28,28,1)) |>
  layer_max_pooling_2d(pool_size = c(2,2)) |>
  layer_conv_2d(filters = 64, kernel_size = c(3,3), activation = "relu") |>
  layer_flatten() |>
  layer_dense(units = 64, activation = "relu") |>
  layer_dense(units = 10, activation = "softmax")

model |>
  compile(optimizer = "adam",
          loss = "sparse_categorical_crossentropy",
          metrics = "accuracy")

history <- model |>
  fit(x_train, y_train, epochs = 5, validation_data = list(x_test, y_test))

# Predict first 2 test images
predictions <- model |> predict(x_test[1:2,,,drop=FALSE])

# Class names
class_names <- c("T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
                 "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot")

# Plot results
par(mfrow=c(1,2))
for (i in 1:2) {
  pred_label <- which.max(predictions[i,]) - 1
  true_label <- y_test[i]
  
  img <- x_test[i,,,drop=FALSE]
  img <- array_reshape(img, c(28,28))
  
  image(1:28, 1:28, img[,28:1], col=gray.colors(255), axes=FALSE, main=
          paste0("Predicted: ", class_names[pred_label+1],
                 "\nTrue: ", class_names[true_label+1]))
}
