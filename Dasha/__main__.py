from Dasha import ubot, tbot, dbot, xbot, hbot, TOKEN_2, TOKEN, abot, bbot, cbot
import Dasha.events
import sys

try:
  dbot.start()
  xbot.start()
  ubot.start()
  abot.start()
  cbot.start()
  bbot.start() 
  tbot.start(bot_token=TOKEN)
  hbot.start(bot_token=TOKEN_2)
except:
  print("Invalid STRING/Token__bot exiting...")
 # sys.exit()
  
ubot.run_until_disconnected()
xbot.run_until_disconnected()
abot.run_until_disconnected()
bbot.run_until_disconnected()
cbot.run_until_disconnected()
dbot.run_until_disconnected()
tbot.run_until_disconnected()
hbot.run_until_disconnected()
