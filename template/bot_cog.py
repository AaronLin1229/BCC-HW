import os
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from discord.ext import commands
import discord
import asyncio
from decimal import *
import basic_features as basic
import voice_channel as advanced

class MyCommandBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged in as {0} ({0.id})'.format(self.user))

    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')
        await super().on_message(message)

async def create_bot():
    # Intents
    intents = discord.Intents.default()
    intents.message_content = True

    # Add commands by cog
    bot = MyCommandBot(command_prefix='!', intents=intents)
    await bot.add_cog(basic.Greetings(bot))
    await bot.add_cog(basic.Repeat(bot))
    await bot.add_cog(basic.Change(bot))
    await bot.add_cog(basic.Cal_gpa(bot))
    await bot.add_cog(advanced.Tts_features(bot))
    return bot

def main():
    load_dotenv()
    bot = asyncio.run(create_bot())
    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
