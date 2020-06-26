import base64
import discord
from discord.ext import commands

class Base64(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == "id":
            msg = message.content
            channel = message.channel
            msg_bytes = msg.encode('ascii')
            base64_bytes = base64.b64encode(msg_bytes)
            base64_msg = base64_bytes.decode('ascii')

            embed = discord.Embed(
                colour = discord.Colour.green()
            )

            embed.add_field(name = 'Base64Encoded', value = base64_msg, inline = False)

            try:
                await channel.send(embed=embed)
                await message.delete()
            except Exception as e:
                print(e)

    @commands.command()
    async def decode(self, ctx, *, msg):
        msg_bytes = msg.encode('ascii')
        base64_bytes = base64.b64decode(msg_bytes)
        base64_msg = base64_bytes.decode('ascii')

        embed_1 = discord.Embed(
            colour = discord.Colour.blue()
        )

        embed_1.add_field(name = 'Decoded Message', value = base64_msg, inline = False)
        await ctx.send(embed = embed_1)

def setup(client):
    client.add_cog(Base64(client))
