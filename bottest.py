import discord
import os
from dotenv import load_dotenv

bot=discord.Client()

@bot.event
async def on_ready():
    print("機器人已就緒",bot.user)
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game("SITCON"))
    print(bot.user.id)


@bot.event
async def on_message(message):
    print(message.author.id)
    if message.author==bot.user:
        return
    if message.content=="發送embed":
        embed=discord.Embed(
              title="嗨",
              colour=discord.Colour(0xE5E242),
              url="https://google.com",
              description="Welcome"
                )
        await message.channel.send(embed=embed)
    if message.content == "img":
        await message.channel.send("see",file=discord.File('this.jpg'))
    if message.content.startswith('change'):
        messagelist=message.content.split(" ",2)
        if len(messagelist)!=1:
            await bot.change_presence(status=discord.Status.online,activity=discord.Game(messagelist[1]))
        else:
            await message.channel.send("記得打字!")
    if message.content=="hi":
        await bot.change_presence(status=discord.Status.online)
        await message.channel.send("HI~")
    if message.content=="mouse":
        global reaction_msg
        reaction_msg=await message.channel.send("點我!")
        await reaction_msg.add_reaction('🐹')
@bot.event
async def on_reaction_add(reaction,user):
    if user==bot.user:
        return
    if reaction.message.id != reaction_msg.id:
        return
    if reaction.emoji=='🐹':
        role=discord.utils.get(user.guid.roles,id=875911357604720641)
        await user.add_roles(role)











load_dotenv()
bot.run(os.getenv("TOKEN"))
