from flask import Blueprint, request, jsonify
from llama_cpp import Llama

llama_blueprint = Blueprint('llama', __name__)

# Load LLaMA model
llama = Llama(model_path="path/to/llama-7b.bin")

@llama_blueprint.route('/generate-lesson', methods=['POST'])
def generate_lesson():
    data = request.json
    topic = data.get('topic')
    try:
        response = llama(f"Create a lesson on {topic} in Swahili. Include a quiz.")
        return jsonify({"lesson": response['choices'][0]['text']})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
