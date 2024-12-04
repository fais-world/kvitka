from flask import Flask, jsonify, request
from openai import Client
import os

# Initialize OpenAI Client with the API key
client = Client(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Flask app
app = Flask("kvitka-backend")

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle POST requests to the /api/chat endpoint.
    """
    try:
        # Parse the JSON payload from the client
        data = request.get_json()
        query = data.get("query")
        if not query:
            return jsonify({"error": "Query is required"}), 400

        # Use Client's chat.completions.create method
        response = client.chat.completions.create(
            model="ft:gpt-4o-mini-2024-07-18:fai-s-tudio:kvitka:ATGvsK8F",  # Replace with your fine-tuned model ID
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ],
            max_tokens=150,
            temperature=0.7
        )

        # Extract and return the assistant's response
        response_content = response.choices[0].message.content.strip()
        return jsonify({"response": response_content})

    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
