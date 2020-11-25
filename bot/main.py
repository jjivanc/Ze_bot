import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.getenv("NzgwNzY4ODQ1ODQxMTcwNDMz.X7z5pg.G_QhbQzhuuwmfopzuuBq3OL68r0")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Ativo  .help"))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"Você é {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

@client.command(name="search")
async def speak(ctx, *, text):
    message = ctx.message
    await message.delete()
    await ctx.send(f"https://nhentai.net/g/{text}/")
    
@client.command(name="img")
async def imagen(ctx,*,text):
	message = ctx.message
	await message.delete()
	await ctx.send(f"https://t.nhentai.net/galleries/{text}/cover.jpg")

client.run('NzgwNzY4ODQ1ODQxMTcwNDMz.X7z5pg.G_QhbQzhuuwmfopzuuBq3OL68r0')