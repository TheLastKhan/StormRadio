import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.help_message = """
        ```
        General commands:
        h!help - displays all the available commands
        h!play <keywords> - finds the song on youtube
        h!queue - displays the current music queue
        h!skip - skips the current song being played
        h!clear - stops the music and clears the queue
        h!leave - disconnects the bot from the voice channel
        h!pause - pauses the current song being played
        h!resume - resumes playing the current song
        ```
        """
        
        self.text_channel_list = []
        self.channel_id = 1112451485788274769  # Replace with your specific channel ID
        
    @commands.Cog.listener()
    async def on_ready(self):
        channel = self.bot.get_channel(self.channel_id)
        if channel:
            self.text_channel_list.append(channel)
            # Comment out the following line to prevent the message from being sent automatically
            await self.send_to_all(self.help_message)
        else:
            print(f"Channel with ID {self.channel_id} not found.")
            
    async def send_to_all(self, msg):
        for text_channel in self.text_channel_list:
            await text_channel.send(msg)
                
    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)
