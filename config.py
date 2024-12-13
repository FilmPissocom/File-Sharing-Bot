#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("7003297491:AAGU-VF7KYGmu9LGyAC31r8UVhW1XEgXUwo")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("16707564"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("0d96229e8fa200de84c6776641ba8404")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("-1002242801589"))

#OWNER ID
OWNER_ID = int(os.environ.get("7647409655"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("mongodb+srv://filmpisso:CHi2S4KHswk0akfS@cluster0.erh62.mongodb.net/")
DB_NAME = os.environ.get("filmpisso", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("-1002088006907"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = os.environ.get("START_PIC","")
START_MSG = os.environ.get("START_MESSAGE", "හෙලෝ !👋 {first}\n\n<b>Telegram හරහා 🎬 Movies සහ TV Shows 📺 Download කරගැනීමට හැක.</b>\n\n 🎬 𝐌𝐨𝐯𝐢𝐞𝐬 & 𝐓𝐕 𝐒𝐡𝐨𝐰𝐬 📺 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐚𝐧𝐝 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐏𝐥𝐚𝐭𝐟𝐨𝐫𝐦 𝐢𝐧 #𝐒𝐫𝐢𝐋𝐚𝐧𝐤𝐚 🔥🇱🇰 \n\n<b>𝐕𝐢𝐬𝐢𝐭 📽 𝐅𝐈𝐋𝐌 𝐏𝐈𝐒𝐒𝐎ᶜᵒᵐ 📽</b> - https://www.filmpisso.com")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "හෙලෝ !👋 {first}\n\n<b>Telegram හරහා 🎬 Movies සහ TV Shows 📺 Download කරගැනීමට පෙර අපගේ 📽 𝐅𝐈𝐋𝐌 𝐏𝐈𝐒𝐒𝐎ᶜᵒᵐ 📽🔥🇱🇰 Updates Channel එකට Join වෙලා Back 🔙 වෙලා ඇවිත් පහල Try Again 🔄 ක්ලික් කරන්න. 👇 \n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
