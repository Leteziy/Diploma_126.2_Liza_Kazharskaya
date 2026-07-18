import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
TOKEN = os.getenv("TOKEN")

MY_HEADERS = {
    "Accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

UI_BASE_URL = os.getenv("UI_BASE_URL")
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "--window-size=2560,1600")

BOOK_TITLE = os.getenv("BOOK_TITLE")
BOOK_URL = os.getenv("BOOK_URL")
SEARCH_PAGE_URL = os.getenv("SEARCH_PAGE_URL")
CART_PAGE_URL = os.getenv("CART_PAGE_URL")
