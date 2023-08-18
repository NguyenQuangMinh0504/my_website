import dotenv
import os
dotenv.load_dotenv()
DOCKER_USING = os.getenv("DOCKER_USING")
DB_HOST = os.getenv("DB_DOCKER_HOST") if DOCKER_USING == "True" \
        else os.getenv("DB_HOST")
DB_PASSWORD = os.getenv("DB_PASSWORD")
