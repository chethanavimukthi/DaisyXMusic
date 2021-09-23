# DaisyXMusic (Telegram bot project)
# Copyright (C) 2021  Inuka Asith & Rojserbest

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import requests
from pyrogram import Client as Bot

from 𝗗𝗔𝗥𝗞 𝗦𝗔𝗡𝗧𝗔 |【𝗙𝗛𝗕】⁪⁬⁮⁮.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN
from 𝗗𝗔𝗥𝗞 𝗦𝗔𝗡𝗧𝗔 |【𝗙𝗛𝗕⁪⁬⁮】.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,8556184
    API_HASH,7ca71223ea88db7e9b5a824eae8c3c52
    bot_token=BOT_TOKEN,2045361996:AAG2HVPO1JDM2U_E4B_hIUa2j6n3wYlXNkg
    plugins=dict(root="𝗗𝗔𝗥𝗞 𝗦𝗔𝗡𝗧𝗔 |【𝗙𝗛𝗕⁪⁬⁮】.modules⁪"),
)

bot.start()
run()
