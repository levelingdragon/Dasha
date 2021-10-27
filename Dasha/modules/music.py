import asyncio
from Dasha import xbot,tbot
from telethon import Button
from Dasha.events import dasha
from pytgcalls import GroupCallFactory

@dasha(pattern="^/vplay$")
async def vid(event):
   call = GroupCallFactory(xbot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON).get_group_call()
   lol=await event.get_reply_message()
   x=await tbot.send_message(event.chat_id,'`Downloading....`',reply_to=event)
   s=await xbot.download_media(lol)
   await call.start(event.chat_id)
   await call.start_video(s)
  
@dasha(pattern="^/aplay$")
async def audio(event):
   call = GroupCallFactory(xbot, GroupCallFactory.MTPROTO_CLIENT_TYPE.TELETHON).get_group_call()
   lol=await event.get_reply_message()
   x=await tbot.send_message(event.chat_id,'`Downloading....`',reply_to=event)
   ok=await xbot.download_media(lol)
   await call.start(event.chat_id)
   await call.start_audio(ok)
   await x.delete()
   await tbot.send_message(event.chat_id, '`Playing.....`', file='https://telegra.ph//file/82c68cdadd6b06ca2b8be.jpg', buttons=[Button.url('Source',f'http://t.me/c/{(lol.chat.id)}/{(lol.id)}'), Button.url('Support', 't.me/Dashasupport')],reply_to=event)
