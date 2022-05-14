from crypt import methods
import json
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter

import utils
from client import SlackClient
import os

app = Flask(__name__)
slack_client = SlackClient()
slack_event_adapter = SlackEventAdapter(os.getenv("SECRET_TOKEN"),'/slack/events',app)
BOT_ID = slack_client.client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')
    if user_id != BOT_ID :
        text = event.get('text')
        msg = f"hi <@{user_id}> i know you send '{text}' and don't just try \n يا اهل الجروب <!channel> اليوزر ده بعت الرسالة دى"
        slack_client.post_message(channel_id=channel_id,message=msg)

@app.route("/say-hi",methods=["POST"])
def say_hi():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    channel_name = data.get("channel_name")
    user_name = data.get('user_name')
    MSG = f"Hi <@{user_id}> to {channel_name} Channel \n Please All <!here> Welcome OUR Friend {user_name}"
    slack_client.post_message(channel_id=channel_id,message=MSG)
    return Response(),200
    
