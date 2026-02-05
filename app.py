from flask import Flask, render_template, request, jsonify
from chat_engine import ChatBot
import uuid

app = Flask(__name__)

# Basic in-memory session store
# sessions = { "session_id": ChatBotInstance }
sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message', '')
    session_id = data.get('session_id')

    # Assign a new session ID if none provided or invalid
    if not session_id or session_id not in sessions:
        session_id = str(uuid.uuid4())
        sessions[session_id] = ChatBot()
    
    bot = sessions[session_id]
    response = bot.get_response(user_input)

    # Convert newlines to HTML line breaks for correct display
    response_html = response.replace('\n', '<br>')

    return jsonify({
        'response': response_html,
        'session_id': session_id
    })

if __name__ == '__main__':
    app.run(debug=True)
