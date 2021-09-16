import numpy as np
from flask import request, jsonify,  Blueprint
from pathlib import Path
from app.models.singleton import Singleton
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model


MODEL = Path("app/training_models/recognition_test/model.h5")
WEIGHTS = Path("app/training_models/recognition_test/weights.h5")

recognition_model_ = Blueprint('recognition_model', __name__)

class RecognitionModel(metaclass = Singleton):
    def __init__(self):
        try:
            self.cnn = load_model(MODEL)
            self.cnn.load_weights(WEIGHTS)
            self.length = 80
            self.height = 80

            print('\n*** Recognition test model initialized sucessfully ***\n')
        except Exception as exception:
            print(exception)
            print(exception.traceback)


    def transform(self, file):

        x = load_img(file['images'], target_size=(self.length, self.height))
        x = img_to_array(x)
        x = np.expand_dims(x, axis=0)
        return x

    def predict(self, file):
        x = self.transform(file)
        array = self.cnn.predict(x)
        result = array[0]
        answer = np.argmax(result)
        print(answer.tolist())
        return {'prediction': answer.tolist()}


@recognition_model_.route("", methods=['POST'])
def recognition_images():
    recognition_model = RecognitionModel()
    result = recognition_model.predict(request.get_json(force=True))
    return jsonify(result)



