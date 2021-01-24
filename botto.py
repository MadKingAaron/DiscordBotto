import os
import discord
from discord.ext import commands
# from dotenv import load_dotenv

import CustomBotClass

# load_dotenv()

# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD_NAME= os.getenv('DISCORD_GUILD')


TOKEN = "ODAyMzg1NTY3ODc4MjE3NzM4.YAudyg.yibfMuCO_JdBJ_pD2ZH2OtKfUsw"
client = CustomBotClass.DiscordBottoClient()

client.run(TOKEN)