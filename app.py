from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip().lower()

    # Condition 1 - Greeting
    if user_message in ["hi", "hii", "hiii", "hello", "hey"]:
        bot_reply = "Hello! 😊 How can I help you?"

    # Condition 2 - Name
    elif "your name" in user_message or "who are you" in user_message:
        bot_reply = "I am SRI Chatbot 🤖"

    # Condition 3 - How are you
    elif "how are you" in user_message:
        bot_reply = "I'm fine! 😊 Thanks for asking."

    # Unknown message
    else:
        bot_reply = "Sorry, I don't understand that. 😅"

    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
