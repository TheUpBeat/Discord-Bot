import base64
import discord
from discord.ext import commands

class Base64(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def encode(self, ctx, Title, *, msg):
        msg_bytes = msg.encode('ascii')
        base64_bytes = base64.b64encode(msg_bytes)
        base64_msg = base64_bytes.decode('ascii')

        embed = discord.Embed(
            colour = discord.Colour.green(),
            title = 'Base64 Encoded'
        )

        embed.add_field(name = Title, value = base64_msg, inline = False)
        await ctx.send(embed = embed)
        await ctx.message.delete()

    @commands.command()
    async def decode(self, ctx, *, msg):
        msg_bytes = msg.encode('ascii')
        base64_bytes = base64.b64decode(msg_bytes)
        base64_msg = base64_bytes.decode('ascii')

        embed_1 = discord.Embed(
            colour = discord.Colour.blue(),
            title = 'Base64 Decoded'
        )

        embed_1.add_field(name = 'Decoded Message', value = base64_msg, inline = False)
        await ctx.send(embed = embed_1)

def setup(client):
    client.add_cog(Base64(client))
