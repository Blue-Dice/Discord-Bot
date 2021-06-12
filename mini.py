import discord
import os
import asyncio

client = discord.Client()

lume = 555955826880413696

@client.event
async def on_ready():
    await client.get_channel(853267392754221077).send('Hax Mode: ON')
    print('you have been successfully tricked by blueberry')

@client.event
async def on_message(message):
    minion = discord.utils.get(guild.roles, name = 'Mini-Berry')
    channel1 = client.get_channel()
    if minion in message.author.roles:
        if message.content.startswith('#upgrade'):
            await message.channel.send('rpg guild upgrade')
            def check1(message):
                embed = message.embeds
                return message.author.id == lume and any(embed in embeds)
            try:
                msg = await client.wait_for('message',timeout=10,check=check1)
                await message.channel.send(f'{msg}')
                await message.channel.send(f'{msg.content}')
                await message.channel.send(f'{msg.embed}')
                embeds = msg.embed
                for embed in embeds:
                    await message.channel.send(f'{embed.to_dict()}')
            except:
                return

client.run(os.getenv('TOKEN'))