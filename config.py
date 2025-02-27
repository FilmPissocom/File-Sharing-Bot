import os
import logging
from logging.handlers import RotatingFileHandler

# Bot Token from @BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7742850582:AAGO1HhnxVGPYZxybZkNiA47XCVzax8KUSY")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26834328"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ddc4bd4e60c6d007e9c0428916b64f92")

# Owner ID (Your Telegram User ID)
OWNER_ID = int(os.environ.get("OWNER_ID", "6199575037"))

# Database URL (MongoDB Connection String)
DB_URL = os.environ.get(
    "DB_URL",
    "mongodb+srv://FilmPisso:fw&iaziqF(P96Hvwvkr5@cluster0.i2v4v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)

# Database Name
DB_NAME = os.environ.get("DB_NAME", "FilmPisso")

# Your channel ID for storing files
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002378478916"))

# Force Subscription Channel ID
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002088006907"))

# Auto-delete time in seconds
FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "2592000"))

# Port for the bot server
PORT = os.environ.get("PORT", "8080")

# Number of bot workers
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Admins List
try:
    ADMINS = [8004139936]  # Default admin IDs
    for x in os.environ.get("ADMINS", "8004139936").split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Custom Caption (set to None to disable)
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Protect content from being forwarded
PROTECT_CONTENT = True if os.environ.get("PROTECT_CONTENT", "False") == "True" else False

# Disable the "Open Channel" button
DISABLE_CHANNEL_BUTTON = True if os.environ.get("DISABLE_CHANNEL_BUTTON", "True") == "True" else False

# Bot stats text
BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"

# User reply message
USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot on Film Pisso!"

# Start message
START_MSG = os.environ.get(
    "START_MESSAGE",
    "හෙලෝ !👋 {mention}\n\n<b>Telegram හරහා 🎬 Movies සහ TV Shows 📺 Download කරගැනීමට හැක.</b>\n\n 🎬 𝐌𝐨𝐯𝐢𝐞𝐬 & 𝐓𝐕 𝐒𝐡𝐨𝐰𝐬 📺 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐚𝐧𝐝 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐏𝐥𝐚𝐭𝐟𝐨𝐫𝐦 𝐢𝐧 #𝐒𝐫𝐢𝐋𝐚𝐧𝐤𝐚 🔥🇱🇰\n\n𝐕𝐢𝐬𝐢𝐭 📽 𝐅𝐈𝐋𝐌 𝐏𝐈𝐒𝐒𝐎ᶜᵒᵐ 📽 - https://www.filmpisso.com",
)

# Force subscription message
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "හෙලෝ !👋 {mention}\n\n<b>🎬 𝐌𝐨𝐯𝐢𝐞𝐬 & 𝐓𝐕 𝐒𝐡𝐨𝐰𝐬 📺 Telegram  හරහා Download  කරගැනීමට පහත Join Channel  ක්ලික් කරල ජොයින් වෙලා බැක් වෙලා ඇවිත් පහල Try Again ක්ලික් කරන </b>",
)

# Append owner ID to admins list
ADMINS.append(OWNER_ID)

# Log file name
LOG_FILE_NAME = "filesharingbot.txt"

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
