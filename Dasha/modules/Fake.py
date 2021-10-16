#soon
from telethon import events
from Dasha import hbot

@hbot.on(events.NewMessage(pattern="[/]start"))
async def fuck(event):
      await hbot.send_message(event.chat_id, '/hunt for pokemon') 
