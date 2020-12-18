import os
import discord
import random
import asyncio
from discord import Game
from discord.ext.commands import Bot

import keepAlive

BOT_PREFIX = ("fresh ")
TOKEN = os.getenv("token")

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command(name='hey',
                description="Greets the bot.",
                brief="Hey.",
                pass_context=True)
async def hi(context):
    await client.say("Hello, " + context.message.author.mention)


@client.command(name='referee',
                description="Initializes a referee and starts a timer for the duel.",
                brief="Summons the referee.",
                aliases=['ref', 'rf'],
                pass_context=True)
async def referee(context):
    refereeReplies = [
        'I\'m still on development so... Not yet, no.',
        'I\'m sorry, I know you need me but I have responsibilities too.',
    ]
    await client.say(context.message.author.mention + ", " + random.choice(refereeReplies))


@client.command(name='8ball',
                description="Sends your question out to space in hopes of receiving an answer.",
                brief="Answers from the universe.",
                aliases=['8b', 'eightball', '8-ball'],
                pass_context=True)
async def eightBall(context):
    eightBallReplies = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(eightBallReplies) + ", " + context.message.author.mention)


@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

keepAlive.keepAlive()

client.run(TOKEN)