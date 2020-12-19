import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions, is_owner
import json

def getServerBalance(client, message):
  with open("currency.json", "r") as f:
    serverBalance = json.load(f)
  try:
    x = serverBalance.get(str(message.guild.id))
    return x
  except:
    pass

Class Economy(commands.Cog):
@bot.event
async def on_guild_join(guild):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)