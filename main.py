
from flask import Flask

from recognition.pipeline.service_recognition import recognition_model_ as recognition_blueprint, RecognitionModel

app = Flask(__name__)
port = 5000
debug = False

RecognitionModel()



app.register_blueprint(recognition_blueprint, url_prefix='/recognition/recognition_images')


@app.errorhandler(404)
def not_found(error):
    return "Not found."

@app.route('/', methods=['GET','POST'])
def index():
    return 'models is run'

if __name__ =='__main__':
    app.run(port = port, debug = debug)