import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(os.path.join('.env'))

TELEGRAM_BOT_API_TOKEN=os.environ.get('TELEGRAM_BOT_API_TOKEN')
ENVIRONMENT=os.environ.get('ENVIRONMENT')
URL=os.environ.get('URL')

DB_HOST=os.environ.get('DB_HOST')
DB_PORT=os.environ.get('DB_PORT')
DB_NAME=os.environ.get('DB_NAME')
DB_USER=os.environ.get('DB_USER')
DB_PASSWORD=os.environ.get('DB_PASSWORD')
