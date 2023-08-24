import dotenv
import os
dotenv.load_dotenv()
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")
WEBSITE_TRAFFIC_PANEL_LINK = os.getenv("WEBSITE_TRAFFIC_PANEL_LINK")
IMAGES_FOLDER_PATH = os.getenv("IMAGES_FOLDER_PATH")
