import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions, is_owner
import json

def getServerBalance(guild):
  with open("currency.json", "r") as f:
    serverBalance = json.load(f)
  try:
    x = serverBalance.get(str(guild))
    return x
  except:
    pass

class Economy(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.event
  async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)