import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("CocoBot is Online ✅")

@bot.command()
async def vibes(ctx):
    await ctx.send("🌴 Feel the tropical vibes, my friend!")

@bot.command()
async def coconut(ctx):
    await ctx.send("🥥 You just got a fresh coconut!")

@bot.command()
async def help(ctx):
    await ctx.send("Here are my commands:\n!vibes\n!coconut\n!help")

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
