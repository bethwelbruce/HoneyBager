# HoneyBadger
Create a production-ready web endpoint that accepts a JSON payload as a POST request and sends an alert to a Slack channel if the payload matches desired criteria. This project should be straight-forward 

#SOLUTION
To implement this web endpoint, we can use Python and the Flask framework, along with the slack-sdk library to send messages to Slack.
In this implementation, we define a single endpoint / that accepts POST requests. When a request is received, we check if the payload has a Type field of SpamNotification. If it does, we send a Slack alert with the email address included in the payload.

The send_slack_alert function sends a message to a Slack channel using the chat_postMessage method from the WebClient class. We pass in the Slack API token for our bot, the name of the channel to post to, and the text of the message
To run this code, you will need to replace SLACK_BOT_TOKEN with your actual Slack API token. You will also need to create a Slack bot and invite it to the channel you want to post alerts to.
Once you've updated the code with your Slack API token, you can run the server by executing python app.py in your terminal. This will start the server on http://localhost:5000. You can test the endpoint by sending a POST request with one of the sample payloads:
curl -X POST -H "Content-Type: application/json" -d '{"RecordType": "Bounce", "Type": "SpamNotification", "TypeCode": 512, "Name": "Spam notification", "Tag": "", "MessageStream": "outbound", "Description": "The message was delivered, but was either blocked by the user, or classified as spam, bulk mail, or had rejected content.", "Email": "zaphod@example.com", "From": "notifications@honeybadger.io", "BouncedAt": "2023-02-27T21:41:30Z"}' http://localhost:5000/
If the payload matches the desired criteria, you should see a message posted to the Slack channel you specified in the code.
