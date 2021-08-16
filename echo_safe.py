from discord.ext import commands
from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv('TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)


bot.run(TOKEN)
