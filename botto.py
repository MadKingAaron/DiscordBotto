import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

import CustomBotClass

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_NAME= os.getenv('DISCORD_GUILD')


client = CustomBotClass.DiscordBottoClient()

client.run(TOKEN)