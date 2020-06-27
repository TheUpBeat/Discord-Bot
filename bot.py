import os
import discord
from discord.ext import commands
import time
import asyncio

client = commands.Bot(command_prefix = 'sudo ')


@client.command()
async def load(ctx, extension):
    client.load_extension('cogs.{}'.format(extension))

@client.command()
async def unload(ctx, extension):
    client.unload_extension('cogs.{}'.format(extension))

@client.command()
async def reload(ctx, extension):
    client.load_extension('cogs.{}'.format(extension))
    client.unload_extension('cogs.{}'.format(extension))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension('cogs.{}'.format(filename[:-3]))

# messages = joined = 0
#
# async def update_stats():
#     await client.wait_until_ready()
#     global messages, joined
#
#     while not client.is_closed():
#         try:
#             with open("stats.txt", "a") as f:
#                 f.write("Time: {}, Messages: {}, Mem joined: {}\n".format(int(time.time()), messages, joined))
#
#             messages = 0
#             joined = 0
#
#             await asyncio.sleep(5)
#         except Exception as e:
#             print(e)
#             await asyncio.sleep(5)
#
# @client.event
# async def on_member_join(member):
#     global joined
#     joined += 1
#
# @client.event
# async def on_message(message):
#     global messages
#     messages += 1
#
# client.loop.create_task(update_stats())

client.run('id') # id = Bot Token
