from flask import Flask
from flask import request
from flask import Response

from t2s import genEnSpeech

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    text = request.args.get('text')
    speech = genEnSpeech(text)
    return Response(speech, mimetype='audio/mp3')


if __name__ == '__main__':
    app.run()
