import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

img_size = (28,28)
batch_size = 32

datagen = ImageDataGenerator(validation_split=0.2, rescale=1./255)

train = datagen.flow_from_directory(
    "dataset",
    target_size=img_size,
    color_mode="grayscale",
    batch_size=batch_size,
    class_mode="categorical",
    subset="training"
)

val = datagen.flow_from_directory(
    "dataset",
    target_size=img_size,
    color_mode="grayscale",
    batch_size=batch_size,
    class_mode="categorical",
    subset="validation"
)

model = models.Sequential([
    layers.Input(shape=(28,28,1)),
    layers.Conv2D(32,3,activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64,3,activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128,activation='relu'),
    layers.Dense(36,activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train, validation_data=val, epochs=5)

model.save("plate_model.keras")
print("Saved!")
