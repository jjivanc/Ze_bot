import discord
from discord.ext import commands
import os
import ver

client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("A Vida Fora |.help para ajuda| "))
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

@client.command(name="ver")
async def imagen(ctx,*,text):
	message = ctx.message
	await message.delete()
	await ctx.send(f"test {image}")	
	
client.run(token)
