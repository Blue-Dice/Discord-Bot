import discord
import os
import asyncio

client = discord.Client()

lume = 555955826880413696
minichannel = 853267392754221077
bluebelly = 828941473096794142
dicechannel = 828941629984735252
rpgstuff = 848197327935373323

@client.event
async def on_ready():
    print('you have been successfully tricked by blueberry')
    
async def time(msg):
    hour = 0
    minute = 0
    second = 0
    if 'h' in msg:
        hour = msg.split("h",1)[0]
        hour_a = hour.rstrip('0123456789')
        hour = int(hour[len(hour_a):])
    if 'm' in msg:
        if 'h' in msg:
            minute = msg.split("h",1)[1]
        minute = msg.split("m",1)[0]
        minute_a = minute.rstrip('0123456789')
        minute = int(minute[len(minute_a):])
    if 's' in msg:
        if 'm' in msg:
            second = msg.split('m',1)[1]
        second = msg.split("s",1)[0]
        second_a = second.rstrip('0123456789')
        second = int(second[len(second_a):])
    return (hour*3600) + (minute*60) + second

@client.event
async def on_message(message):
    minion = discord.utils.get(message.guild.roles, name = 'Mini-Berry')
    channel1 = client.get_channel(minichannel)
    default_time = 2
    if message.channel != channel1:
        return
    if minion in message.author.roles:
        if message.content.startswith('#upgrade'):
            while(1):
                for x in range(3):
                    await message.channel.send('rpg guild upgrade')
                    def check1(message):
                        embeds = message.embeds
                        for embed in embeds:
                            global embed_dict1
                            embed_dict1 = embed.to_dict()
                        return message.author.id == lume and (embed_dict1['description'] == 'Guild successfully upgraded!' or 'wait at least' in embed_dict1['title'])
                    try:
                        msg = await client.wait_for('message',timeout=20,check=check1)
                        if 'wait at least' in embed_dict1['title']:
                            msg = embed_dict1['title']
                            msg = msg.split('least ',1)[1]
                            msg = msg.split('...',1)[0]
                            time_word = msg
                            default_time = await time(msg)
                        await message.channel.send(f'Next Upgrade in {time_word}')
                        break
                    except:
                        continue
        
        if message.content.startswith('#raid'):
            while(1):
                await message.channel.send('rpg guild raid')
                def check1(message):
                    embeds = message.embeds
                    for embed in embeds:
                        embed_dict2 = embed.to_dict()
                    return message.author.id == lume and 'RAIDED' in embed_dict2['description']
                try:
                    await client.wait_for('message',timeout=20,check=check1)
                    await message.channel.send('Next Raid in 2 hours')
                except:
                    continue
    
    if message.content.startswith('#history'):
        msg = await channel1.history(limit=3).flatten()
        msg = msg[2]
        embeds = msg.embeds
        for embed in embeds:
            embed_dict3 = embed.to_dict()
        if 'wait at least' in embed_dict3['title']:
            msg = embed_dict3['title']
            msg = msg.split('least ',1)[1]
            msg = msg.split('...',1)[0]
            time_word = msg
            default_time = await time(msg)
        await message.channel.send(f'{time_word} = {default_time}seconds')

client.run(os.getenv('TOKEN'))