from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/42c826f62631bd72a9eb6.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/42c826f62631bd72a9eb6.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/VVBB6")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/VVBB6")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6255366438").split()))


FAILED = "https://telegra.ph/file/42c826f62631bd72a9eb6.jpg"
