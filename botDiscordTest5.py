import discord
import configparser
import random

from discord.ext import commands
from discord.flags import Intents

config = configparser.ConfigParser()
config.read("config.ini")
discordSection = config["DISCORD"]
botToken = discordSection["token"]

# intents = discord.Intents.default()
intents = discord.Intents(messages=True, guilds=True, members=True)

bot = commands.Bot(command_prefix='!', intents=intents)
# bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
@bot.command(name="members", help="List all guild members")
async def members(ctx):
    response = "Here's a list of all members:\n"
    for guildMember in bot.get_all_members():
        response += f" - {guildMember}\n"
    await ctx.send(response)

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
        
@bot.command(name="rshifumi", help="A genius cannot lose this simple game called shifumi")
async def rshifumi(ctx, hand = ""):
    moveListe = {"paper":"cissors", "cissors":"stone", "stone":"paper"}
    if hand == "":
        await ctx.send("You need to play something ; scared of losing ?'")
        return
    if hand not in moveListe:
        await ctx.send("Not a legal move, please try 'paper', 'cissors', 'stone'\nAre you trying to cheat ?")
        return
    await ctx.send(f"I use {moveListe[hand]}\nSorry, you lose ; but you had no chance ...")
    
# Faire un blackjack
# @bot.command(name="blackjack", help="Play a game of blackjack with me !\nDraw cards (!d) until you you want to stop (!s) and try to get 21.\nI'll play after you, and the winner is the closest to 21.\nIf you go over 21, you automatically lose !!")
# async def blackjack(ctx):
#     await ctx.send("Blackjack starts ; start to draw cards with !d, and stop with !s")
#     @bot.command(name="d")
#     return    
    
    

bot.run(botToken)
