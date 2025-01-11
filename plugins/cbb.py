from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🌐 Website :</b> <a href='https://filmpisso.com'>𝐕𝐢𝐬𝐢𝐭 📽 𝐅𝐈𝐋𝐌 𝐏𝐈𝐒𝐒𝐎ᶜᵒᵐ 📽</a> \n<b>📝 Language :</b> <a href='https://python.org'>Python 3</a> \n<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram {__version__}</a> \n<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a> \n<b>📢 Join Channel :</b> <a href='https://t.me/FilmPissocom'>📽 𝐅𝐈𝐋𝐌 𝐏𝐈𝐒𝐒𝐎ᶜᵒᵐ 📽🔥🇱🇰</a> \n<b>📢 Join Chat :</b> <a href='https://t.me/FilmPissoChat'>📽 𝐅𝐈𝐋𝐌 𝐏𝐈𝐒𝐒𝐎ᶜᵒᵐ 𝐂𝐡𝐚𝐭 📽🔥🇱🇰</a> \n<b>🧑‍💻 Developer :</b> <a href='tg://user?id={OWNER_ID}'>Sadew Didulanga</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
