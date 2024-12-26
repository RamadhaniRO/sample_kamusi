from flask import Blueprint, request, jsonify
from openassistant import OpenAssistant

oa_blueprint = Blueprint('openassistant', __name__)

# Load OpenAssistant model
oa = OpenAssistant(model_name="OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")

@oa_blueprint.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message')
    try:
        response = oa.generate(message)
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
