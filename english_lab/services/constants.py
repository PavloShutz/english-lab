"""Global constants for the application."""


import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

ADMINS = json.loads(os.environ.get("ADMINS"))
CHAT_ID = os.getenv("CHAT_ID")
TOKEN = os.getenv("TOKEN")
PER_PAGE = 2
