import discord
import configparser
import random

from discord.ext import commands

config = configparser.ConfigParser()
config.read("config.ini")
discordSection = config["DISCORD"]
botToken = discordSection["token"]

bot = commands.Bot(command_prefix='!')

# bot = discord.Client()
# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
    
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         print("on_message - return")
#         return
#     print("on_message - await")
#     await message.channel.send("asagi !")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='boo', help='Try your luck at this lucky scary draw ;)')
async def booFunc(ctx):
    listResponse = ["A boo !", "PikaBoo", "Pikapika", "Asagi !"]
    response = random.choice(listResponse)
    print(response)
    print("booFunc - await")
    await ctx.send(response)
    
@bot.command(name="rollMe", help="Try your luck and bet me at a dice roll !")
async def rollMe(ctx):
    memberRoll = random.randint(1,6)
    botRoll = random.randint(1,6)
    response = f'You rolled a {memberRoll}\nI rolled a {botRoll}\n'
    if memberRoll > botRoll:
        response += "You win !"
    elif botRoll > memberRoll:
        response += "I win you scrub !!"
    else:
        response += "I guess it's time for rematch !"
    await ctx.send(response)

@bot.command(name="rrollMe", help="Try your luck and bet me with my dice roll !!")
async def rrollMe(ctx):
    memberRoll = random.randint(1,6)
    botRoll = 6
    response = f'You rolled a {memberRoll}\n'
    if memberRoll < botRoll:
        botRoll = memberRoll + 1
    response += f'I rolled a {botRoll}\n'
    if memberRoll == botRoll:
        response += "I guess you are lucky. But you coward don't stand a chance against me !!"
    else:
        response += "This is easy win :D !!"
    await ctx.send(response)

@bot.command(name="shifumi", help="Play a game of shifumi with me :D ; play 'paper', 'cissors', 'stone'")
async def shifumiMe(ctx, hand = "") :
    # A faire avec un dictionnaire
    moveListe = {"paper":"cissors", "cissors":"stone", "stone":"paper"}
    if hand == "":
        await ctx.send("You need to play something !!'")
        return
    if hand not in moveListe:
        await ctx.send("Not a legal move, please try 'paper', 'cissors', 'stone'")
        return
    botRoll = random.choice(list(moveListe.keys()))
    if botRoll == hand:
        await ctx.send(f"I use {botRoll}\nNo winner today ^-^")
    elif moveListe[hand] == botRoll:
        await ctx.send(f"I use {botRoll}\nYou lose :p !")
    else:
        await ctx.send(f"I use {botRoll}\nYou're an instopalbe winner ;D !!")
        
    
    
# Faire un blackjack
    
    
    

bot.run(botToken)
