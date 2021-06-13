import discord
import os
import asyncio

client = discord.Client()

lume = 555955826880413696
minichannel = 853267392754221077
bluebelly = 828941473096794142
dicechannel = 828941629984735252
rpgstuff = 848197327935373323

entry = ['yes','rpg guild', 'no', 'y', 'n', 'rpg guild list', 'a', 'b', 'c', 'rpg jail', 'protest', 'fish', 'normie fish', 'golden fish', 'epic fish', 'life potion', 'epic coin', 'coin', 'apple', 'banana', 'ruby', 'wolf', 'wolf skin', 'zombie eye', 'unicorn horn', 'mermaid hair', 'chip', 'dragon scale']

protester = ['normie fish', 'golden fish', 'epic fish', 'life potion', 'epic coin', 'coin', 'apple', 'banana', 'ruby', 'wolf skin', 'zombie eye', 'unicorn horn', 'mermaid hair', 'chip', 'dragon scale']

current_protest = ['normie fish', 'golden fish', 'epic fish', 'life potion', 'epic coin', 'coin', 'apple', 'banana', 'ruby', 'wolf skin', 'zombie eye']

@client.event
async def on_ready():
    print('you have been successfully tricked by blueberry')
    
async def time(msg):
    hour = 0
    minute = 0
    second = 0
    if 'h' in msg:
        hour = msg.split('h',1)[0]
        hour_a = hour.rstrip('0123456789')
        hour = int(hour[len(hour_a):])
    if 'm' in msg:
        if 'h' in msg:
            minute = msg.split('h',1)[1]
        minute = msg.split('m',1)[0]
        minute_a = minute.rstrip('0123456789')
        minute = int(minute[len(minute_a):])
    if 's' in msg:
        if 'm' in msg:
            second = msg.split('m',1)[1]
        second = msg.split('s',1)[0]
        second_a = second.rstrip('0123456789')
        second = int(second[len(second_a):])
    return (hour*3600) + (minute*60) + second

@client.event
async def on_message(message):
    minion = discord.utils.get(message.guild.roles, name = 'Mini-Berry')
    myid = int(client.user.id)
    me = client.get_user(myid)
    channel1 = client.get_channel(minichannel)
    default_time = 2
    if message.channel != channel1:
        return
    if minion in message.author.roles:
        if message.content.startswith('#upgrade'):
            while(1):
                time_word = '2h 0m 0s'
                for x in range(2):
                    await message.channel.send('rpg guild upgrade')
                    def check1(message):
                        embeds = message.embeds
                        for embed in embeds:
                            global embed_dict1
                            embed_dict1 = embed.to_dict()
                        return message.author.id == lume and (embed_dict1['description'] == 'Guild successfully upgraded!' or 'wait at least' in embed_dict1['title'])
                    try:
                        msg = await client.wait_for('message',timeout=10,check=check1)
                        if 'wait at least' in embed_dict1['title']:
                            msg = embed_dict1['title']
                            msg = msg.split('least ',1)[1]
                            msg = msg.split('...',1)[0]
                            time_word = msg
                            default_time = await time(msg)
                        await message.channel.send(f'Next Upgrade in {time_word}')
                        break
                    except asyncio.TimeoutError:
                        continue
                def check2(message):
                    return message.content.lower() == '#halt'
                try:
                    await client.wait_for('message',timeout=default_time,check=check2)
                    await message.channel.send('Upgrade Halted')
                except asyncio.TimeoutError:
                    await message.channel.send(f'{minion.mention} Automatic upgrade in 5 seconds')
                    await asyncio.sleep(5)
                    continue
        elif message.content.startswith('#raid'):
            while(1):
                time_word = '2h 0m 0s'
                for x in range(2):
                    await message.channel.send('rpg guild raid')
                    def check3(message):
                        embeds = message.embeds
                        for embed in embeds:
                            global embed_dict2
                            embed_dict2 = embed.to_dict()
                        return message.author.id == lume and ('RAIDED' in embed_dict2['description'] or 'wait at least' in embed_dict1['title'])
                    try:
                        msg = await client.wait_for('message',timeout=10,check=check3)
                        if 'wait at least' in embed_dict2['title']:
                            msg = embed_dict2['title']
                            msg = msg.split('least ',1)[1]
                            msg = msg.split('...',1)[0]
                            time_word = msg
                            default_time = await time(msg)
                        await message.channel.send(f'Next Raid in {time_word}')
                    except asyncio.TimeoutError:
                        continue
                def check4(message):
                    return message.content.lower() == '#halt'
                try:
                    await client.wait_for('message',timeout=default_time,check=check4)
                    await message.channel.send('Raid Halted')
                except asyncio.TimeoutError:
                    await message.channel.send(f'{minion.mention} Automatic Raid in 5 seconds')
                    await asyncio.sleep(5)
                    continue
        elif message.content.startswith('#say'):
            msg = message.content.split('#say ',1)[1]
            if any(word in msg.lower() for word in entry):
                await message.channel.send(f'{msg.lower()}')
            elif message.author.id == 475364248197791764:
                await message.channel.send(f'{msg.lower()}')
            else:
                await message.channel.send(f'{message.author.name}, you can not do that')
    
    if minion in me.roles:
        if (message.author.id == lume and 'stop there' in message.content.lower() and client.user.id in message.content) or message.content.startswith('#jail check'):
            for x in range(len(current_protest)):
                await message.channel.send(f'{current_protest[x]}')
            client.remove_roles(me,minion)
    if message.author.id == lume and ((client.user.name in message.content and 'get in the car' in message.content.lower()) or (client.user.id in message.content and 'you are in the' in message.content.lower())):
        await message.channel.send('#halt')
        await message.channel.send(f'{minion.mention} Jail Alert')
        await message.channel.send(f'{minion.mention} Jail Alert')
    if message.content.startswith('#mention'):
        await message.channel.send(f'{minion.mention}')

client.run(os.getenv('TOKEN'))