import os
import dotenv
dotenv.load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")
IP_GRAPH_LINK = os.getenv("IP_GRAPH_LINK")
REQUEST_GRAPH_LINK = os.getenv("REQUEST_GRAPH_LINK")
DATE_FORMAT = "%m/%d/%Y"
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
CHAT_ROOM_ID = os.getenv("CHAT_ROOM_ID")
GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")
DEBUG = True if os.getenv("DEBUG") == "True" else False
