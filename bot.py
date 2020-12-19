import os
import random
import asyncio
from dotenv import load_dotenv
import discord
from discord import Game
from discord.ext import commands

import keepAlive

load_dotenv()
TOKEN = os.getenv("token")

bot = commands.Bot(command_prefix="fresh, ")

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="fresh, help"))
  print('We have logged in as {0.user}'.format(bot))

@bot.command(description="Performs complex calulations to ensure that ping is definitely pong.",
              brief="Pong")
async def ping(context):
	await context.channel.send("Pong")

@bot.command(name='hey',
                description="Greets the bot",
                brief="Hey")
async def hey(context):
  await context.channel.send("Heyo, " + context.author.mention)

@bot.command(name='8ball',
                description="Sends your question out to space in hopes of receiving an answer.",
                brief="Gives answers from the universe",
                aliases=['8b', 'eightball', '8-ball'],
                pass_context=True)
async def eightBall(context, question):
  eightBallReplies = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'Definitely',
  ]
  await context.channel.send(random.choice(eightBallReplies) + ", " + context.message.author.mention)

#@bot.command(name='referee',
#                description="Initializes a referee and starts a timer for the duel.\n"
#                            + "Usage: eb referee [@player]",
#                brief="Summons the referee.",
#                aliases=['ref', 'rf'],
#                pass_context=True)
#async def referee(context):
#    refereeReplies = [
#        'I\'m still on development so... Not yet, no.',
#        'I\'m sorry, I know you need me but I have responsibilities too.',
#    ]
#    await context.channel.send(context.message.author.mention + ", " + random.choice(refereeReplies))

@bot.command(description="Borrows computing power from NASA's supercomputer to calculate the result of multiplying a number by itself.",
                brief="Gives the square of a number",)
async def square(context, number: int):
  await context.channel.send(str(number) + " squared is " + str(number^2))

@bot.event
async def on_message(context):
  praiseReplies = [
        'Thanks, boss!',
        '*wags tail happily*',
        "Okay, but where's my treat?",
        'Aww, love you too.',
        '*wags tail happily*',
        '*wags tail happily*',
        'Thanks, boss!',
    ]

  if context.author == bot.user:
    return

  if context.content.startswith('good bot, fresh'):
    await context.channel.send(random.choice(praiseReplies))

  await bot.process_commands(context)

keepAlive.keepAlive()

bot.run(TOKEN)