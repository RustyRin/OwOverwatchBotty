from functions.bot_log import bot_log
import discord
from discord.ext import commands
import discord.utils


async def check_admin(ctx: discord.ext.commands.Context, client: discord.Client, user: discord.User|discord.Member|int|str) -> bool:

    guild = ctx.guild

    if type(user) is discord.User:
        user = guild.get_member(user.id)
    elif type(user) is int or type(user) is str:
        bot_log(func1="functions/check_admin", desc=f"Given id {user}")
        user = guild.get_member(int(user))
    if user.guild_permissions.administrator:
        return True
    else:
        return False
