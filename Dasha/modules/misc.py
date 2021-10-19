from Dasha.events import dasha
import speedtest
#Some misc modules

@dasha(pattern='^/stat')
async def stat(event):
      await event.edit(f'➤ 𝚃𝚘𝚝𝚊𝚕 𝙽𝚘 𝙾𝚏 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝙸𝚗 **{event.chat.title}** **:** `{event.id}`')

@dasha(pattern='^/test$')
async def test(event):
      s = speedtest.Speedtest()
      s.download()
      s.upload()
      x=s.results.share()
      await event.reply(file=x)