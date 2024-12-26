from flask import Blueprint, request, jsonify
from falcon import Falcon

falcon_blueprint = Blueprint('falcon', __name__)

# Load Falcon model
falcon = Falcon(model_name="tiiuae/falcon-7b")

@falcon_blueprint.route('/generate-lesson', methods=['POST'])
def generate_lesson():
    data = request.json
    topic = data.get('topic')
    try:
        response = falcon(f"Create a lesson on {topic} in Swahili. Include a quiz.")
        return jsonify({"lesson": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
