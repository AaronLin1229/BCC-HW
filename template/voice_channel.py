import os
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from discord.ext import commands
import discord
import asyncio
import nacl
import gtts

class Tts_features(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.channel = None

    @commands.command()
    async def print_info(self, ctx: Context, *, member: discord.Member = None):
        voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice_client:
            await ctx.send(f'{voice_client.channel}')
        else:
            await ctx.send(f'{voice_client}')

    @commands.command()
    async def join(self, ctx: Context, *, member: discord.Member = None):
        voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice_client:
            await ctx.send(f"I'm already in the voice channel {voice_client.channel},\nusing `{self.bot.command_prefix}leave` command first and then join me again!")
        elif ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            await ctx.send(f'Joining to channel {channel}.')
            await channel.connect()
        else:
            await ctx.send("You are not connected to a voice channel.")

    @commands.command()
    async def leave(self, ctx: Context, *, member: discord.Member = None):
        voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice_client:
            await ctx.send("I'm am not in a voice channel.")
        else:
            await ctx.send(f"Leaving channel {voice_client.channel}.")
            await ctx.voice_client.disconnect()

    @commands.command()
    async def tts_say(self, ctx: Context, *args, member: discord.Member = None):
        voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if not voice_client:
            await ctx.send("I'm am not in a voice channel.")
        else:
            # tts = gtts.gTTS(f"測試", lang="zh-TW")
            # tts.save(f'test.mp3')
            voice = ctx.channel.guild.voice_client
            voice.play(
                discord.FFmpegPCMAudio(executable="/Users/aaron/Coding/BCC-HW/template/ffmpeg", source="test.mp3")
                # after=lambda exc: ctx.bot.loop.run_until_complete(leave_vc(exc))
            )
