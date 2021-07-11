import discord
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
discordSection = config["DISCORD"]
botToken = discordSection["token"]

client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send("asagi !")

client.run(botToken)
