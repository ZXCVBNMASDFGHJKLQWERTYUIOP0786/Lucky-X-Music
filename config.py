import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps.
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","LuckyRaja0")
# Get Your bot username without @ 
BOT_USERNAME = getenv("BOT_USERNAME" , "LuckyXMusic_Bot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "𝐋𝚞𝚌𝚔𝚢🅧𝐌𝚞𝚜𝚒𝚌")
#get Your Assistant User name without @ 
ASSUSERNAME = getenv("ASSUSERNAME" , "LuckyXmusic")
EVALOP = list(map(int, getenv("EVALOP", "5993654715").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", 1001764180763))

# External APIs - Get these from their respective providers
GPT_API = getenv("GPT_API")
DEEP_API = getenv("DEEP_API")
PLAYHT_API = getenv("PLAYHT_API")
OWNER_ID = int(getenv("OWNER_ID", 5493923823))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ZXCVBNMASDFGHJKLQWERTYUIOP0786/Lucky-X-Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/LUCKYXUPDATE")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LUCKYXSUPPORT")


# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

# MaximuM limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "2500"))

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

# Get pyrogramv2 session from @Strings_Gen_Robot
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

AMBOT = [
    "💞", "🦋", "🔍", "🧪", "💖", "⚡️", "🔥", "❤️‍🔥", "🎩", "🌈", "🍷", "🥂", "👀", "🥃", "🥤", "🕊️", 
    "💔", "💘", "🎉", "🥀", "🌹", "❣️", "❤️", "🦋", "🪄", "💌", "💗", "💝", "🧨"
]

AMOP = ["      **🍷𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 {0}**🍷\n\n🌹𝐈 𝐀𝐦 𝐀𝐧 📀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 🎭 𝐀𝐧𝐝 🌱 𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 🌼 𝐕𝐂 🍄 𝐏𝐥𝐚𝐲𝐞𝐫 📣 𝐖𝐢𝐭𝐡 🕙 24𝐱7 🌀 𝐀𝐜𝐭𝐢𝐯𝐞 » 𝐅𝐨𝐫 🗨️ 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 ♨️ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🎸 𝐀𝐧𝐝 🏓 𝐆𝐫𝐨𝐮𝐩𝐬 🎻\n\n💐𝐅𝐞𝐞𝐥 😍 𝐋𝐚𝐠 📍 𝐅𝐫𝐞𝐞 😇 𝐓𝐨 🕊️ **𝐀𝐝𝐝 𝐌𝐞 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩** 🤖 𝐀𝐧𝐝 🩸 𝐄𝐧𝐣𝐨𝐲 ❥︎ 𝐒𝐮𝐩𝐞𝐫 💥 𝐇𝐢𝐠𝐡 💫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 🦞 𝐀𝐮𝐝𝐢𝐨 🎧 𝐀𝐧𝐝 🔊 𝐕𝐢𝐝𝐞𝐨 🌷\n\n🏓 𝐆𝐑𝐎𝐔𝐏  ➪ **[ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://t.me/LuckyXSupport) 💞**\n📡 𝐌𝐚𝐝𝐞 𝐁𝐲 ➪ **[𝙻𝚄𝙲𝙺𝚈 ✯ 𝚁𝙰𝙹𝙰](https://t.me/LuckyRaja0)** 💞""",
      "ʜᴇʟʟᴏ {0}, 🥀\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [🇯𝗔𝗥𝗩𝗜𝗦💗](https://t.me/LuckyRaja0)""",
        "ʜɪɪ, {0} ~\n\n◆ ɪ'ᴍ ᴀ {1} ᴛᴇʟᴇɢʀᴀᴍ ꜱᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴡɪᴛʜ ꜱᴏᴍᴇ ᴜꜱᴇꜰᴜʟ\n◆ ᴜʟᴛʀᴀ ғᴀsᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ꜰᴇᴀᴛᴜʀᴇꜱ.\n\n✨ ꜰᴇᴀᴛᴜʀᴇꜱ ⚡️\n◆ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.\n◆ Sᴜᴘᴇʀғᴀsᴛ ʟᴀɢ Fʀᴇᴇ ᴘʟᴀʏᴇʀ.\n◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ.\n◆ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍɪɴɢ.\n◆ ɴᴏ ᴘʀᴏᴍᴏ.\n◆ ʙᴇꜱᴛ ꜱᴏᴜɴᴅ Qᴜᴀʟɪᴛʏ.\n◆ 24×7 ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ.\n◆ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴀᴅᴍɪɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴍᴜꜱɪᴄ 🎵.\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [🇯𝗔𝗥𝗩𝗜𝗦💗](https://t.me/LuckyRaja0)""",
        "ʜᴇʟʟᴏ {0}, 🥀\n\n ɪᴛ'ꜱ ᴍᴇ {1} !\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ꜱᴜᴘᴘᴏʀᴛɪɴɢ ᴘʟᴀᴛꜰᴏʀᴍꜱ : ʏᴏᴜᴛᴜʙᴇ, ꜱᴘᴏᴛɪꜰʏ,\n┠ ◆ ʀᴇꜱꜱᴏ, ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ , ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ ᴇᴛᴄ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [🇯𝗔𝗥𝗩𝗜𝗦💗](https://t.me/LuckyRaja0)""",
        "ʙᴀʙʏ {0},\n ᴍʏ ꜱᴇʟꜰ {1} ..\n{1} ꜱʏꜱ ꜱᴛᴀᴛꜱ\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ➥ Uᴘᴛɪᴍᴇ : {2}\n┠ ➥ SᴇʀᴠᴇʀSᴛᴏʀᴀɢᴇ : {3}\n┠ ➥ CPU Lᴏᴀᴅ : {4}\n┠ ➥ RAM Cᴏɴsᴜᴘᴛɪᴏɴ : {5}\n┠ ➥ ᴜꜱᴇʀꜱ : {6}\n┠ ➥ ᴄʜᴀᴛꜱ : {7}\n┗━━━━━━━━━━━━━━━━━⧫\n\nᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [🇯𝗔𝗥𝗩𝗜𝗦💗](https://t.me/LuckyRaja0)""",
        "ʜᴇʏ, {0} \nɪ'ᴍ {1},\n\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs.\n┠ ◆ ᴀʟʟ-ɪɴ-ᴏɴᴇ ʙᴏᴛ.\n┗━━━━━━━━━━━━━━━━━⧫\n┏━━━━━━━━━━━━━━━━━⧫\n┠ ◆ ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.\n┠ ◆ ʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ɪᴍᴀɢᴇs.\n┠ ◆ ʏᴏᴜ ᴄᴀɴ ᴛʀᴀɴꜱʟᴀᴛᴇ ᴍᴜʟᴛɪᴘʟᴇ ʟᴀɴɢᴜᴀɢᴇꜱ.\n┠ ◆ ɪ ᴄᴀɴ ᴍᴜᴛᴇ,ᴜɴᴍᴜᴛᴇ,ʙᴀɴ,ᴜɴʙᴀɴ,ᴋɪᴄᴋ..\n┠ ◆ ꜱᴘᴇᴄɪᴀʟ ᴡᴇʟᴄᴏᴍᴇ \n┠ ◆ ᴍᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ᴄʟɪᴄᴋ ᴄᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ...\n┗━━━━━━━━━━━━━━━━━⧫\n๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.\n\n🫧 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🪽 ➪ [🇯𝗔𝗥𝗩𝗜𝗦💗](https://t.me/LuckyRaja0)""",
        "╭───────────────────⦿\n│🍁 ▸ 𝐇ᴇʏ {0} \n│🤍 ▸ 𝐈 𝐀ᴍ {1} \n├───────────────────⦿\n│🖤 ▸ 𝐈 𝐇ᴀᴠᴇ 𝐒ᴘᴇᴄɪᴀʟ 𝐅ᴇᴀᴛᴜʀᴇs\n│🤎️ ▸ 𝐀ʟʟ-𝐈ɴ-𝐎ɴᴇ 𝐁ᴏᴛ\n├───────────────────⦿\n│❤️ ▸ 𝐁ᴏᴛ 𝐅ᴏʀ 𝐓ᴇʟᴇɢʀᴀᴍ 𝐆ʀᴏᴜᴘs\n│🧡 ▸ 𝐂ʜᴀᴛ-𝐁ᴏᴛ + 𝐌ᴜsɪᴄ-𝐁ᴏᴛ\n│💛 ▸ 𝐘ᴏᴜ 𝐂ᴀɴ 𝐏ʟᴀʏ 𝐌ᴜꜱɪᴄ + 𝐕ɪᴅᴇᴏ\n│💚 ▸ 𝐆ᴇɴᴇʀᴀᴛᴏʀ 𝐈ᴍᴀɢᴇs + 𝐓ᴀɢ 𝐀ʟʟ\n│💙️ ▸ 𝐖ᴇʟᴄᴏᴍᴇ + 𝐋ᴇғᴛ 𝐍ᴏᴛɪᴄᴇ\n│💜 ▸ 24x7 𝐎ɴʟɪɴᴇ 𝐒ᴜᴘᴘᴏʀᴛ\n├───────────────────⦿\n│🍷 𝐓ᴀᴘ 𝐓ᴏ 𝐂ᴏᴍᴍᴀɴᴅs 𝐌ʏ 𝐃ᴇᴀʀ\n╰───────────────────⦿ 🥀 𝐒ᴏᴜꝛᴄᴇ 🥀 ➥ [𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ](https://t.me/LuckyRaja0) ♡\n"""
       ]

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/fdbffdb39d20374823466.jpg"
)
PING_VID_URL = getenv(
    "PING_VID_URL", "https://telegra.ph/file/4be43ed2aa6872337e9a8.mp4"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/94e9eca3b0ec6e2dc6cd5.png"
STATS_IMG_URL = "https://telegra.ph/file/9f3613d95078ff5f81120.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/ef5bdba78c475a9e50d24.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/c8db17e1612487be13571.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/6a81d918bd5d44c646205.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/1470316a51382cc446fe1.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/06679f04da4b2fbbb12d0.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
