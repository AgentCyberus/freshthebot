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

    #loads nick.json file
    with open("./cogs/nick.json") as f:
      nick = json.load(f)

    if not str(f"{context.guild.id}") in nick["nicknames"]:
      guildID = {
        context.guild.id: {
          "server_name": context.guild.name,
          "member_nicks": {}
        }
      }
      nick["nicknames"].update(guildID)
      await context.send(f"Guild file has been created for {context.guild.name}")
        
    if message is not None:
      try:
        userNick = nick["nicknames"][f"{context.guild.id}"]["member_nicks"][f"{context.author.id}"]
        print(userNick)
        nick["nicknames"][f"{context.guild.id}"]["member_nicks"][f"{context.author.id}"] = message
      except KeyError:
        nick["nicknames"][f"{context.guild.id}"]["member_nicks"].update({context.author.id: message})
    else:
      try:
        userNick = nick["nicknames"][f"{context.guild.id}"]["member_nicks"][f"{context.author.id}"]
        await context.send(userNick) 
      except KeyError:
        await context.send(f"You have no nickname set, {context.author.mention}") 

    
    with open("./cogs/nick.json", "w") as fw:
      json.dump(nick, fw, indent=2)

def setup(bot):
  bot.add_cog(Personalization(bot))