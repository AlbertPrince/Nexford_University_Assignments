library(keras3)
library(tensorflow)

fashion <- dataset_fashion_mnist()
x_train <- fashion$train$x
y_train <- fashion$train$y
x_test  <- fashion$test$x
y_test  <- fashion$test$y

x_train <- x_train / 255
x_test  <- x_test / 255

x_train <- array_reshape(x_train, c(nrow(x_train), 28, 28, 1))
x_test  <- array_reshape(x_test,  c(nrow(x_test), 28, 28, 1))

model <- keras_model_sequential() |>
  layer_conv_2d(filters = 32, kernel_size = c(3,3), activation = "relu",
                input_shape = c(28, 28, 1)) |>
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

history <- model |>
  fit(
    x_train, y_train,
    epochs = 5,
    validation_data = list(x_test, y_test)
  )

class_names <- c("T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
                 "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot")

save_dir <- file.path(getwd(), "Module_6_assignment", "R_assignment")
if (!dir.exists(save_dir)) {
  dir.create(save_dir, recursive = TRUE)
}

x_subset <- x_test[1:2,,, , drop=FALSE]
predictions <- model |> predict(x_subset)

for (i in 1:2) {
  pred_label <- which.max(predictions[i,]) - 1
  true_label <- y_test[i]

  png(file.path(save_dir, paste0("prediction_", i-1, ".png")))
  img <- x_test[i,,,1]
  image(1:28, 1:28, img[,28:1], col=gray.colors(255), axes=FALSE,
        main=paste0("Predicted: ", class_names[pred_label+1],
                    "\nTrue: ", class_names[true_label+1]))
  dev.off()
}

model$save(file.path(save_dir, "fashion_cnn.keras"))
write.table(predictions, file=file.path(save_dir, "predictions.txt"))
