import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()

async def new(ctx):
    await ctx.send('  @everyone دوست عزیز منتظر بمانید دوستان برای وریفای تشریف می آورند ')

bot.run('TOKEN')