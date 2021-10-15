from Dasha.events import dasha

#Some misc modules

@dasha(pattern='^/stat')
async def stat(event):
      await event.edit(f'【 𝚃𝚘𝚝𝚊𝚕 𝙽𝚘 𝙾𝚏 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝙸𝚗 **{event.chat.title}** ➣ `{event.id}` 】')

