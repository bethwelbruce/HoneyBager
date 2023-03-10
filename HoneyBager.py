from flask import Flask, request
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = json.loads(request.data)
    if data.get('Type') == 'SpamNotification':
        send_slack_alert(data.get('Email'))
    return '', 200

def send_slack_alert(email):
    client = WebClient(token="SLACK_BOT_TOKEN")
    try:
        response = client.chat_postMessage(
            channel="#spam-alerts",
            text=f"Spam report received from {email}"
        )
        print(response)
    except SlackApiError as e:
        print(f"Error sending message: {e}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
