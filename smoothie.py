import discord
import os
import asyncio
import sys

client = discord.Client()

@client.event
async def on_ready():
    global name
    n1 = str(client.user.name)
    n2 = str(client.user.id)
    name = [n1,n2]
    await client.get_channel(828941473096794142).send('Hax Mode: ON')
    print('You have successfully been tricked by Blueberry')

bluebelly = 828941473096794142

hunt = ['slime','goblin','wolf','skeleton','nymph','ghost','baby','zombie','witch','imp','ghoul','giant','scorpion','unicorn','sorcerer','cecaelia','giant','mermaid','nereid','demon','harpy','robot','dullahan','manticore','dragon']
work = ['fishing','chopping','collecting','mining']
worker = ['fish','net','boat','bigboat','chop','axe','bowsaw','chainsaw','pickup','ladder','tractor','greenhouse','mine','pickaxe','drill','dynamite']
advs = ['mutant','giant','bees','ogre','dark','hyper','werewolf','centaur','chimera','golem','mammoth','key','ent','dinosaur','cyclops','helicopter','hydra','kraken','leviathan','tank','wyrm','titan','typhon','dragon']
edgy = ['successfully bought','EDGY','420,600']
heal = ['your life has been restored','your life is maxed out']
farm = []
nofarm = ['']
farmer = ['farm d','farm b','farm c','farm p']
pets = ['pet_la','pet_lb','pet_lc','pet_ld','pet_le','pet_lf','pet_lg','pet_lh','pet_li','pet_lj','pet_lk','pet_ll','pet_lm','pet_ln','pet_lo','pet_lp','pet_fa','pet_fb','pet_fc','pet_fd','pet_fe','pet_ff','pet_fg','pet_fh','pet_fi','pet_fj','pet_fk','pet_fl','pet_fm','pet_fn','pet_fo','pet_fp']
lume = 555955826880413696

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

async def Hunt(message):
    while(1):
        for x in range(2):
            await message.channel.send('rpg hunt')
            def check1(message):
                return message.author.id == lume and any(word in message.content for word in name) and any(word in message.content.lower() for word in hunt)
            try:
                msg = await client.wait_for('message',timeout=10,check=check1)
                break
            except asyncio.TimeoutError:
                continue  
                
        if 'Lost' in msg.content:
            HP = msg.content.split("Lost ",1)[1]
            HP = int(HP.split(" HP,",1)[0])
            if HP == 0:
                pass
            else:
                for x in range(3):
                    await asyncio.sleep(2)
                    await message.channel.send('rpg heal')
                    def check2(message):
                        return message.author.id == lume and any(word in message.content for word in name) and any(word in message.content for word in heal)
                    try:
                        await client.wait_for('message',timeout=10,check=check2)
                        break
                    except asyncio.TimeoutError:
                        continue    
                        
        def check3(message):
            return message.author == client.user and message.content.lower() == '#stop hunt'
        try:
            await client.wait_for('message',timeout=61,check=check3)
            await message.channel.send('!hunt')
            break
        except asyncio.TimeoutError:
            continue
    return

async def Advs(message):
    while(1):
        default_time = 3600
        time_word = '**1h 0m 0s**'
        for x in range(2):
            await message.channel.send('rpg adv')
            def check1(message):
                return (message.author.id == lume and any(word in message.content for word in name) and any(word in message.content.lower() for word in advs)) or (message.author == client.user and 'Time:' in message.content)
            try:
                msg = await client.wait_for('message',timeout=10,check=check1)
                psg = msg.content
                if 'Time:' in msg.content:
                    msg = msg.content.split('Time: ',1)[1]
                    time_word = msg
                    default_time = await time(msg)
                await message.channel.send(f'{time_word} = **{default_time}** seconds')
                break
            except asyncio.TimeoutError:
                await asyncio.sleep(3)
                continue  
                
        if 'Lost' in psg:
            HP = psg.split("Lost ",1)[1]
            HP = int(HP.split(" HP,",1)[0])
            if HP == 0:
                pass
            else:
                for x in range(3):
                    await asyncio.sleep(2)
                    await message.channel.send('rpg heal')
                    def check2(message):
                        return message.author.id == lume and any(word in message.content for word in name) and any(word in message.content for word in heal)
                    try:
                        await client.wait_for('message',timeout=10,check=check2)
                        break
                    except asyncio.TimeoutError:
                        continue    
                        
        def check3(message):
            return message.author == client.user and message.content.lower() == '#stop adv'
        try:
            await client.wait_for('message',timeout=default_time+5,check=check3)
            await message.channel.send('!adv')
            break
        except asyncio.TimeoutError:
            continue
    return

async def Work(message,action):
    while(1):
        for x in range(2):
            await message.channel.send(f'rpg {action}')
            def check1(message):
                return message.author.id == lume and any(word in message.content for word in name) and any(word in message.content.lower() for word in work)
            try:
                await client.wait_for('message',timeout=10,check=check1)
                break
            except asyncio.TimeoutError:
                await asyncio.sleep(4)
                continue
                
        def check2(message):
            return message.author == client.user and message.content.lower() == '#stop work'
        try:
            await client.wait_for('message',timeout=302,check=check2)
            await message.channel.send('!work')
            break
        except asyncio.TimeoutError:
            continue
    return

async def Edlb(message):
    while(1):
        time_word = '**3h 0m 0s**'
        default_time = 10800
        for x in range(3):
            await message.channel.send('rpg buy ed lb')
            def check1(message):
                return (message.author.id == lume and 'successfully bought' in message.content.lower()) or (message.author == client.user and 'Time:' in message.content)
            try:
                msg = await client.wait_for('message',timeout=10,check=check1)
                if 'Time:' in msg.content:
                    msg = msg.content.split('Time: ',1)[1]
                    time_word = msg
                    default_time = await time(msg)
                await message.channel.send(f'{time_word} = **{default_time}** seconds')
                break
            except asyncio.TimeoutError:
                await asyncio.sleep(6)
                continue
        def check2(message):
            return message.author == client.user and message.content.lower() == '#stop ed'
        try:
            await client.wait_for('message',timeout=default_time+5,check=check2)
            await message.channel.send('!edgy')
            break
        except asyncio.TimeoutError:
            continue
    return

async def Farm(message,action):
    action = action.split('farm ',1)[1]
    if action == p:
        execute = 'potato'
    elif action == c:
        execute = 'carrot'
    elif action == b:
        execute = 'bread'
    else:
        execute = ''
    while(1):
        for x in range(2):
            await message.channel.send(f'rpg farm {execute}')
            def check1(message):
                return message.author.id == lume and ('have grown from the seed' in message.content.lower() or 'you do not have this type of seed' in message.content.lower())
            try:
                msg = await client.wait_for('message',timeout=10,check=check1)
                if 'you do not have this type of seed' in msg.content:
                    execute = ''
                    continue
                break
            except asyncio.TimeoutError:
                await asyncio.sleep(1)
                continue
        def check2(message):
            return message.author == client.user and message.content.lower() == '#stop farm'
        try:
            await client.wait_for('message',602,check=check2)
            await message.channel.send('!farm')
            break
        except asyncio.TimeoutError:
            continue
    return

@client.event
async def on_message(message):
    channel1 = client.get_channel(bluebelly)
    if message.channel != channel1:
        return
    
    if message.author == client.user:
        if 'rpg adv' in message.content or 'rpg buy ed lb' in message.content:
            msg = await client.wait_for('message',check = lambda message: message.author.id == lume)
            embeds = msg.embeds
            for embed in embeds:
                embed_dict = embed.to_dict()
            if 'title' in embed_dict.keys():
                if 'wait at least' in embed_dict['title']:
                    msg = embed_dict['title']
                    msg = msg.split('least ',1)[1]
                    msg = msg.split('...',1)[0]
                    await message.channel.send(f'Time: {msg}')
        if message.content.startswith('#start'):
            action = str(message.content.split('#start ',1)[1])
            if action.lower() == 'hunt':
                await Hunt(message)
            if action.lower() == 'adv':
                await Advs(message)
            if any(word in action.lower() for word in worker):
                await Work(message,action)
            if action.lower() == 'ed':
                await Edlb(message)
            if any(word in action.lower() for word in farmer):
                await Farm(message,action)
    
    if message.author.id == lume and 'stop there' in message.content.lower() and client.user.id in message.content:
        await channel1.send('normie fish')
        await channel1.send('golden fish')
        await channel1.send('epic fish')
        await channel1.send('life potion')
        await channel1.send('epic coin')
        await channel1.send('coin')
        await channel1.send('apple')
        await channel1.send('banana')
        await channel1.send('ruby')
        await channel1.send('wolf skin')
        await channel1.send('zombie eye')
        await channel1.send('unicorn horn')
        await channel1.send('mermaid hair')
        await channel1.send('chip')
        await channel1.send('dragon scale')
    
    if message.author.id == lume and client.user.name in message.content and 'get in the car' in message.content.lower():
        await message.channel.send('#stop hunt')
        await message.channel.send('#stop work')
        await message.channel.send('#stop farm')
    
    if message.author.id == lume and str(client.user.id) in message.content and 'you are in the' in message.content.lower():
        await message.channel.send('#stop hunt')
        await message.channel.send('#stop work')
        await message.channel.send('#stop farm')
        await message.channel.send('#stop adv')
        await message.channel.send('#stop ed')
        
client.run(os.getenv('TOKEN'))