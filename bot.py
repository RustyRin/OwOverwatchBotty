"""
OwOverwatch Botty

Python Discord Bot for my friends Overwatch (mostly) server

"""

# PyPi Packages
import discord
from discord.ext import commands
import discord.utils

# Internal functions
from functions.bot_log import bot_log
from functions.find_server_owner import find_server_owner

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

'''
COMMANDS
'''


@discord_client.command()
async def ping(ctx):
    """Command to tell user the bot ping in ms"""
    bot_log(func1="bot/commands/ping")
    await ctx.send(f'Pong! {int(discord_client.latency * 1000)} ms')


@discord_client.command(aliases=["owner"])
async def server_owner(ctx):
    """Tells user who the owner of the current sever is"""
    owner: discord.User = await find_server_owner(ctx, client=discord_client)
    await ctx.send('The owner of ' + ctx.guild.name + ' is ' + owner.mention)


@discord_client.event
async def on_ready():
    bot_log(func1="On Ready", desc="Bot is running!")
    await discord_client.change_presence(status=discord.Status.online, activity=discord.Game("@me"))


discord_client.run(token=DISCORD_TOKEN)
