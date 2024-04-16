import math
from typing import Union
from pyrogram.types import InlineKeyboardButton

from LuckyX.utils.formatters import time_to_seconds

from LuckyX import app

def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            )
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥𝐎𝚆𝙽𝙴𝚁❤️‍🔥", url=f"tg://openmessage?user_id={OWNER_ID}",
            ),
            InlineKeyboardButton(
                text="💝𝐉𝙰𝙰𝙽💝", url=f"https://t.me/Badnam_Mohabbat",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    top = math.floor(percentage)
    if 0 < top <= 10:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ❤️"
    elif 10 < top < 20:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ❤️٨ـ"
    elif 20 <= top < 30:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـ❤️ﮩﮩ٨ـ"
    elif 30 <= top < 40:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨❤️ـﮩﮩ٨ـ"
    elif 40 <= top < 50:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ❤️٨ـﮩﮩ٨ـ"
    elif 50 <= top < 60:
        bar = "ﮩ٨ـﮩﮩ٨❤️ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= top < 70:
        bar = "ﮩ٨ـﮩ❤️ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 70 <= top < 80:
        bar = "ﮩ٨❤️ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= top < 95:
        bar = "ﮩ❤️٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    else:
        bar = "❤️ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="❣️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="❤️", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="💞", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="💔", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="❤️‍🩹", callback_data=f"ADMIN Stop|{chat_id}")
        
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons

def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "◉—————————"
    elif 10 < umm < 20:
        bar = "—◉————————"
    elif 20 <= umm < 30:
        bar = "——◉———————"
    elif 30 <= umm < 40:
        bar = "———◉——————"
    elif 40 <= umm < 50:
        bar = "————◉—————"
    elif 50 <= umm < 60:
        bar = "—————◉————"
    elif 60 <= umm < 70:
        bar = "——————◉———"
    elif 70 <= umm < 80:
        bar = "———————◉——"
    elif 80 <= umm < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"
    buttons = [
        
        [
            InlineKeyboardButton(text=f"{played} {bar} {dur}", callback_data="GetTimer",)
        ],
          [
            InlineKeyboardButton(text="▷ ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}",),
            InlineKeyboardButton(text="sᴋɪᴘ ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="▢ sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ ↺", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="๏ ᴍᴏʀᴇ ๏", callback_data=f"PanelMarkup None|{chat_id}",),
        ],
    ]

    return buttons

def stream_markup(_, chat_id):
    buttons  = [

        [
            InlineKeyboardButton(text="▷ ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}",),
            InlineKeyboardButton(text="sᴋɪᴘ ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            
        ],
        [
            InlineKeyboardButton(text="▢ sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ ↺", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="๏ ᴍᴏʀᴇ ๏", callback_data=f"PanelMarkup None|{chat_id}",),
        ],
    ]

    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"RajaPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"RajaPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text=_["✧ᴄʟᴏsᴇ✧"], callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        
        [
            InlineKeyboardButton(text=_["P_B_3"], callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text=_["✧ᴄʟᴏsᴇ✧"], callback_data=f"forceclose {videoid}|{user_id}"),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}"),
        ],
        [
            InlineKeyboardButton(text="◁", callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",),
            InlineKeyboardButton(text=_["✧ᴄʟᴏsᴇ✧"], callback_data=f"forceclose {query}|{user_id}",),
            InlineKeyboardButton(text="▷", callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",),
        ],
     ]
    return buttons

## Telegram Markup

def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text= "๏ ɴᴇxᴛ ๏", callback_data=f"PanelMarkup None|{chat_id}",),
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons
        
## Queue Markup

def queue_markup(_, videoid, chat_id):

    buttons = [
        
          [
            InlineKeyboardButton(text="II ᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}",),
            InlineKeyboardButton(text="▢ sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="sᴋɪᴘ ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="▷ ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ ↺", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="๏ ᴍᴏʀᴇ ๏", callback_data=f"PanelMarkup None|{chat_id}"),
        ],
    ]

    return buttons



                
def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text= "✚ ᴀᴅᴅ ɪɴ ʏᴏᴜʀ ᴘʟᴀʏʟɪsᴛ ✚", callback_data=f"add_playlist {videoid}")
        ],
        [
            InlineKeyboardButton(text="🎧 sᴜғғʟᴇ", callback_data=f"ADMIN Shuffle|{chat_id}",),
            InlineKeyboardButton(text="ʟᴏᴏᴘ ↺", callback_data=f"ADMIN Loop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="◁ 10 sᴇᴄ", callback_data=f"ADMIN 1|{chat_id}",),
            InlineKeyboardButton(text="10 sᴇᴄ ▷", callback_data=f"ADMIN 2|{chat_id}",),
        ],
        [
            InlineKeyboardButton(text="๏ ʜᴏᴍᴇ ๏", callback_data=f"MainMarkup {videoid}|{chat_id}",),
            InlineKeyboardButton(text="๏ ɴᴇxᴛ ๏", callback_data=f"Pages Forw|0|{videoid}|{chat_id}",),
        ],
    ]
    return buttons


def panel_markup_2(_, videoid, chat_id):
    buttons = [
       
        [
                InlineKeyboardButton(text="🕒 0.5x", callback_data=f"SpeedUP {chat_id}|0.5",),
                InlineKeyboardButton(text="🕓 0.75x", callback_data=f"SpeedUP {chat_id}|0.75",),
                InlineKeyboardButton(text="🕤 1.0x", callback_data=f"SpeedUP {chat_id}|1.0",),
            ],
            [
                InlineKeyboardButton(text="🕤 1.5x", callback_data=f"SpeedUP {chat_id}|1.5",),
                InlineKeyboardButton(text="🕛 2.0x", callback_data=f"SpeedUP {chat_id}|2.0",),
            ],
        [
            InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data=f"Pages Back|1|{videoid}|{chat_id}",),
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
                InlineKeyboardButton(text="🕒 0.5x", callback_data=f"SpeedUP {chat_id}|0.5",),
                InlineKeyboardButton(text="🕓 0.75x", callback_data=f"SpeedUP {chat_id}|0.75",),
                InlineKeyboardButton(text="🕤 1.0x", callback_data=f"SpeedUP {chat_id}|1.0",),
            ],
            [
                InlineKeyboardButton(text="🕤 1.5x", callback_data=f"SpeedUP {chat_id}|1.5",),
                InlineKeyboardButton(text="🕛 2.0x", callback_data=f"SpeedUP {chat_id}|2.0",),
            ],
        [
            InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data=f"Pages Back|2|{videoid}|{chat_id}",),
        ],
    ]
    return buttons
