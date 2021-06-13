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

@client.event
async def on_message(message):
    minion = discord.utils.get(message.guild.roles, name = 'Mini-Berry')
    channel1 = client.get_channel(minichannel)
    if message.channel != channel1:
        return
    if minion in message.author.roles:
        if message.content.startswith('#upgrade'):
            while(1):
                await message.channel.send('rpg guild upgrade')
                def check1(message):
                    embeds = message.embeds
                    for embed in embeds:
                        embed_dict1 = embed.to_dict()
                    return message.author.id == lume and embed_dict1['description'] == 'Guild successfully upgraded!'
                try:
                    await client.wait_for('message',timeout=20,check=check1)
                    await message.channel.send('Next Upgrade in 2 hours')
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
            embed_ict = embed.to_dict()
        await message.channel.send(f"{embed_ict}")

client.run(os.getenv('TOKEN'))