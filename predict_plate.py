import cv2
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model("plate_model.keras")
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

path = input("Enter image path: ")
img = cv2.imread(path)

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Better threshold
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Remove noise
kernel = np.ones((2,2), np.uint8)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

boxes = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)

    # Better filtering
    if h > 15 and w > 5:
        boxes.append((x, y, w, h))

boxes = sorted(boxes, key=lambda b: b[0])

result = ""

for (x, y, w, h) in boxes:
    roi = thresh[y:y+h, x:x+w]

    # Add padding
    roi = cv2.copyMakeBorder(roi, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=0)
    roi = cv2.resize(roi, (28, 28))

    roi = roi / 255.0
    roi = roi.reshape(1, 28, 28, 1)

    pred = model.predict(roi, verbose=0)
    char = chars[np.argmax(pred)]

    result += char

print("Detected Plate:", result)
