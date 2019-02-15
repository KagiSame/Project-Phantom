#Phantom 2 Beta Insider Bulid (V 0.4.1 SU 1 CodeName Divine Dayousei EX) is
#Made by KagiSame with help from The Arcane Brony :D

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
    print("V 0.4.1 EX (SU1) CodeName Divine Dayousei EX (Service Update 1)")
    game = discord.Game("V 0.4.1 EX CodeName Divine Dayousei EX")  
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
        await message.author.send("***Phantom Help*** \n **ph help** - Shows this message \n **ph ver** - Shows Phantom's version \n **ph neko** - Sends random image with Nekos :3 \n **ph pong** - Phantom pings to You :D \n **ph ping** - Phantom pongs to you :3 \n **ph changelog** - Displays Phantom's Changelog \n **ph info** - Displays Phantom's runtime info \n **ph lewdneko** - Send Lewd Nekos (Useable only in NSFW) \n **ph invite** - Invite Phantom to your server ")
        print("[Help]:",message.author)
    #Displays Version (\n makes new line)
    if message.content.startswith("ph ver"):
        await message.channel.send("Phantom 2 Beta (Insider Build) \n Written by Hina Kagiyama (KagiSame) with help from The Arcane Brony \n ``Buildinfo : 20181219`` \n CodeName : Divine Daiyousei EX")
        print("[Version]:",message.author)
    #Multiline text test (Depricated Command)
    if message.content.startswith("ph multitest"):
        await message.channel.send("This is sample \n multi line message \n :thinking:")

    #Random Neko Command (Powered by nekos.py API)
    lewdnekos=["lewd","hentai","nsfw_neko_gif"]  
    
    
    if message.content.startswith("ph lewdneko"):
         if (message.channel.is_nsfw()):
            await message.channel.send("Neko for you :3",)
            await message.channel.send(nekos.img(random.choice(lewdnekos)))
            print("[LewdNeko]:",message.author)
         else:
             await message.channel.send(" :x: You can't use this command here Try NSFW Channels... ")
             print("[LewdNekoFail]:",message.author)

   
   
   
   
   
    #Random Neko Command (Powered by nekos.py API)
    if message.content.startswith("ph neko"):
        await message.channel.send(nekos.img("neko"))
        print("[Neko]:",message.author)
    
    #Changelog
    if message.content.startswith("ph changelog"):
        await message.channel.send("****Project Phantom Changelog**** \n ***V.0.1.0 Amazing Awoo*** - Intital Release of Phantom 1.x Branch \n ***v 0.2.0 Beautiful Byakuren*** Added Image commands last release of 1.x Branch \n ***v 0.3.0 Cold Cirno*** - Complete Rewrite from Python 3.6.x to 3.7  \n Start of Phantom 2.x Branch \n Neko command using Nekos.py API \n ***v 0.4.0 Divine Dayousei*** \n - A lot of Bug Fixes \n -Optimized Few Things (Thanks to The Arcane Brony) \n - ph help now outputs to DMs \n - Added support for NSFW \n **v.0.4.1 EX** \n Also Known as Divine Daiyousei Service Update 1 \n -Lot of Bugfixes mostly \n -More Nekos :3 ")    
        print("[Changelog]:",message.author)
    
    #Phantom's runtime info
    if message.content.startswith("ph info"):
        current_time = time.time()
        diffrence = int(round(current_time - start_time))
        await message.channel.send("**Uptime**:\n{}\n**Running on**:\n{}\n**Phantom's Time**:\n{}".format(*[datetime.timedelta(seconds=diffrence),platform.platform(),time.strftime("%H:%M:%S")]))
        print("[Info]:",message.author)
    
    #Invite Command
    if message.content.startswith("ph invite"):
        await message.channel.send("Invite Phantom to Your Server : \n https://discordapp.com/oauth2/authorize?&client_id=482669512131477504&scope=bot&permissions=0")
        print("[Invite]:",message.author)





#Run Phantom
client.run("inserttokenhere")       


