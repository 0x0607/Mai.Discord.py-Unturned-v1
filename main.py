import discord   # discord.py
import asyncio   
import requests  
import time      
token = "{discord.com/developers/applications's Token}"
unturnedServersAPI = "{unturned-servers.net's API}"
intents = discord.Intents.default()
intents.members = True
intents.messages = True
#====================================================================#
# 就緒
class client(discord.Client):
# 啟動
    async def on_ready(self):
        print('{} Ready.'.format(self.user))
        await self.get_info(unturnedServersAPI)
# 抓取玩家人數
    async def get_info(self, api):
        unturnedServersUrl = 'https://unturned-servers.net/api/?object=servers&element=detail&key='
        url = unturnedServersUrl + api
        try:
            oldPlayersCount = 0
            while True:
              response = requests.get(url)
              if response.status_code == 200:
                  unturned_status = response.json()
                  playersCount = str(unturned_status['players'])
                  # channel_id = 0
                  # channel = self.get_channel(channel_id)
                  # if channel and (oldPlayersCount != playersCount):
                  #     await channel.edit(name="【👥】ＵＮ-online: "+playersCount)
                  await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Unturned👥 '+playersCount+'/' + str(unturned_status['maxplayers'])),status=discord.Status('online'))
                  print('Online Players: {} '.format(playersCount ))
                  oldPlayersCount = playersCount
                  await asyncio.sleep(120)
        except requests.RequestException as e:
            print("Request Exception:", e)
#====================================================================#
# 執行
try: bot = client(intents=intents) # intents: Discord.intents
except:
    bot = client()
    print("You must enable privileged intent → https://discord.com/developers/applications/")
try: bot.run(token)    
except: exit()   
