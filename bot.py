"""
OwOverwatch Botty

Python Discord Bot for my friends Overwatch (mostly) server

"""

# PyPi Packages
import discord
from discord.ext import commands
import discord.utils

try:
    with open("./database/secrets/discord.txt") as f:
        DISCORD_TOKEN = str(f.readline())
except FileNotFoundError:
    raise Exception("You did not make a Discord secrets file. Make one in \"./database/secrets/discord.txt\"")

bot_prefix = commands.when_mentioned_or("!ow")
bot_intents = discord.Intents.default()
discord_client = commands.Bot(
    command_prefix=bot_prefix,
    help_command=None,
    intents=bot_intents
)


@discord_client.event
async def on_ready():
    print("Bot running!")
    await discord_client.change_presence(status=discord.Status.online, activity=discord.Game("@me"))


discord_client.run(token=DISCORD_TOKEN)
