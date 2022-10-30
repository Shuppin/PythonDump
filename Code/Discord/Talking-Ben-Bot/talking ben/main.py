import nextcord as discord
from nextcord.ext import commands
import os
import json

defaultPrefix = '-'

dev = "Shuppin#0001"

activity = discord.Activity(type=discord.ActivityType.watching, name="https://youtu.be/jXF2mV-KnLE")
bot = commands.Bot(command_prefix="496683edcda77d13cfd2a5c6c3047fcee1ae9284d352db594af124d9fd139743",activity=activity, status=discord.Status.online)

# prefix is sha256 hash of "talkingben" // this is to prevent (mostly) everyone from calling any command from the bot

for filename in os.listdir('talking ben/modules'):
  if filename.endswith(".py"):
    bot.load_extension(f"modules.{filename[:-3]}")

bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as "{bot.user.name}" ({bot.user.id})')
    print("Running on discord", discord.__version__)
    print('------')

    print(f'Servers connected to: ({len(bot.guilds)} servers)')
    for guild in bot.guilds:
        print(f'{guild.name} ({guild.id}) - {guild.member_count} Members')


bot.run("token") # production
