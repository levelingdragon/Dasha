from Dasha.events import dasha
from Dasha import StartTime
import time, datetime
from . import get_readable_time
from telethon import Button

@dasha(pattern="^/ping")
async def _(event):
    start_time = datetime.datetime.now()
    message = await event.edit("`Pinging..`")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b>Pong !! </b> <code>{}</code>\n"
        "<b>Uptime -</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
       
@dasha(pattern="^/repo$")
async def repo(event):
      await event.client.send_file(event.chat_id, file='Dasha/resources/Dasha.jpg', caption='click - **[Rᴇᴘᴏ](http://github.com/tamilvip007/dasha)**')

@dasha(pattern="^/alive$")
async def alive(event):
    chat = await event.get_chat()
    await event.delete()
    uptime = await get_readable_time((time.time() - StartTime))
    x = "**𝙳𝙰𝚂𝙷𝙰 𝙸𝚂 𝙰𝙻𝙸𝚅𝙴**\n\n"
    x += "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
    x += "✘ About My System ✘\n\n"
    x += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n"

    x += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n"
    x += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [Iɴᴅʀᴀᴊɪᴛʜ • 🇮🇳 • #AɪɴCʀᴀᴅ](tg://user?id=1633375527)\n"
    lol = await event.client.send_file(event.chat_id, file='Dasha/resources/Dasha.jpg', caption=x)

