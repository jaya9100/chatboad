
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Set your OpenAI API Key
openai.api_key = "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"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip().lower()  # Clean input

    if not user_message:
        return jsonify({"response": "Please enter a message."})

    # Predefined responses for basic words
    predefined_responses = {
        "hello": "Hello",
        "hi": "Hello",
        "hey": "Hello",
        "bye": "Goodbye",
        "thanks": "You're welcome!",
        "help": "How can I assist you?"
    }

    # Check if cleaned user input matches predefined responses
    if user_message in predefined_responses:
        return jsonify({"response": predefined_responses[user_message]})

    try:
        # Call OpenAI API only if no predefined response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error: {e}")  # Debugging in console
        bot_reply = "Sorry, something went wrong."

    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
