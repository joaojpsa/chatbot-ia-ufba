
from flask import Flask, jsonify, request

from services.AI_service import ask_chatgpt

app = Flask(__name__)

@app.route('/documents/<string:document_id>', methods=["POST"])
def document_info(document_id):
    data = request.json
    question = data.get("question")

    if not question:
        return jsonify({"error": "empty question"}), 400

    response = ask_chatgpt(question)
    return jsonify(response)
    


if __name__ == "__main__":
    app.run(debug=True)
