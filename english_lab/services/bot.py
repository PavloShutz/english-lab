"""Methods described for bot usage"""

import requests
from datetime import date
from flask import url_for

from english_lab.models import Topic


def _send_message(token: str, chat_id: int, message: str) -> None:
    """Send a message to the chat with given chat_id and from bot that has the token"""
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.post(url)


def send_notification_about_new_topic(token: str, chat_id: int, new_topic: Topic):
    _send_message(token, chat_id, f"""
📢 NEW TOPIC IS HERE!

{new_topic.title}

📆 Added: {date.today()}

🔎 Check it on our web-site:

{f'http://127.0.0.1:5000/{url_for("topic.read_topic", topic_id=new_topic.id)}'}
""")
