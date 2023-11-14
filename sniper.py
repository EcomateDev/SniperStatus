import disnake
from disnake.ext import commands
import asyncio
from webserver import keep_alive

TOKEN = 'token-here ><'

bot = commands.Bot(command_prefix='/', intents=disnake.Intents.default())

async def change_status():
    await bot.change_presence(activity=disnake.Game(name='[+] SNIPERSTATUS 🛠️'))
    await asyncio.sleep(3)
    while True:
        for _ in range(10):
            await bot.change_presence(activity=disnake.Game(name=' '))
            await asyncio.sleep(2)
            await bot.change_presence(activity=disnake.Game(name='  '))
            await asyncio.sleep(2)
            await bot.change_presence(activity=disnake.Game(name='   '))
            await asyncio.sleep(2)

@bot.event
async def on_ready():
    bot.loop.create_task(change_status())
    print('[+] Thank you for using SniperStatus!')
    print(f'[/] {bot.user.name} has connected to Discord!')
    print('[=] SniperStatus is working =)')
    print('[!] WARNING: SNIPERSTATUS WATERMARK IS APPEARING FOR 3 SECONDS')
    print('[//] https://github.com/EcomateDev/SniperStatus')
    print('[//] https://www.patreon.com/EcomateDev')

keep_alive()
bot.run(TOKEN)
