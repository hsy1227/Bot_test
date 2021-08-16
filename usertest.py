import discord
import os
from dotenv import load_dotenv
import requests
import asyncio

bot=discord.Client()

@bot.event
async def on_ready():
    print("機器人已就緒",bot.user)
    await bot.change_presence(status=discord.Status.idle,activity=discord.Game("爆肝中"))

@bot.event
async def on_message(message):
    usenumber=0
    number=message.author.id
    if message.content=="開始遊戲": #檢查使否有資料

        find=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
        id_data=find.json()
        a={"id":number,"money":50,"等級":1,"satisfy":0,"clean":0,"lovely":0,"普通飼料":0,"中級飼料":0,"高級飼料":0,"飛盤":0,"小球":0,"逗貓棒":0,"沐浴劑":0,"寵物香皂":0,"梳毛器":0}
        length=len(id_data["data"])
        for i in range(len(id_data["data"])):
            if length==1 and number!=int(id_data["data"][i]["id"]):
                usenumber+=1
                id_data["data"].append(a)
                update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=id_data)
            elif number==int(id_data["data"][i]["id"]):
                usenumber=i
                break
            elif (number!=int(id_data["data"][i]["id"]) and i==(length-1)):
                    id_data["data"].append(a)
                    usenumber+=1
                    update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=id_data)
            else:
                continue
    if message.author==bot.user:
        return
    if message.content=="record": #記錄累積成就
        ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
        data=ans.json()
        if data["data"][usenumber]['lovely']>=100:
            data["data"][usenumber]['lovely']=data["data"][usenumber]['lovely']-100
            data["data"][usenumber]['等級']=data["data"][number]['等級']+1
            update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=data)
            await message.channel.send("恭喜你升等啦💞")
        embed=discord.Embed(
               title="目前等級與成就",
               colour=discord.Colour(0xE5E842),
                )
        embed.add_field(name="等級:",value=data["data"][usenumber]['等級'],inline=False)
        embed.add_field(name="飽足感:",value=data["data"][usenumber]['satisfy'],inline=True)
        embed.add_field(name="清潔度:",value=data["data"][usenumber]['clean'],inline=True)
        embed.add_field(name="喜愛度:",value=data["data"][usenumber]['lovely'],inline=True)
        await message.channel.send(embed=embed)
        #    if message.content == "img":
        #        await message.channel.send("see",file=discord.File('this.jpg'))
        # if message.content.startswith('change'):
        # messagelist=message.content.split(" ",2)
        # if len(messagelist)!=1:
        #     await bot.change_presence(status=discord.Status.online,activity=discord.Game(messagelist[1]))
        # else:
        #     await message.channel.send("記得打字!")
    if message.content=="hi":
        await bot.change_presence(status=discord.Status.online)
        await message.channel.send("HI~")
    if message.content=="mouse":
        global reaction_msg
        reaction_msg=await message.channel.send("點我!")
        await reaction_msg.add_reaction('🐹')

    #     if message.content=="item":  #查看物品
     #        ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
        # data=ans.json()
        # embed=discord.Embed(
        #         title="我的口袋",
                # embed.add_field(name="普通飼料",value=data['普通飼料'],inline=True)
                #  embed.add_field(name="中級飼料",value=data['中級飼料'],inline=True)
                #  embed.add_field(name="高級飼料",value=data['高級飼料'],inline=True)
                #  embed.add_field(name="飛盤",value=data['飛盤'],inline=True)
            #   embed.add_field(name="小球",value=data['小球'],inline=True)
      #  embed.add_field(name="逗貓棒",value=data['逗貓棒'],inline=True)
     #   embed.add_field(name="沐浴劑",value=data['沐浴劑'],inline=True)
       # embed.add_field(name="寵物香皂",value=data['寵物香皂'],inline=True)
     #   embed.add_field(name="梳毛器",value=data['梳毛器'],inline=True)
      #  await message.channel.send(embed=embed)
   # if message.content=="普通飼料":
      #  ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
     #   data=ans.json()
      #  if data['普通飼料']==0:
          #  await message.channel.send("沒庫存了QQ")
     #   else:
       #     data['普通飼料']=(data['普通飼料'])-1
      #      data['satisfy']=(data['satisfy'])+10
      #      update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=data)
     #       await message.channel.send("餵食完成!好感度增加囉:D")
    #if message.content=="中級飼料":
    #    ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
    #    data=ans.json()
    #    if data['中級飼料']==0:
   #         await message.channel.send("沒了快去買!")
    #    else:
     #       data['中級飼料']=(data['中級飼料'])-1
      #      data['satisfy']=(data['satisfy'])+20
       #     update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=data)
       #     await message.channel.send("餵食完成!謝謝你用心照顧我<3")
   # if message.content=="高級飼料":
    #    ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
     #   data=ans.json()
      #  if data['高級飼料']==0:
       #     await message.channel.send("沒有了耶:(")
        #else:
     #       data['高級飼料']=(data['高級飼料'])-1
      #      data['satisfy']=(data['satisfy'])+35
       #     update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=data)
        #    await message.channel.send("餵食完成!好開心><!")

    #if message.content=="飛盤":
     #   ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
      #  data=ans.json()
       # if data['飛盤']==0:
      #      await message.channel.send("沒庫存了QQ")
       # else:
        #    data['飛盤']=(data['飛盤'])-1
         #   data['lovely']=(data['lovely'])+10
          #  data['clean']=(data['clean'])-5
       #     update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=data)
        #    await message.channel.send("謝謝你陪我玩:D")
   # if message.content=="小球":
    #    ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
     #   data=ans.json()
      #  if data['小球']==0:
       #     await message.channel.send("沒庫存不能玩球了QQ")
        #else:
         #   data['小球']=(data['小球'])-1
          #  data['lovely']=(data['lovely'])+10
           # data['satisfy']=data['satisfy']-5
            #update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=data)
            #await message.channel.send("好好玩><!")
    #if message.content=="逗貓棒":
     #   ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
      #  data=ans.json()
       # if data['逗貓棒']==0:
        #    await message.channel.send("沒有了耶:(")
#        else:
 #           data['lovely']=(data['lovely'])+10
  #          data['satisfy']=data['satisfy']-5
   #         data['逗貓棒']=(data['逗貓棒'])-1
    #        update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=data)
     #       await message.channel.send("逗貓棒好好玩🧡")

#    if message.content=="沐浴劑":
 #      ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
 #       data=ans.json()
  #      if data['沐浴劑']==0:
   #         await message.channel.send("沒庫存了QQ")
    #    else:
     #      data['沐浴劑']=(data['沐浴劑'])-1
      #      data['clean']=(data['clean'])+15
       #     update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=data)
        #    await message.channel.send("洗香香🥳")

#    if message.content=="寵物香皂":
 #       ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
  #      data=ans.json()
   #     if data['寵物香皂']==0:
    #        await message.channel.send("沒辦法洗澡了QQ")
     #   else:
      #      data['寵物香皂']=(data['寵物香皂'])-1
       #     data['clean']=(data['clean'])+20
        #    update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=data)
         #   await message.channel.send("最喜歡洗澡!😍")


    #if message.content=="梳毛器":
     #   ans=requests.get('https://jsonstorage.net/api/items/',{"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"})
      #  data=ans.json()
       # if data['梳毛器']==0:
        #    await message.channel.send("沒有了QQ(")
        #else:
         #   data['clean']=(data['clean'])+25
           # data['梳毛器']=(data['梳毛器'])-1
            #update=requests.put("https://jsonstorage.net/api/items/",params={"id":"2d5e884e-6de0-4a1f-addf-ff73fc36d5b8"},json=data)
            #await message.channel.send("喜歡梳毛!💛")























@bot.event
async def on_reaction_add(reaction,user):
    if user==bot.user:
        return
    if reaction.message.id != reaction_msg.id:
        return
    if reaction.emoji=='🐹':
        role=discord.utils.get(user.guid.roles,id=876647797280112650)
        await user.add_roles(role)











load_dotenv()
bot.run(os.getenv("TOKEN"))
import discord
import discord
