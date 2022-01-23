# Divyesh Vaghela // @ZaYNxOP 
from pyrogram import Client, filters
from modules.helpers.filters import command, other_filters
from modules.helpers.command import commandpro
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton




@Client.on_message(commandpro(["/divyeshh", "divyeshh"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/92bba3375827ea52df036.mp4",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ƬᕼΞ ĽΞᎶξŊƊ...🖤", url=f"https://t.me/zaynxop")
                ]
            ]
        ),
    )






@Client.on_message(commandpro(["/owner","owner"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/92bba3375827ea52df036.mp4",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ƬᕼΞ ĽΞᎶξŊƊ...🖤", url=f"https://t.me/zaynxop")
                ]
            ]
        ),
    )

@Client.on_message(commandpro(["/creator", "creator"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/e7d2b22f8bb5a5af22bc1.mp4",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ƬᕼΞ ĽΞᎶξŊƊ...🖤", url=f"https://t.me/zaynxop")
                ]
            ]
        ),
    )

@Client.on_message(commandpro(["mojila"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/e7d2b22f8bb5a5af22bc1.mp4",
        caption=f"ᴊᴏɪɴ ɴᴏᴡ ᴘᴇ ᴛᴀᴘ ᴋᴀʀ 🙂\nʜᴏ ᴊᴀʏᴇɢᴀ ᴊᴏɪɴ🙂",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴊᴏɪɴ ɴᴏᴡ ", url=f"https://t.me/mojilagujrati?videochat")
                ]
            ]
        ),
    )

