import os
from flask import Flask, jsonify, request
import openai

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask("kvitka-backend")

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        query = data.get("query", "")
        if not query:
            return jsonify({"error": "Query is required"}), 400

        # Query OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Update this as needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query},
            ],
            max_tokens=150,
        )
        return jsonify({"response": response.choices[0].message.content.strip()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
