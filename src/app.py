import os
from flask import Flask, jsonify, request
import openai

# Access the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask("kvitka-backend")

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle POST requests to the /api/chat endpoint.
    """
    try:
        # Get the user query from the JSON payload
        data = request.get_json()
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "Query is required"}), 400

        # Call the OpenAI API using the fine-tuned model
        response = openai.ChatCompletion.create(
            model="ft:gpt-4o-mini-2024-07-18:fai-s-tudio:kvitka:ATGvsK8F",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=150
        )

        # Return the chatbot's response
        return jsonify({"response": response.choices[0].message.content.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
