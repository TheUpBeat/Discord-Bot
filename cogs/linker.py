import os
import discord
from discord.ext import commands
from urllib.parse import *

class Convert(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        global count
        count = 0
        def checkLink(str):
            global count
            YT = 'https://www.youtube.com/'
            RT = 'https://reddit.com'
            YT_TO = 'https://www.invidio.us/'
            RT_TO = 'https://old.reddit.com'
            if (str == RT):
                url = RT_TO
                count = 1
                return url
            elif (str == RT_TO):
                url = RT
                count = 1
                return url
            elif str.startswith(RT):
                url = RT_TO + (urlparse(str).path)
                count = 1
                return url
            elif str.startswith(RT_TO):
                url = RT + (urlparse(str).path)
                count = 1
                return url
            elif (str == YT):
                count = 1
                url = YT_TO
                return url
            elif (str == YT_TO):
                count = 1
                url = YT
                return url
            elif str.startswith(YT):
                count = 1
                url = YT_TO +"watch" + "?" + (urlparse(i).query)
                return url
            elif str.startswith(YT_TO):
                count = 1
                url = YT + "watch" + "?" + (urlparse(i).query)
                return url
            else:
                count = 0

        if message.channel.id == "id":
            pass

        string = str(message.content)
        li = list(string.split(" "))
        for i in li:
            url = checkLink(str(i))
            channel = message.channel
            embed = discord.Embed(
                    colour = discord.Colour.green()
            )
            embed.add_field(name = 'Main Link', value = i,  inline = False)
            embed.add_field(name = 'Convert Link', value = (url), inline = False)
            if count == 1:
                try:
                    await channel.send(embed=embed)

                except Exception as e:
                    print(e)

def setup(client):
    client.add_cog(Convert(client))
