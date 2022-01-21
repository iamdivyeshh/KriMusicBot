# Divyesh Vaghela // @ZaYNxOP 
from pyrogram import Client, filters
from modules.helpers.filters import command, other_filters
from modules.helpers.command import commandpro
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton










@Client.on_message(commandpro(["/start", "/alive", "divyeshh", "owner"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/92bba3375827ea52df036.mp4",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "मेरे भगवान...✨", url=f"https://t.me/zaynxop")
                ]
            ]
        ),
    )

