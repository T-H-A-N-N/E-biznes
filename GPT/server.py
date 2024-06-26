from flask import Flask, request, jsonify, render_template_string
import openai

app = Flask(__name__)

openai.api_key = ''

def analyze_sentiment(text):
    from textblob import TextBlob
    blob = TextBlob(text)
    return blob.sentiment.polarity

def filter_by_topic(text, topics):
    for topic in topics:
        if topic.lower() in text.lower():
            return True
    return False

@app.route('/')
def home():
    return render_template_string('''
        <form action="/chat" method="post" id="chat-form">
            <input type="text" name="message" placeholder="Type your message here">
            <input type="submit">
        </form>
        <div id="response"></div>
        <script>
            document.getElementById('chat-form').onsubmit = async function(event) {
                event.preventDefault();
                const message = document.querySelector('input[name="message"]').value;
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ message: message })
                });
                const data = await response.json();
                document.getElementById('response').innerText = JSON.stringify(data, null, 2);
            }
        </script>
    ''')

@app.route('/chat', methods=['POST'])
def chat():
    if request.content_type != 'application/json':
        return jsonify({'error': "Unsupported Media Type: Did not attempt to load JSON data because the request Content-Type was not 'application/json'."}), 415

    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        
        user_input = data['message']
        allowed_topics = ['dogs', 'cats']

        if filter_by_topic(user_input, allowed_topics):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Welcome!"},
                    {"role": "user", "content": user_input}
                ]
            )
            gpt_response = response.choices[0].message['content'].strip()
            sentiment = analyze_sentiment(gpt_response)

            return jsonify({
                'response': gpt_response,
                'sentiment': 'positive' if sentiment > 0 else 'negative' if sentiment < 0 else 'neutral',
                'source': 'gpt'
            })
        else:
            return jsonify({'error': 'Topic not allowed'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
