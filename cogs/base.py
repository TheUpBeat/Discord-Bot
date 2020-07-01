import discord
from discord.ext import commands

class Base(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Online!!")

    @commands.Cog.listener()
    async def on_memeber_join(self, member):

        # Enter the Channel id
        channel_id =


        channel = self.client.get_channel(channel_id)
        await channel.send("{} Welcome to the server. Hope you have a fun time".format(member))

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        # Enter the Channel id
        channel_id =


        channel = self.client.get_channel(channel_id)
        await channel.send("{} Sorry to see you leave.".format(member))


def setup(client):
    client.add_cog(Base(client))
