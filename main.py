import discord
from discord.ext import commands, tasks
import os
import asyncio
from itertools import cycle
from config import  BOT_STATUS
from bottoken import BOT_TOKEN

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot_status = cycle(BOT_STATUS)


@tasks.loop(seconds=5)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(bot_status)))


@bot.event
async def on_ready():
    print('Bot sikeresen elindult!')
    change_status.start()
    try:
        sync_commands = await bot.tree.sync()
        print(f'Successfully registered {len(sync_commands)} commands')
    except Exception as e:
        print(f'Failed to register commands: {e}')


async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await load_extensions()
    async with bot:
        await bot.start(BOT_TOKEN)


asyncio.run(main())
