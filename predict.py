import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load model
model = tf.keras.models.load_model("digit_model.h5")

# Read your image
img = cv2.imread("digit.png", cv2.IMREAD_GRAYSCALE)

# Resize to 28x28
img = cv2.resize(img, (28, 28))

# Normalize
img = img / 255.0

# Reshape for model
img_input = img.reshape(1, 28, 28, 1)

# Predict
prediction = model.predict(img_input)
digit = np.argmax(prediction)

print("Predicted Digit:", digit)

# Show image
plt.imshow(img, cmap="gray")
plt.title(f"Predicted: {digit}")
plt.show()
