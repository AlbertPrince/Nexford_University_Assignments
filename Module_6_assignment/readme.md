# Fashion MNIST Classification Assignment

## Overview
This project trains a Convolutional Neural Network (CNN) to classify images from the **Fashion MNIST dataset**, which contains 70,000 grayscale images of clothing items across 10 categories.

The task was implemented in both **Python** and **R** for comparison.

---

## Files
- **fashion_assignment.py** → Python implementation using TensorFlow/Keras  
- **fashion_assignment.R** → R implementation using keras3/tensorflow  
- **readme.md** → Documentation for the project  

---

## Dataset
The **Fashion MNIST dataset** has the following classes:

1. T-shirt/top  
2. Trouser  
3. Pullover  
4. Dress  
5. Coat  
6. Sandal  
7. Shirt  
8. Sneaker  
9. Bag  
10. Ankle boot  

Each image is **28x28 pixels**, grayscale.

---

## Model Architecture
The CNN used in both Python and R implementations has the following layers:

1. **Conv2D (32 filters, 3x3, ReLU)**  
2. **MaxPooling2D (2x2)**  
3. **Conv2D (64 filters, 3x3, ReLU)**  
4. **Flatten**  
5. **Dense (64 units, ReLU)**  
6. **Dense (10 units, Softmax)**  

---

## Training
- Optimizer: **Adam**  
- Loss: **Sparse Categorical Crossentropy**  
- Metrics: **Accuracy**  
- Epochs: **5**  

Both implementations achieve around **91–92% validation accuracy** after 5 epochs.

---

## Results
After training, the model makes predictions on two test images.

- **Console Output:** Predicted and true labels are printed.  
- **Plot (R version):** Displays two test images with predicted and true labels in the plot window.  

Example:
Predicted: Sneaker, True: Sneaker
Predicted: Trouser, True: Trouser


---

## Requirements

### Python
- tensorflow  
- keras  
- matplotlib  
- numpy  

Run:
```bash
python fashion_assignment.py


R

keras3

tensorflow

Run inside R:
source("fashion_assignment.R")