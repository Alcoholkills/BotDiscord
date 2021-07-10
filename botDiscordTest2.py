import discord
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
discordSection = config["DISCORD"]
botToken = discordSection["token"]
guildToken = discordSection["guildeid"]

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == guildToken:
            break
    print(f'{client.user} is connected to the following guild:\n{guild.name}(id:{guild.id})')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild members :\n - {members}')

client.run(botToken)
