#Phantom 2 Beta Insider Bulid (V 0.3.1 CodeName Cold Cirno)
#Made by KagiSame

import platform
import nekos
import random
import discord
import time
import datetime

client = discord.Client()
start_time = time.time()

#Welcome Message when Phantom loads and Change Presence
@client.event
async def on_ready():
    print('Welcome To Phantom 2 Beta (Insider Bulid)')
    print("V 0.3.1 CodeName Cold Cirno")
    game = discord.Game("V 0.3.1 CodeName Cold Cirno")  
    await client.change_presence(status=discord.Status.online, activity=game)
    

@client.event

async def on_message(message):
    
    if message.author == client.user:
        return

    #Simple test command
    if message.content.startswith("ph ping"):
        await message.channel.send("***Pong***")
    if message.content.startswith("ph pong"):
        await message.channel.send("***Ping***")


    #Help Command
    if message.content.startswith("ph help"):
        await message.channel.send("***Phantom Help*** \n **ph help** - Shows this message \n **ph ver** - Shows Phantom's version \n **ph neko** - Sends random image with Nekos :3 \n **ph pong** - Phantom pings to You :D \n **ph ping** - Phantom pongs to you :3 \n **ph changelog** - Displays Phantom's Changelog \n **ph info** - Displays Phantom's runtime info")

    #Displays Help \n makes new line
    if message.content.startswith("ph ver"):
        await message.channel.send("Phantom 2 Beta (Insider Bulid) \n Written by Hina Kagiyama (KagiSame) \n ``Bulidinfo : 20181021``")

    #Multiline text test
    if message.content.startswith("ph multitest"):
        await message.channel.send("This is sample \n multi line message \n :thinking:")

    #Random Neko Command (Powered by nekos.py API)
    if message.content.startswith("ph neko"):
        await message.channel.send(nekos.img("neko"))
        await message.channel.send("Neko for You :3")

    #Changelog
    if message.content.startswith("ph changelog"):
        await message.channel.send("****Project Phantom Changelog**** \n ***V.0.1.0 Amazing Awoo*** - Intital Release of Phantom 1.x Branch \n ***v 0.2.0 Beautiful Byakuren*** Added Image commands last release of 1.x Branch \n ***v 0.3.0 Cold Cirno*** - Complete Rewrite from Python 3.6.x to 3.7  \n Start of Phantom 2.x Branch \nNeko command using Nekos.py API")    

    #Phantom's runtime info
    if message.content.startswith("ph info"):
        current_time = time.time()
        diffrence = int(round(current_time - start_time))
        await message.channel.send("**Uptime**:")
        await message.channel.send((datetime.timedelta(seconds=diffrence)))
        await message.channel.send("**Running on **:")
        await message.channel.send(platform.platform())
        await message.channel.send("**Phantom's Time**:")
        time_string = time.strftime("%H:%M:%S")
        await message.channel.send((time_string))
        




#Run Phantom
client.run("put_your_token_here")       
