import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

ADMINS = json.loads(os.environ.get("ADMINS"))
