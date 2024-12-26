from flask import Blueprint, request, jsonify
from google.cloud import translate_v2 as translate

translate_client = translate.Client()

translate_blueprint = Blueprint('translate', __name__)

@translate_blueprint.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get('text')
    target_lang = data.get('targetLang')

    if not text or not target_lang:
        return jsonify({"error": "Missing text or targetLang"}), 400

    try:
        result = translate_client.translate(text, target_language=target_lang)
        return jsonify({"translatedText": result['translatedText']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
