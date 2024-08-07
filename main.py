import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

from music_cog import MusicCog
from help_cog import HelpCog

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="h!", intents=intents)

bot.remove_command("help")

async def main():
    await bot.add_cog(MusicCog(bot))
    await bot.add_cog(HelpCog(bot))
    await bot.start(os.getenv("TOKEN"))

asyncio.run(main())
