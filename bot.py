import discord
from discord.ext import commands
import dotenv
import os

dotenv.load_dotenv()
TOKEN = os.getenv("CASBOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="c!",
    description="CASbot is a test bot created by CAS AKA weirdcease.",
    intents=intents
)

@bot.hybrid_command(name="hello")
async def hello(ctx):
    await ctx.send("Hello there!")

bot.run(TOKEN)