import discord
import os
import asyncio
import sys

client = discord.Client()

@client.event
async def on_ready():
    global n1
    global n2
    n1 = str(client.user.name)
    n2 = str(client.user.id)
    await client.get_channel(828941473096794142).send('Hax Mode: ON')
    print('You have successfully been tricked by Blueberry')

name = [n1,n2]
hunt = ['slime','goblin','wolf','skeleton','nymph','ghost','baby','zombie','witch','imp','ghoul','giant','scorpion','unicorn','sorcerer','cecaelia','giant','mermaid','nereid','demon','harpy','robot','dullahan','manticore','dragon']
work = ['chopping','fishing','fish','log','nets','axe']
jail = ['jail']
advs = ['mutant','giant','bees','ogre','dark','hyper','werewolf','centaur','chimera','golem','mammoth','key','ent','dinosaur','cyclops','helicopter','hydra','kraken','leviathan','tank','wyrm','titan','typhon','dragon']
edgy = ['successfully bought','EDGY','420,600']
heal = ['your life has been restored','your life is maxed out']
farm = ['have grown from the seed']
nofarm = ['you do not have this type of seed']
pets = ['pet_la','pet_lb','pet_lc','pet_ld','pet_le','pet_lf','pet_lg','pet_lh','pet_li','pet_lj','pet_lk','pet_ll','pet_lm','pet_ln','pet_lo','pet_lp','pet_fa','pet_fb','pet_fc','pet_fd','pet_fe','pet_ff','pet_fg','pet_fh','pet_fi','pet_fj','pet_fk','pet_fl','pet_fm','pet_fn','pet_fo','pet_fp']
petter = ['will be back','started an adventure']
inside_jail = ['you are in the','jail','type']
lume = 555955826880413696

async def Hunt(message):
    while(1):
        while(1):
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
                while(1):
                    await message.channel.send('rpg heal')
                    def check2(message):
                        return message.author.id == lume and any(word in message.content for word in name) and any(word in message.content for word in heal)
                    try:
                        await client.wait_for('message',timeout=10,check=check2)
                        break
                    except asyncio.TimeoutError:
                        continue
        
        def check3(message):
            return message.author == client.user and message.content.lower() == '#halt'
        try:
            await client.wait_for('message',timeout=61,check=check3)
            await message.channel.send('Abrupt Halt - DeprecationWarning')
            break
    if message.content.lower().startswith('#stop hunt'):
        return
    return      

@client.event
async def on_message(message):
    channel1 = await client.get_channel(828941473096794142)
    if message.channel != channel1:
        return
    
    if message.author == client.user:
        if message.content.startswith('#start'):
            action = str(message.content.split('#start ',1)[1])
            if action.lower() == 'hunt':
                Hunt(message)

client.run(os.getenv('TOKEN'))