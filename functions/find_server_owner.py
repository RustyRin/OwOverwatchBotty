'''
Command to find the owner of the server
'''

from functions.bot_log import bot_log
import discord
from discord.ext import commands
import discord.utils


async def find_server_owner(ctx: discord.ext.commands.Context, client: discord.Client) -> discord.User:
    user_id: int = int(ctx.guild.owner_id)
    owner: discord.User = await client.fetch_user(user_id)
    bot_log(func1="functions/find_server_owner", desc=(owner.name + ' ' + str(owner.id)))
    return owner
