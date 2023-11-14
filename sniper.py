import disnake
from disnake.ext import commands
import time
from webserver import keep_alive

TOKEN = 'token-here ><'

bot = commands.Bot(command_prefix='/', intents=disnake.Intents.default())

async def change_status():
        await bot.change_presence(activity=disnake.Game(name='[+] SNIPERSTATUS 🛠️'))
        time.sleep(10)
        while True:
          await bot.change_presence(activity=disnake.Game(name=' '))
          time.sleep(0.3)
          await bot.change_presence(activity=disnake.Game(name='  '))
          time.sleep(0.3)
          await bot.change_presence(activity=disnake.Game(name='   '))

@bot.event
async def on_ready():
    bot.loop.create_task(change_status())
    print('[+] ty for using sniperstatus ^^')
    time.sleep(0.2)
    print(f'[/] {bot.user.name} has connected to Discord!')
    time.sleep(0.7)
    print('[=] SniperStatus is working =)')
    time.sleep(0.7)
    print('[!] WARNING: SNIPERSTATUS WATERMARK IS GETTING FOR 10 SECONDS')
    time.sleep(0.4)
    print('[//] https://github.com/EcomateDev/SniperStatus')

keep_alive()
bot.run(TOKEN)
