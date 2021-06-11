import discord
import os
import asyncio
import sys

from keep_alive import keep_alive
client = discord.Client()

@client.event
async def on_ready():
    print('You have successfully been tricked by Blueberry')

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

async def Hunt(message):
  while(1):
    await message.channel.send('rpg hunt')
    def check(message):
      return message.author.id == 555955826880413696 and any(word in message.content for word in name) and (any(word in message.content for word in hunt) or any(word in message.content for word in jail))
    try:
      msg = await client.wait_for('message', timeout=10, check=check)
      if any(word in msg.content for word in name) and any(word in msg.content for word in jail):
        return
    except asyncio.TimeoutError:
      await message.channel.send('rpg hunt')
    def stop(message):
      return message.author == client.user and message.content == '#stop hunt'
    try:
      await client.wait_for('message', timeout=62, check=stop)
      await message.channel.send('!1')
      return
    except asyncio.TimeoutError:
      continue
  return

async def Work(message,action):
  while(1):
    await message.channel.send(f"rpg {action}")
    def check(message):
      return message.author.id == 555955826880413696 and any(word in message.content for word in name) and (any(word in message.content for word in work) or any(word in message.content for word in jail))
    try:
      msg = await client.wait_for('message', timeout=10, check=check)
      if any(word in msg.content for word in name) and any(word in msg.content for word in jail):
        return
    except asyncio.TimeoutError:
      await message.channel.send(f"rpg {action}")
    def stop(message):
      return message.author == client.user and message.content == '#stop work'
    try:
      await client.wait_for('message', timeout=303, check=stop)
      await message.channel.send('!2')
      return
    except asyncio.TimeoutError:
      continue
  return

async def Adv(message):
  while(1):
    y = 3600
    await message.channel.send('rpg adv')
    def check(message):
      return (message.author.id == 555955826880413696 and any(word in message.content for word in name) and (any(word in message.content for word in advs) or any(word in message.content for word in jail))) or (message.author == client.user and message.content.startswith('adv time'))
    try:
      msg = await client.wait_for('message', timeout=10, check=check)
      if any(word in msg.content for word in name) and any(word in msg.content for word in jail):
        return
      elif msg.content.startswith('adv time'):
        y=0
        timecounter = msg.content.split("adv time ",1)[0]
        pettime = timecounter
        hour = int(timecounter.split("h",1)[0])
        y = y + hour*3600
        minute = timecounter.split("h ",1)[1]
        minute = int(minute.split("m",1)[0])
        y = y + minute*60
        await message.channel.send(f'**{pettime}** = {y}')
    except asyncio.TimeoutError:
      await message.channel.send('rpg adv')
    def stop(message):
      return message.author == client.user and message.content == '#stop adv'
    try:
      await client.wait_for('message', timeout=y+3, check=stop)
      await message.channel.send('!3')
      return
    except asyncio.TimeoutError:
      continue
  return

async def Ed(message):
  while(1):
    y = 10800
    await message.channel.send('rpg buy ed lb')
    def check(message):
      return (message.author.id == 555955826880413696 and (any(word in message.content for word in edgy) or any(word in message.content for word in jail))) or (message.author == client.user and message.content.startswith('ed time'))
    try:
      msg = await client.wait_for('message', timeout=10, check=check)
      if any(word in msg.content for word in name) and any(word in msg.content for word in jail):
        return
      elif msg.content.startswith('ed time'):
        y=0
        timecounter = msg.content.split("ed time ",1)[1]
        pettime = timecounter
        hour = int(timecounter.split("h",1)[0])
        y = y + hour*3600
        minute = timecounter.split("h ",1)[1]
        minute = int(minute.split("m",1)[0])
        y = y + minute*60
        await message.channel.send(f'**{pettime}** = {y}')
    except asyncio.TimeoutError:
      await message.channel.send('rpg buy ed lb')
    def stop(message):
      return message.author == client.user and message.content == '#stop ed'
    try:
      await client.wait_for('message', timeout=y+5, check=stop)
      await message.channel.send('!4')
      return
    except asyncio.TimeoutError:
      continue
  return

async def HealH(message):
  while(1):
    await message.channel.send('rpg heal')
    def check(message):
      return message.author.id == 555955826880413696 and any(word in message.content for word in name) and (any(word in message.content for word in heal) or any(word in message.content for word in jail))
    try:
      msg = await client.wait_for('message', timeout=10, check=check)
      if any(word in msg.content for word in name) and any(word in msg.content for word in jail):
        return
    except asyncio.TimeoutError:
      await message.channel.send('rpg heal')
    await asyncio.sleep(5)
    await message.channel.send('rpg hunt')
    def check(message):
      return message.author.id == 555955826880413696 and any(word in message.content for word in name) and (any(word in message.content for word in hunt) or any(word in message.content for word in jail))
    try:
      msg = await client.wait_for('message', timeout=10, check=check)
      if any(word in msg.content for word in name) and any(word in msg.content for word in jail):
        return
    except asyncio.TimeoutError:
      await message.channel.send('rpg hunt')
    def stop(message):
      return message.author == client.user and message.content == '#stop hunt'
    try:
      await client.wait_for('message', timeout=57, check=stop)
      await message.channel.send('!!')
      return
    except asyncio.TimeoutError:
      continue
  return

async def AdvH(message):
  while(1):
    y = 3595
    await message.channel.send('rpg heal')
    def check(message):
      return message.author.id == 555955826880413696 and any(word in message.content for word in name) and (any(word in message.content for word in heal) or any(word in message.content for word in jail))
    try:
      msg = await client.wait_for('message', timeout=10, check=check)
      if any(word in msg.content for word in name) and any(word in msg.content for word in jail):
        return
    except asyncio.TimeoutError:
      await message.channel.send('rpg heal')
    await asyncio.sleep(5)
    await message.channel.send('rpg adv')
    def check(message):
      return (message.author.id == 555955826880413696 and any(word in message.content for word in name) and (any(word in message.content for word in advs) or any(word in message.content for word in jail))) or (message.author == client.user and message.content.startswith('adv time'))
    try:
      msg = await client.wait_for('message', timeout=10, check=check)
      if any(word in msg.content for word in name) and any(word in msg.content for word in jail):
        return
      elif msg.content.startswith('adv time'):
        y=0
        timecounter = msg.content.split("adv time ",1)[1]
        pettime = timecounter
        hour = int(timecounter.split("h",1)[0])
        y = y + hour*3600
        minute = timecounter.split("h ",1)[1]
        minute = int(minute.split("m",1)[0])
        y = y + minute*60
        await message.channel.send(f'**{pettime}** = {y+3}')
    except asyncio.TimeoutError:
      await message.channel.send('rpg adv')
    def stop(message):
      return message.author == client.user and message.content == '#stop adv'
    try:
      await client.wait_for('message', timeout=y+5, check=stop)
      await message.channel.send('!!!')
      return
    except asyncio.TimeoutError:
      continue
  return

async def Farm(message,action):
  if action == 'farm_potato':
    execute = "rpg farm potato"
  elif action == 'farm_bread':
    execute = "rpg farm bread"
  elif action == 'farm_carrot':
    execute = "rpg farm carrot"
  else:
    execute = "rpg farm"
  while(1):
    await message.channel.send(f"{execute}")
    def check(message):
      return message.author.id == 555955826880413696 and any(word in message.content for word in name) and (any(word in message.content for word in farm) or any(word in message.content for word in jail) or any(word in message.content for word in nofarm))
    try:
      msg = await client.wait_for('message', timeout=10, check=check)
      if any(word in msg.content for word in name) and any(word in msg.content for word in jail):
        return
      elif any(word in msg.content for word in name) and any(word in msg.content for word in nofarm):
        execute = "rpg farm"
        await message.channel.send(f"{execute}")
    except asyncio.TimeoutError:
      await message.channel.send(f"{execute}")
    def stop(message):
      return message.author == client.user and message.content == '#stop farm'
    try:
      await client.wait_for('message', timeout=601, check=stop)
      await message.channel.send('!5')
      return
    except asyncio.TimeoutError:
      continue
  return

async def Pet(message,action):
  initial = str(action.split("pet_",1)[1])
  if initial.startswith('l'):
    part_a = 'learn'
    part_b = str(initial.split("l",1)[1])
  elif initial.startswith('f'):
    part_a = 'find'
    part_b = str(initial.split("f",1)[1])
  execute = f"rpg pets adv {part_a} {part_b}"
  while(1):
    await message.channel.send("rpg pets adv claim")
    await asyncio.sleep(5)
    await message.channel.send(f"{execute}")
    y=0
    def check(message):
      return (message.author.id == 555955826880413696 and (any(word in message.content for word in petter) or any(word in message.content for word in jail))) or (message.author == client.user and message.content.startswith('pet time'))
    try:
      msg = await client.wait_for('message', timeout=10, check=check)
      if any(word in msg.content for word in name) and any(word in msg.content for word in jail):
        return
      elif any(word in msg.content for word in petter):
        timecounter = msg.content.split("in ",1)[1]
        timecounter = timecounter.split("!",1)[0]
        pettime = timecounter
        hour = timecounter.split("h",1)[0]
        hour_a = hour.rstrip('0123456789')
        hour = int(hour[len(hour_a):])
        y = y + hour*3600
        minute = timecounter.split("h ",1)[1]
        minute = int(minute.split("m",1)[0])
        y = y + minute*60
        second = timecounter.split("m ",1)[1]
        second = int(second.split("s",1)[0])
        y = y + second
      elif msg.content.startswith('pet time'):
        timecounter = msg.content.split("pet time ",1)[1]
        pettime = timecounter
        hour = int(timecounter.split("h",1)[0])
        y = y + hour*3600
        minute = timecounter.split("h ",1)[1]
        minute = int(minute.split("m",1)[0])
        y = y + minute*60
      await message.channel.send(f'**{pettime}** = {3}')
    except asyncio.TimeoutError:
      await message.channel.send(f"{execute}")
    def stop(message):
      return message.author == client.user and message.content == '#stop pet'
    try:
      await client.wait_for('message', timeout=y+5, check=stop)
      await message.channel.send('!6')
      return
    except asyncio.TimeoutError:
      continue
  return

async def Restart_Program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

@client.event
async def on_message(message):
  if message.author == client.user:
    if message.content.startswith("#start"):
      action = str(message.content.split("#start ",1)[1])
      if action == 'hunt':
        await Hunt(message)
      elif action == 'chop' or action == 'axe' or action == 'bowsaw' or action == 'chainsaw' or action == 'fish' or action == 'net' or action == 'boat' or action == 'bigboat':
        await Work(message,action)
      elif action == 'adv':
        await Adv(message)
      elif action == 'ed':
        await Ed(message)
      elif action == 'healhunt':
        await HealH(message)
      elif action == 'healadv':
        await AdvH(message)
      elif action == 'farm_normal' or action == 'farm_potato' or action == 'farm_bread' or action == 'farm_carrot':
        await Farm(message,action)
      elif any(word in action for word in pets):
        await Pet(message,action)
      elif action == 'restart':
        await message.channel.send('okay')
        await Restart_Program()
      else:
        return
    else:
      return
  else:
    return

keep_alive()
client.run(os.getenv('TOKEN'))