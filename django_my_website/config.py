import dotenv
import os
dotenv.load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")
IP_GRAPH_LINK = os.getenv("IP_GRAPH_LINK")
REQUEST_GRAPH_LINK = os.getenv("REQUEST_GRAPH_LINK")
IMAGES_FOLDER_PATH = os.getenv("IMAGES_FOLDER_PATH")
DATE_FORMAT = "%m/%d/%Y"
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")
CHAT_ROOM_ID = os.getenv("CHAT_ROOM_ID")
GOOGLE_APP_PASSWORD = os.getenv("GOOGLE_APP_PASSWORD")
DEBUG = os.getenv("DEBUG")
