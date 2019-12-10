from flask import Flask
from flask import request
from flask import Response
from flask_cors import CORS

from t2s import genEnSpeech

app = Flask(__name__)
CORS(app)


@app.route('/speech', methods=['GET'])
def hello():
    text = request.args.get('text')
    gender = request.args.get('gender')
    speech = genEnSpeech(text, gender)
    return Response(speech, mimetype='audio/mp3')


if __name__ == '__main__':
    app.run()
