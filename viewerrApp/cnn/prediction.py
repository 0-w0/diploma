import keras
import requests
import cv2
import numpy as np


class Prediction:

    def __init__(self):
        self.model = keras.models.load_model('cnn/saved_model_1.keras')

    def predict_local(self, items_list):
        images = self.read_from_dir(items_list)
        return self.get_prediction(images)

    def predict_url(self, urls):
        images = self.get_from_url(urls)
        return self.get_prediction(images)

    def get_prediction(self, data):
        model_prediction = self.model.predict(data, batch_size=20)
        model_prediction = model_prediction.argmax(axis=-1)
        last_prediction = ['TUMOR' if i == 1 else 'NO' for i in model_prediction]
        # [last_prediction.append('NO') if i == 1 else last_prediction.append('TUMOR') for i in model_prediction]
        return last_prediction

    def get_from_url(self, urls):
        images = []
        for url in urls:
            img_data = requests.get(url).content
            img = cv2.imdecode(np.frombuffer(img_data, np.uint8), 0)
            img = cv2.resize(img, (200, 200))
            images.append(img)

        images = np.reshape(images, [len(urls), 200, 200, 1])

        return images

    def read_from_dir(self, items_list):
        images = []
        for item in items_list:
            img = cv2.imread(item, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (200, 200))
            images.append(img)

        images = np.asarray(images)
        return images


# pred = Prediction()
# print(pred.predict_local(['../archive/pred/pred0.jpg', '../archive/pred/pred1.jpg', '../archive/pred/pred2.jpg',
#                           '../archive/pred/pred3.jpg', '../archive/pred/pred4.jpg', '../archive/pred/pred5.jpg',
#                           '../archive/pred/pred6.jpg', '../archive/pred/pred14.jpg']))
