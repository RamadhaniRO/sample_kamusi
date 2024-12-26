from flask import Flask
from flask_cors import CORS
from .routes.translate import translate_blueprint
from .routes.dictionary import dictionary_blueprint
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(translate_blueprint, url_prefix='/api')
app.register_blueprint(dictionary_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(port=5000)
