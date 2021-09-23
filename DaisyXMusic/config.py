# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
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
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQC9cKJi9QD8bZaUzALPf9bEdPAl9jo7AEoTGC0Sei7j_sbLakpdYHgjf1-vy1XuYPk6ntnKJAik-GaW9_UfxtOQtwRySX1ebAA-om0IfAhxsadNTUal70hYOWg4tmlIMpIufOID9DHvSMNonfa9vLCkA6fHvAcHhEUsIHWb-5oJgsPX_8V6KwIKWV6Zw2R-9p0wJgOBFGjOOdzFApBQGm4vySAQrDSxdXJjv4SkeMk7gMG-m2in3HC9iAHGQ_OHjrAbQcETn7kFIOaaiAOZvy32pVuWblWiU058QhzEDXiGDCKArPZbvaVKNgPo3K7pCxhfF_Q9FwXi5qj9zvZ5D8wZcbsz3QA")
BOT_TOKEN = getenv("2045361996:AAG2HVPO1JDM2U_E4B_hIUa2j6n3wYlXNkg")
BOT_NAME = getenv("song_finder")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Teletechsupport_channal")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", "8556184"))
API_HASH = getenv("7ca71223ea88db7e9b5a824eae8c3c52")
BOT_USERNAME = getenv("songfinder3_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "𝗗𝗔𝗥𝗞 𝗦𝗔𝗡𝗧𝗔 |【𝗙𝗛𝗕】⁪⁬⁮")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Teletech_supportgroup")
PROJECT_NAME = getenv("PROJECT_NAME", "𝗗𝗔𝗥𝗞 𝗦𝗔𝗡𝗧𝗔 |【𝗙𝗛𝗕】⁪⁬⁮⁮")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("1908093917").split()))
