from os import getenv

import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = getenv("DATABASE_URL")

connection = psycopg2.connect(DATABASE_URL)
cursor = connection.cursor()
