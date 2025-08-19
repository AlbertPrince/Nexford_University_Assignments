library(keras3)
library(tensorflow)

fashion_mnist <- dataset_fashion_mnist()
c(c(x_train, y_train), c(x_test, y_test)) %<-% fashion_mnist

x_train <- x_train / 255
x_test <- x_test / 255

x_train <- array_reshape(x_train, c(nrow(x_train), 28, 28, 1))
x_test <- array_reshape(x_test, c(nrow(x_test), 28, 28, 1))

model <- keras_model_sequential() |>
  layer_input(shape = c(28, 28, 1)) |>
  layer_conv_2d(filters = 32, kernel_size = c(3,3), activation = "relu") |>
  layer_max_pooling_2d(pool_size = c(2,2)) |>
  layer_conv_2d(filters = 64, kernel_size = c(3,3), activation = "relu") |>
  layer_flatten() |>
  layer_dense(units = 64, activation = "relu") |>
  layer_dense(units = 10, activation = "softmax")

model |>
  compile(
    optimizer = "adam",
    loss = "sparse_categorical_crossentropy",
    metrics = "accuracy"
  )

model |>
  fit(
    x = x_train,
    y = y_train,
    epochs = 5,
    validation_data = list(x_test, y_test)
  )

predictions <- model |>
  predict(x_test[1:2, , , , drop = FALSE])

predicted_labels <- apply(predictions, 1, which.max) - 1

for (i in 1:2) {
  image(matrix(x_test[i, , , 1], nrow = 28)[, 28:1],
        col = gray.colors(255), axes = FALSE)
  title(main = paste("Predicted:", predicted_labels[i], "| Actual:", y_test[i]))
}
