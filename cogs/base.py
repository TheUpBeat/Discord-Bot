import discord
from discord.ext import commands

class Base(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Online!!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = client.get_channel(id)
        await channel.send('{} has the joined server'.format(member))

def setup(client):
    client.add_cog(Base(client))
