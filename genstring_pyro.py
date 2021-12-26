import pyrogram
from pyrogram import Client

heiman_ = """
Copyright (C) 2021 by @Shailendra34
This file is part of dev project,
and is released under the "MIT License Agreement".
Telegram @Shailendra34 and @Modmenumaking
"""

print(heiman_)
api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")

with Client("Heiman", api_id=api_id, api_hash=api_hash) as bot:
    first_name = (bot.get_me()).first_name
    string_session_ = f"<b>😎 sᴛʀɪɴɢ 🤟 sᴇssɪᴏɴ 🔥 ғᴏʀ ❤ {first_name}</b> \nᴛʜᴀɴᴋs ✌ ᴛᴏ 💞 @Shailendra34 \n\n<code>{bot.export_session_string()}</code> 🇮🇳"
    bot.send_message("me", string_session_, parse_mode="html")
    print(f"String Has Been Sent To Your Saved Message : {first_name}")
