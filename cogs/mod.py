import discord
from discord.ext import commands

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, ammount=1):
        channel = ctx.message.channel
        if ctx.message.author.guild_permissions.administrator:
            await channel.purge(limit=ammount,check=None,bulk=True)
        else:
            await ctx.send("You can't use that command, you are not an administrator!")
            await ctx.message.delete()


def setup(client):
    client.add_cog(Mod(client))
