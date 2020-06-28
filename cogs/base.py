import discord
from discord.ext import commands

class Base(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot Online!!")

    @commands.Cog.listener()import discord
    from discord.ext import commands
    import base64

    class Base(commands.Cog):

        def __init__(self, client):
            self.client = client

        @commands.Cog.listener()
        async def on_ready(self):
            print('Bot is ready')

        @commands.Cog.listener()
        async def on_memeber_join(self, member):
            channel = self.client.get_channel(726726039937482814)
            await channel.send("{} Welcome to the server. Hope you have a fun time".format(member))

        @commands.Cog.listener()
        async def on_member_remove(self, member):
            channel = self.client.get_channel(726726039937482814)
            await channel.send("{} Sorry to see you leave.".format(member))

    # To kick or ban
        @commands.command()
        async def kick(self, ctx, member : discord.Member, *, reason=None):
            if ctx.message.author.guild_permissions.administrator:
                await member.kick(reason=reason)
                await ctx.send('Kicked {}'.format(member.mention))
            else:
                await ctx.send("You are not authorized to do so.")
                await ctx.message.delete()

        @commands.command()
        async def ban(self, ctx, member : discord.Member, *, reason=None):
            if ctx.message.author.guild_permissions.administrator:
                await member.ban(reason=reason)
                await ctx.send('Banned {}'.format(member.mention))
            else:
                await ctx.send("Hol' up a min. You are not permitted to do this.")
                await ctx.message.delete()


        # Unban command
        @commands.command()
        async def unban(self, ctx, *, member):
            if ctx.message.author.guild_permissions.administrator:
                ban_users = await ctx.guild.bans()
                member_name, member_dis = member.split('#')

                for ban_entry in ban_users:
                    user = ban_entry.user

                    if (user.name, user.discriminator) == (member_name, member_dis):
                        await ctx.guild.unban(user)
                        await ctx.send('Unbanned {}'.format(user.mention))
                        return
            else:
                await ctx.send("Just dont do this, You are not allowed.")
                await ctx.message.delete()


    def setup(client):
        client.add_cog(Base(client))

    async def on_member_join(self, member):
        channel = client.get_channel(id)
        await channel.send('{} has the joined server'.format(member))

def setup(client):
    client.add_cog(Base(client))
