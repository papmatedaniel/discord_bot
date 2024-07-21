import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot ready!") 


@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello there, {ctx.author.mention}!")


@bot.command()
async def goodmorning(ctx):
    await ctx.send(f"Good morning, {ctx.author.mention}!")

with open("discordbot/token.txt") as f:
    token = f.read()

bot.run("")

