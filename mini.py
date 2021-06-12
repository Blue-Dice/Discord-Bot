import discord
import os
import asyncio

client = discord.Client()

lume = 555955826880413696

@client.event
async def on_ready():
    print('you have been successfully tricked by blueberry')

@client.event
async def on_message(message):
    minion = discord.utils.get(message.guild.roles, name = 'Mini-Berry')
    channel1 = client.get_channel(853267392754221077)
    if message.channel != channel1:
        return
    if minion in message.author.roles:
        if message.content.startswith('#upgrade'):
            await message.channel.send('rpg guild upgrade')
            def check1(message):
                embeds = message.embeds
                return message.author.id == lume and 'Guild successfully upgraded!' in embeds.description
            try:
                msg = await client.wait_for('message',timeout=10,check=check1)
            except:
                return
        if message.content.startswith('#history'):
            msg = await channel1.history(limit=2).flatten()
            msg = msg[1]
            embeds = msg.embeds
            if 'Guild successfully upgraded!' in embeds.description:
                await message.channel.send('successful upgrade')

client.run(os.getenv('TOKEN'))