from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME')
DB_ACCOUNT = os.getenv('DB_ACCOUNT')
DB_PW = os.getenv('DB_PW')
DB_MECHANISM = os.getenv('DB_MECHANISM')