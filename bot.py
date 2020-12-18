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

bot = commands.Bot(command_prefix="fresh ")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ping(context):
	await context.channel.send("pong")

@bot.command(name='hey',
                description="Greets the bot.",
                brief="Hey.",
                pass_context=True)
async def hey(context):
    await context.channel.send("Heyo, " + context.message.author.mention)

@bot.command(name='8ball',
                description="Sends your question out to space in hopes of receiving an answer.\n"
                            + "Usage: eb 8ball [question]",
                brief="Answers from the universe.",
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

@bot.command()
async def square(context, number):
    squared_value = int(number) * int(number)
    await context.channel.send(str(number) + " squared is " + str(squared_value))

@bot.event
async def on_message(context):
    if context.author == bot.user:
        return

    if context.content.startswith('$hello'):
        await context.channel.send('Hello!')

    await bot.process_commands(context)

keepAlive.keepAlive()

bot.run(TOKEN)