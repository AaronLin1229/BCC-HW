import os
from discord.ext.commands.context import Context
from dotenv import load_dotenv
from discord.ext import commands
import discord
import asyncio
from decimal import *

class Greetings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx: Context, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f'Hello {member.name}~')
        else:
            await ctx.send(f'Hello {member.name}... This feels familiar.')
        self._last_member = member

class Repeat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx: Context, *args, member: discord.Member = None):
        print(f'type = {type(args)}')
        print(f'args = {args}')
        message = ' '.join(args)
        if message == '' or message is None:
            await ctx.send(f"You didn't give me anything to say.")
        else:
            await ctx.send(message)

class Change(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def prefix(self, ctx: Context, *args, member: discord.Member = None):
        message = ' '.join(args)
        print(self.bot.command_prefix)
        if len(message) != 1:
            await ctx.send(f'The prefix should be a single character.')
        else:
            self.bot.command_prefix = message
            await ctx.send(f'The prefix is now set to {message}.')

class Cal_gpa(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def GPA(self, ctx: Context, *args, member: discord.Member = None):
        d = {'A+': Decimal('4.3'), 'A': Decimal('4'), 'A-': Decimal('3.7'),
             'B+': Decimal('3.3'), 'B': Decimal('3'), 'B-': Decimal('2.7'),
             'C+': Decimal('2.3'), 'C': Decimal('2'), 'C-': Decimal('1.7'),
             'D': Decimal('1'), 'E': Decimal('0.8'), 'F': Decimal('0'), 'X': Decimal('0')
        }
        message = ' '.join(args)
        if message == '':
            await ctx.send(f'I cannot evalute blank GPA.')
        elif not set(args).issubset(set(d)):
            await ctx.send(f'Invalid input: All GPAs should be one of {list(d)}.')
        else:
            num_gpa = [d[el] for el in args]
            avg_gpa = sum(num_gpa) / Decimal(len(num_gpa))
            r_avg_gpa = avg_gpa.quantize(Decimal('.00'), ROUND_HALF_UP)
            await ctx.send(f'Your average GPA is {r_avg_gpa.normalize()}')
