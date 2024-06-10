import pandas as pd
from tensorflow.keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
import os
import os.path
from pathlib import Path
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from keras.optimizers import RMSprop

no_tumor_path = Path("archive/no")
tumor_path = Path("archive/yes")

no_tumor_all = list(no_tumor_path.glob(r"*.jpg"))
tumor_all = list(tumor_path.glob(r"*.jpg"))

all_data_list = []

for name in no_tumor_all:
    all_data_list.append(name)

for name in tumor_all:
    all_data_list.append(name)

labels = list(map(lambda x: os.path.split(os.path.split(x)[0])[1], all_data_list))

all_data_series = pd.Series(all_data_list, name="JPG").astype(str)
all_data_category_series = pd.Series(labels, name="TUMOR_CATEGORY")

pretrain_data = pd.concat([all_data_series, all_data_category_series], axis=1)

prediction_path = Path("archive/pred")
prediction_all = list(prediction_path.glob(r"*.jpg"))
prediction_all_labels = list(map(lambda x: os.path.split(os.path.split(x)[0])[1], prediction_all))
prediction_all_series = pd.Series(prediction_all, name="JPG").astype(str)
prediction_all_labels_series = pd.Series(prediction_all_labels, name="TUMOR_CATEGORY")
prediction_data = pd.concat([prediction_all_series, prediction_all_labels_series], axis=1)


pretrain_data = pretrain_data.sample(frac=1).reset_index(drop=True)
train_data, test_data = train_test_split(pretrain_data, train_size=0.9, random_state=42)

image_data_generator = ImageDataGenerator(rescale=1. / 255,
                                          validation_split=0.1)
train_data_extended = image_data_generator.flow_from_dataframe(dataframe=train_data,
                                                               x_col="JPG",
                                                               y_col="TUMOR_CATEGORY",
                                                               color_mode="grayscale",
                                                               class_mode="categorical",
                                                               subset="training",
                                                               batch_size=20,
                                                               target_size=(200, 200))

validation_data = image_data_generator.flow_from_dataframe(dataframe=train_data,
                                                           x_col="JPG",
                                                           y_col="TUMOR_CATEGORY",
                                                           color_mode="grayscale",
                                                           class_mode="categorical",
                                                           subset="validation",
                                                           batch_size=20,
                                                           target_size=(200, 200))

predicted_data = image_data_generator.flow_from_dataframe(dataframe=test_data,
                                                          x_col="JPG",
                                                          y_col="TUMOR_CATEGORY",
                                                          color_mode="grayscale",
                                                          class_mode="categorical",
                                                          batch_size=20,
                                                          target_size=(200, 200))

model = Sequential()

model.add(Conv2D(32, (5, 5), activation="relu", input_shape=(200, 200, 1)))
model.add(MaxPool2D((2, 2)))
model.add(Dropout(0.2))
#
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPool2D((2, 2)))
model.add(Dropout(0.2))
#
model.add(Conv2D(128, (3, 3), activation="relu"))
model.add(MaxPool2D((2, 2)))
model.add(Dropout(0.2))
#
model.add(Conv2D(256, (3, 3), activation="relu"))
model.add(MaxPool2D((2, 2)))
model.add(Dropout(0.2))
#
model.add(Flatten())
model.add(Dropout(0.5))
model.add(Dense(512, activation="relu"))
model.add(Dense(2, activation="softmax"))

model.compile(optimizer=RMSprop(learning_rate=0.001), loss="categorical_crossentropy", metrics=["accuracy"])
model.fit(train_data_extended, validation_data=validation_data, epochs=30, steps_per_epoch=120)

model_evaluated = model.evaluate(predicted_data, verbose=False)
print("LOSS:  " + "%.4f" % model_evaluated[0])
print("ACCURACY:  " + "%.2f" % model_evaluated[1])

# model.save('saved_model_2.keras')
