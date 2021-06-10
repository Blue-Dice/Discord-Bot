import discord
import os
import asyncio
import sys

intents = discord.Intents.all()
client = discord.Client(intents = intents)

@client.event
async def on_ready():
  await client.get_channel(828941473096794142).send("Manual Restart")
  print("You have successfully been tricked by Blueberry")

hunt = ['found and killed']
name = ['Blueberry Smoothie','475364248197791764']
FHunt = 0
FWork = 0
FEdgy = 0
FPett = 0
FFarm = 0
FAdvs = 0
pets = ["pet_la","pet_lb","pet_lc","pet_ld","pet_le","pet_lf","pet_lg","pet_lh","pet_li","pet_lj","pet_lk","pet_ll","pet_lm","pet_ln","pet_lo","pet_lp","pet_fa","pet_fb","pet_fc","pet_fd","pet_fe","pet_ff","pet_fg","pet_fh","pet_fi","pet_fj","pet_fk","pet_fl","pet_fm","pet_fn","pet_fo","pet_fp"]

async def Hunt(message):
  while(1):
    await message.channel.send("rpg hunt")
    def check(message):
      return message.author.id == 555955826880413696 and any(word in message.content for word in name) and (any(word in message.content for word in hunt) or any(word in message.content for word in jail))
    try:
      await client.wait_for("message",timeout=10,check=check)
    except asyncio.TimeoutError:
      await message.channel.send('rpg hunt')
    def stop(message):
      return message.author == client.user and message.content == "#stop hunt"
    try:
      await client.wait_for("message", timeout=62, check=stop)
      break
    except asyncio.TimeoutError:
      continue
  await message.channel.send("!1")
  return

async def Work(message,action):
  while(1):
    await message.channel.send(f"rpg {action}")
    def stop(message):
      return message.author == client.user and message.content == "#stop work"
    try:
      await client.wait_for("message", timeout=303, check=stop)
      break
    except asyncio.TimeoutError:
      continue
  await message.channel.send("!2")
  return

async def Adv(message):
  while(1):
    y = 3600
    await message.channel.send("rpg adv")
    def check(message):
      return message.author == client.user and message.content.startswith("adv in")
    try:
      msg = await client.wait_for("message", timeout=10, check=check)
      if msg.content.startswith("adv in "):
        y=0
        timecounter = msg.content.split("adv in ",1)[1]
        pettime = timecounter
        if "h" in pettime:
          hour = int(timecounter.split("h",1)[0])
          y = y + hour*3600
        if "h" in pettime and "m" in pettime:
          minute = timecounter.split("h ",1)[1]
          minute = int(minute.split("m",1)[0])
          y = y + minute*60
        if "m" in pettime and "h" not in pettime:
          minute = int(timecounter.split("m",1)[0])
          y = y + minute*60
        await message.channel.send(f"**{pettime}** = {y}")
    except asyncio.TimeoutError:
      await message.channel.send("rpg adv")
    def stop(message):
      return message.author == client.user and message.content == "#stop adv"
    try:
      await client.wait_for("message", timeout=y+3, check=stop)
      break
    except asyncio.TimeoutError:
      continue
  await message.channel.send("!3")
  return

async def Ed(message):
  while(1):
    y = 10800
    await message.channel.send("rpg buy ed lb")
    def check(message):
      return message.author == client.user and message.content.startswith("ed in")
    try:
      msg = await client.wait_for("message", timeout=10, check=check)
      if msg.content.startswith("ed in"):
        y=0
        timecounter = msg.content.split("ed in ",1)[1]
        pettime = timecounter
        if "h" in pettime:
          hour = int(timecounter.split("h",1)[0])
          y = y + hour*3600
        if "h" in pettime and "m" in pettime:
          minute = timecounter.split("h ",1)[1]
          minute = int(minute.split("m",1)[0])
          y = y + minute*60
        if "m" in pettime and "h" not in pettime:
          minute = int(timecounter.split("m",1)[0])
          y = y + minute*60
        await message.channel.send(f"**{pettime}** = {y}")
    except asyncio.TimeoutError:
      await message.channel.send("rpg buy ed lb")
    def stop(message):
      return message.author == client.user and message.content == "#stop ed"
    try:
      await client.wait_for("message", timeout=y+5, check=stop)
      break
    except asyncio.TimeoutError:
      continue
  await message.channel.send("!4")
  return

async def HealH(message):
  while(1):
    await message.channel.send("rpg heal")
    await asyncio.sleep(5)
    await message.channel.send("rpg hunt")
    def stop(message):
      return message.author == client.user and message.content == "#stop hunt"
    try:
      await client.wait_for("message", timeout=57, check=stop)
      break
    except asyncio.TimeoutError:
      continue
  await message.channel.send("!!")
  return

async def AdvH(message):
  while(1):
    y = 3590
    await message.channel.send("rpg heal")
    await asyncio.sleep(5)
    await message.channel.send("rpg heal")
    await asyncio.sleep(5)
    await message.channel.send("rpg adv")
    def check(message):
      return message.author == client.user and message.content.startswith("adv in")
    try:
      msg = await client.wait_for("message", timeout=10, check=check)
      if msg.content.startswith("adv in "):
        y=0
        timecounter = msg.content.split("adv in ",1)[1]
        pettime = timecounter
        if "h" in pettime:
          hour = int(timecounter.split("h",1)[0])
          y = y + hour*3600
        if "h" in pettime and "m" in pettime:
          minute = timecounter.split("h ",1)[1]
          minute = int(minute.split("m",1)[0])
          y = y + minute*60
        if "m" in pettime and "h" not in pettime:
          minute = int(timecounter.split("m",1)[0])
          y = y + minute*60
        await message.channel.send(f"**{pettime}** = {y}")
    except asyncio.TimeoutError:
      await message.channel.send("rpg adv")
    def stop(message):
      return message.author == client.user and message.content == "#stop adv"
    try:
      await client.wait_for("message", timeout=y+5, check=stop)
      break
    except asyncio.TimeoutError:
      continue
  await message.channel.send("!!!")
  return

async def Farm(message,action):
  if action == "farm_potato":
    execute = "rpg farm potato"
  elif action == "farm_bread":
    execute = "rpg farm bread"
  elif action == "farm_carrot":
    execute = "rpg farm carrot"
  else:
    execute = "rpg farm"
  while(1):
    await message.channel.send(f"{execute}")
    def stop(message):
      return message.author == client.user and message.content == "#stop farm"
    try:
      await client.wait_for("message", timeout=602, check=stop)
      break
    except asyncio.TimeoutError:
      continue
  await message.channel.send("!5")
  return

async def Pet(message,action):
  initial = str(action.split("pet_",1)[1])
  if initial.startswith("l"):
    part_a = "learn"
    part_b = str(initial.split("l",1)[1])
  elif initial.startswith("f"):
    part_a = "find"
    part_b = str(initial.split("f",1)[1])
  execute = f"rpg pets adv {part_a} {part_b}"
  y = 4040
  while(1):
    await message.channel.send("rpg pets adv claim")
    await asyncio.sleep(2)
    await message.channel.send("rpg pets adv claim")
    await asyncio.sleep(2)
    await message.channel.send(f"{execute}")
    #y=4040
    pettime = "default"
    def check(message):
      return message.author == client.user and message.content.startswith("pet in")
    try:
      msg = await client.wait_for("message", timeout=10, check=check)
      if msg.content.startswith("pet in"):
        y=0
        timecounter = msg.content.split("pet in ",1)[1]
        pettime = timecounter
        if "h" in pettime:
          hour = int(timecounter.split("h",1)[0])
          y = y + hour*3600
        if "h" in pettime and "m" in pettime:
          minute = timecounter.split("h ",1)[1]
          minute = int(minute.split("m",1)[0])
          y = y + minute*60
        if "m" in pettime and "h" not in pettime:
          minute = int(timecounter.split("m",1)[0])
          y = y + minute*60
      await message.channel.send(f"**{pettime}** = {y}")
    except asyncio.TimeoutError:
      await message.channel.send(f"**{pettime}** = {y}")
      await message.channel.send(f"{execute}")
    def stop(message):
      return message.author == client.user and message.content == "#stop pet"
    try:
      await client.wait_for("message", timeout=y+5, check=stop)
      break
    except asyncio.TimeoutError:
      continue
  await message.channel.send("!6")
  return

async def Restart_Program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

@client.event
async def on_message(message):
  global FHunt,FWork,FEdgy,FPett,FFarm,FAdvs
  global channel1
  channel1 = client.get_channel(828941473096794142)
  n1 = str(client.user.name)
  n2 = str(client.user.id)
  if message.channel == channel1 or message.content.endswith("#allowclient---self"):
    pass
  else:
    return
  if message.author.id == 555955826880413696:
    msg = await channel1.history(limit=1).flatten()
    msg = msg[0]
    if 'jail' in msg.content and n1 in msg.content:
      await message.channel.send("#stop 3")
    if 'jail' in msg.content and n2 in msg.content:
      await channel1.send('Jail Reset')
      await Restart_Program()
    if msg.content.startswith('Your pet has started an adventure and will be back in') and message.channel == channel1:
      timecounter = msg.content.split("in ",1)[1]
      timecounter = timecounter.split("!",1)[0]
      hour = timecounter.split("h",1)[0]
      hour_a = hour.rstrip('0123456789')
      hour = int(hour[len(hour_a):])
      minute = timecounter.split("h ",1)[1]
      minute = int(minute.split("m",1)[0])
      second = timecounter.split("m ",1)[1]
      second = int(second.split("s",1)[0])
      if second>10: minute = minute+1
      await asyncio.sleep(2)
      await channel1.send(f"pet in {hour}h {minute}m")
  if message.author == client.user:
    if message.content.startswith("#start"):
      action = str(message.content.split("#start ",1)[1])
      if action == "hunt":
        FHunt = 1
        await Hunt(message)
        FHunt = 0
      elif action == "chop" or action == "axe" or action == "bowsaw" or action == "chainsaw" or action == "fish" or action == "net" or action == "boat" or action == "bigboat":
        FWork = 1
        await Work(message,action)
        FWork = 0
      elif action == "adv":
        FAdvs = 1
        await Adv(message)
        FAdvs = 0
      elif action == "ed":
        FEdgy = 1
        await Ed(message)
        FEdgy = 0
      elif action == "healhunt":
        FHunt = 1
        await HealH(message)
        FHunt = 0
      elif action == "healadv":
        FAdvs = 1
        await AdvH(message)
        FAdvs = 0
      elif action == "farm" or action == "farm_potato" or action == "farm_bread" or action == "farm_carrot":
        FFarm = 1
        await Farm(message,action)
        FFarm = 0
      elif any(word in action for word in pets):
        FPett = 1
        await Pet(message,action)
        FPett = 0
      else:
        return
    if message.content.startswith("#reset"):
      await Restart_Program()
    if message.content.startswith("#stop 3"):
      await message.channel.send("#stop hunt")
      await message.channel.send("#stop work")
      await message.channel.send("#stop farm")
    if message.content.startswith("#stop 4"):
      await message.channel.send("#stop hunt")
      await message.channel.send("#stop work")
      await message.channel.send("#stop farm")
      await message.channel.send("#stop adv")
    if message.content.startswith("#status"):
      embedS = discord.Embed(title="Game Status",color=0x0000ff)
      global act
      if FHunt==1: act = "Up"
      else: act = "Down"
      embedS.add_field(name='Hunt',value=f"\t{act}", inline=True)
      if FWork==1: act = "Up"
      else: act = "Down"
      embedS.add_field(name='Work',value=f"\t{act}", inline=True)
      if FAdvs==1: act = "Up"
      else: act = "Down"
      embedS.add_field(name='Adv',value=f"\t{act}", inline=True)
      if FEdgy==1: act = "Up"
      else: act = "Down"
      embedS.add_field(name='Edgy',value=f"\t{act}", inline=True)
      if FFarm==1: act = "Up"
      else: act = "Down"
      embedS.add_field(name='Farm',value=f"\t{act}", inline=True)
      if FPett==1: act = "Up"
      else: act = "Down"
      embedS.add_field(name='Pet',value=f"\t{act}", inline=True)
      await message.channel.send(embed=embedS)
    else:
      return
  else:
    return

client.run(os.getenv("TOKEN"),bot=False)