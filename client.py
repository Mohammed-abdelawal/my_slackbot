import os
import requests
import slack



class SlackClient:
    def __init__(self):
        self.client = slack.WebClient(token=os.getenv("AUTH_TOKEN"))

    # opens a new conversation
    def open_conv(self, user_id: str):
        url = f"{self.__root}/conversations.open"
        payload = {"token": self.__auth_token, "users": [user_id]}

        res = requests.post(url, data=payload)
        return res.json()["channel"]["id"]

    def post_message(self, channel_id: str, message: str):
        self.client.chat_postMessage(channel=channel_id,text=message)