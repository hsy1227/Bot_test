# ATTENTION!
# This code is for teaching purpose, DO NOT use this in production
# Your token might be LEAKED!
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)


bot.run('ODc1OTEwMDg0ODAxMjI0Nzg1.YRcY1Q.KZ4OH67jxJjVGV4tNCVIG029ZrA')
