from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("host"),
    "port": os.getenv("port"),
    "database": os.getenv("database"),
    "user": os.getenv("user"),
    "password": os.getenv("password")
}

