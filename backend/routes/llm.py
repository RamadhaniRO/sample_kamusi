from flask import Blueprint, request, jsonify
from transformers import pipeline

llm_blueprint = Blueprint('llm', __name__)

# Load pre-trained models
translator = pipeline('translation_en_to_sw', 'Helsinki-NLP/opus-mt-en-sw')
chatbot = pipeline('conversational', 'microsoft/DialoGPT-medium')

@llm_blueprint.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    try:
        result = translator(text)
        return jsonify({"translatedText": result[0]['translation_text']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@llm_blueprint.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    try:
        result = chatbot(message)
        return jsonify({"reply": result[0]['generated_text']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
