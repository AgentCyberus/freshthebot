import discord
from discord.ext import commands
import json


class Personalization(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(description="Display or change your nickname.",
                brief="Display or change your nickname.",
                aliases=['nick', 'nn'])
  async def nickname(self, context, message : str = None):
    with open("./cogs/nick.json", "r") as f:
      nick = json.load(f)
    if not str(f"{context.guild.id}") in nick:
      nick[f"{context.guild.id}"] = {}
      #await context.send(f"Guild file has been created for {context.guild.id}/{context.guild.name}")
    #else:
    #  await context.send(f"Guild file exists for {context.guild.id}/{context.guild.name}")

    if message is not None:
      nick[f"{context.guild.id}"] = {context.author.id : message}
      #await context.send(f"Nickname set for {context.author.name}: {message}")
    else:
      if str(f"{context.author.id}") not in nick[f"{context.guild.id}"]:
        nick[f"{context.guild.id}"] = {context.author.id : context.author.name}

    f.close()
    
    with open("./cogs/nick.json", "w") as fw:
      json.dump(nick, fw)

    if message is None:
      with open("./cogs/nick.json", "r") as f1:
        nick = json.load(f1)
      await context.send(nick[f"{context.guild.id}"][f"{context.author.id}"])
      f1.close

def setup(bot):
  bot.add_cog(Personalization(bot))