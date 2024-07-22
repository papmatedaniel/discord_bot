import discord
from discord.ext import commands
import random


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


temak = [
    "Mesterséges intelligencia",
    "Kvantumszámítógépek",
    "Ökológiai lábnyom",
    "Megújuló energiaforrások",
    "Asztrofizika",
    "Történelem",
    "Modern művészet",
    "Nanotechnológia",
    "Pszichológia",
    "Kultúra és társadalom",
    "Geológia",
    "Bioetika",
    "Kiborgok és ember-gép hibriditás",
    "Irodalom",
    "Filozófia",
    "Kiberbiztonság",
    "Tudományos felfedezések",
    "Klimatológia",
    "Szociológia",
    "Virtuális valóság",
    "Robotika",
    "Orvosi innovációk",
    "Agrártudományok",
    "Nukleáris energia",
    "Adatvédelem és adatbiztonság",
    "Géntechnológia",
    "Tengeri biológia",
    "Antropológia",
    "Matematika",
    "Fizika",
    "Vegyészet",
    "Őslénytan",
    "Művészet és design",
    "Építészet",
    "Éghajlatváltozás",
    "Gazdaságtan",
    "Pénzügyek",
    "Városi tervezés",
    "Fotográfia",
    "Zene",
    "Tánc",
    "Színház",
    "Film és média",
    "Nyelvek és nyelvészet",
    "Számítástechnika",
    "Mobil technológia",
    "E-sport",
    "Táplálkozás és diéta",
    "Sport és fitnesz"
]


@bot.command()
async def topic(ctx):
    veletlen = random.choice(temak)
    await ctx.send(f"A mai téma: {veletlen}")


@bot.command()
async def sendembed(ctx):
    embeded_msg = discord.Embed(title="Title of embed", description="Description of embed", color=discord.Color.green())
    embeded_msg. set_author(name="Footer text", icon_url=ctx.author.avatar)
    embeded_msg.set_thumbnail(url=ctx.author.avatar)
    embeded_msg.add_field(name="Name of field", value="Value of field", inline=False)
    embeded_msg.set_image(url=ctx.guild.icon)
    embeded_msg.set_footer(text="Footer text", icon_url=ctx.author.avatar)
    await ctx.send(embed=embeded_msg)

@bot.command ()
async def ping(ctx):
    ping_embed = discord.Embed(title="Ping", description="Latency in ms", color=discord.Color.blue())
    ping_embed.add_field(name=f"{bot.user.name}'s Latancy (ms): ", value=f"{round(bot.latency *1000)}ms.", inline=False)
    ping_embed. set_footer(text=f"Requested by {ctx.author.name}.", icon_url=ctx.author. avatar)
    await ctx.send(embed=ping_embed)

bot.run("")

