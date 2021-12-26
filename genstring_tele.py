from telethon.sessions import StringSession
from telethon.sync import TelegramClient

heiman_ = """
Copyright (C) 2021 by @Shailendra34
This file is part of dev project,
and is released under the "MIT License Agreement".
Telegram @Shailendra34 and @Modmenumaking
"""

print(heiman_)
api_id = input("Enter Your API ID: \n")
api_hash = input("Enter Your API HASH : \n")

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Check your Telegram Saved Messages to copy the STRING_SESSION value")
    session_string = client.session.save()
    saved_messages_template = """Thanks To @Shailendra34 \n
<code>STRING_SESSION</code>: <code>{}</code>
⚠️ <i>Please be carefull to pass this value to third parties</i>""".format(session_string)
    client.send_message("me", saved_messages_template, parse_mode="html")
