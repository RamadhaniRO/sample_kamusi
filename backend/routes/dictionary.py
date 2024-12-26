from flask import Blueprint, request, jsonify
from ..models.word import find_word

dictionary_blueprint = Blueprint('dictionary', __name__)

@dictionary_blueprint.route('/dictionary/<word>', methods=['GET'])
def search_word(word):
    result = find_word(word)
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Word not found"}), 404
