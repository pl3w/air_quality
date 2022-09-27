import os
from dotenv import load_dotenv
load_dotenv()

MYSQL_DATA_HOST = os.getenv("MYSQL_DATA_HOST")
MYSQL_DATA_USER = os.getenv("MYSQL_DATA_USER")
MYSQL_DATA_PASSWORD = os.getenv("MYSQL_DATA_PASSWORD")
MYSQL_DATA_PORT = os.getenv("MYSQL_DATA_PORT")
MYSQL_DATA_DATABASE = os.getenv("MYSQL_DATA_DATABASE")

MY_API_KEY = os.getenv("MY_API_KEY")
