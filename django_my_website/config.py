import dotenv
import os
dotenv.load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")
IP_GRAPH_LINK = os.getenv("IP_GRAPH_LINK")
REQUEST_GRAPH_LINK = os.getenv("REQUEST_GRAPH_LINK")
IMAGES_FOLDER_PATH = os.getenv("IMAGES_FOLDER_PATH")
DATE_FORMAT = "%m/%d/%Y"
