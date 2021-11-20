from Dasha.events import dasha
from Dasha.modules.Sylviorus import update_gban as k
@dasha(pattern="[+]gban ?(.*)")
async def _(e):
 if e.is_reply:
   i=await e.reply('`Gbanning`')
   ok = await e.get_reply_message()
   sad = (e.pattern_match.group(1))
   send = (ok.sender.id)
   lol = (e.sender.id)
   await k(victim=send, reason=sad, message= ok.text, enforcer=lol)
   await i.edit('**Gbanned succesfully**')
 else:
   await e.reply('`Please reply to a message`')
