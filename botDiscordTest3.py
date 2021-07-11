import discord
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
discordSection = config["DISCORD"]
botToken = discordSection["token"]



class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        
client = CustomClient()
client.run(botToken)
