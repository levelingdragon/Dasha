from Dasha.events import dasha
import speedtest
#Some misc modules

@dasha(pattern='^/stat')
async def stat(event):
      await event.edit(f'➤ 𝚃𝚘𝚝𝚊𝚕 𝙽𝚘 𝙾𝚏 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝙸𝚗 **{event.chat.title}** **:** `{event.id}`')

@dasha(pattern='^/speedtest$')
async def test(event):
      lol=await event.edit('`Processing....`')
      s = speedtest.Speedtest()
      s.download()
      s.upload()
      x=s.results.share()
      await lol.delete()
      await event.reply(file=x)
      
@dasha(pattern="^/vdl$")
async def lmao(event):
      x=await event.get_reply_message()
      sex=await event.edit('`Downloading...`')
      await event.client.download_media(x,f'{x.id}.mp4')
      await sex.edit('`Media Successfully dowmloaded.`')