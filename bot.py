import os
import discord
from discord.ext import commands
import googletrans
import keep_alive

# Create a translator object
translator = googletrans.Translator()

# The discord client
client = discord.Client()

# Notify on console that the discord bot is ready
@client.event
async def on_ready():
    activity = discord.Game(name="Type !help for commands", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("The bot is ready!")

# Responds to commands
@client.event
async def on_message(message):
    # Checks that the bot is not the one who sent a message
    if message.author == client.user:
        return

    # Hello test command
    if message.content.startswith("!hello"):
        await message.channel.send("Hello! {}".format(message.author.mention))
    
    # Help info command
    if message.content.startswith("!help"):
        embed = discord.Embed(title="zZz Translate Help", description="Use this command to Translate into specific text:", color=0x00ff00)
        embed.add_field(name="=======================================================", value="-----------------------------------------------------------------------------------------", inline=False)
        embed.add_field(name="!en", value="Translate to English", inline=True)
        embed.add_field(name="!cn", value="Translate to Chinese", inline=True)
        embed.add_field(name="!ja", value="Translate to Japanese", inline=True)
        embed.add_field(name="!it", value="Translate to Italian", inline=True)
        embed.add_field(name="!de", value="Translate to Spanish", inline=True)
        embed.add_field(name="!es", value="Translate to Chinese", inline=True)
        embed.add_field(name="!fr", value="Translate to French", inline=True)
        embed.add_field(name="!nl", value="Translate to Dutch", inline=True)
        embed.add_field(name="!ru", value="Translate to Russian", inline=True)
        embed.add_field(name="!pt", value="Translate to Portughese", inline=True)
        embed.add_field(name="!bn", value="Translate to Bengali", inline=True)
        embed.add_field(name="!th", value="Translate to Thai", inline=True)
        embed.add_field(name="!uk", value="Translate to Ukrainan", inline=True)
        embed.add_field
        embed.add_field(name="!ko", value="Translate to Korean", inline=True)
        embed.add_field(name="!ga", value="Translate to Irish", inline=True)
        embed.add_field
        embed.add_field(name="!mk", value="Translate to Irish", inline=True)
        embed.add_field
        embed.add_field(name="!ro", value="Translate to Irish", inline=True)
        embed.add_field
        embed.add_field(name="!tr", value="Translate to Irish", inline=True)
        embed.add_field(name="=======================================================", value="-----------------------------------------------------------------------------------------", inline=False)
        embed.add_field(name="Example for translate text on German:", value="-----------------------------------------------------------------------------------------", inline=False)
        embed.add_field(name="!de hi how are you?", value="-----------------------------------------------------------------------------------------", inline=False)
        embed.add_field(name="Every time you have a text to translate, you have to put the code fist! :wink:", value="-----------------------------------------------------------------------------------------", inline=False)
        
        
              
      
        await message.channel.send(embed=embed)


    # Ping test command
    ping = (round(client.latency * 1000))
    if message.content.startswith("!ping"):
        await message.channel.send("Pong! {} ` ` -> `{}` ms ".format(message.author.mention, ping))
    
    # Translate google engine
    if message.content.lower().startswith("!en "):
        # Grab the message after the command
        msg = message.content[3:]
        # Get the language of the file
        translated_message = translator.translate(msg)
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))

    if message.content.lower().startswith("!jp "):
        msg = message.content[3:]
        # Directly converts English to Chinese (Traditional)
        translated_message = translator.translate(msg, dest="zh-tw")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    
    if message.content.lower().startswith("!it "):
        msg = message.content[3:]
        # Directly converts English to Italian (Traditional)
        translated_message = translator.translate(msg, dest="it")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    
    if message.content.lower().startswith("!de "):
        msg = message.content[3:]
        # Directly converts English to German (Traditional)
        translated_message = translator.translate(msg, dest="de")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    
    if message.content.lower().startswith("!es "):
        msg = message.content[3:]
        # Directly converts English to Spanish (Traditional)
        translated_message = translator.translate(msg, dest="es")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))

    if message.content.lower().startswith("!fr "):
        msg = message.content[3:]
        # Directly converts English to French (Traditional)
        translated_message = translator.translate(msg, dest="fr")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    
    if message.content.lower().startswith("!nl "):
        msg = message.content[3:]
        # Directly converts English to Chinese (Traditional)
        translated_message = translator.translate(msg, dest="nl")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))

    if message.content.lower().startswith("!ru "):
        msg = message.content[3:]
        # Directly converts English to Chinese (Traditional)
        translated_message = translator.translate(msg, dest="ru")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))

    if message.content.lower().startswith("!pt "):
        msg = message.content[3:]
        # Directly converts English to Chinese (Traditional)
        translated_message = translator.translate(msg, dest="pt")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))

    if message.content.lower().startswith("!bn "):
        msg = message.content[3:]
        # Directly converts English to Chinese (Traditional)
        translated_message = translator.translate(msg, dest="bn")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))

    if message.content.lower().startswith("!th "):
        msg = message.content[3:]
        # Directly converts English to Chinese (Traditional)
        translated_message = translator.translate(msg, dest="th")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    if message.content.lower().startswith("!ja "):
        msg = message.content[3:]
        # Directly converts English to Spanish (Traditional)
        translated_message = translator.translate(msg, dest="ja")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    if message.content.lower().startswith("!uk "):
        msg = message.content[3:]
        # Directly converts English to Spanish (Traditional)
        translated_message = translator.translate(msg, dest="uk")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    if message.content.lower().startswith("!ko "):
        msg = message.content[3:]
        # Directly converts English to Spanish (Traditional)
        translated_message = translator.translate(msg, dest="ko")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    if message.content.lower().startswith("!ga "):
        msg = message.content[3:]
        # Directly converts English to Spanish (Traditional)
        translated_message = translator.translate(msg, dest="ga")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    if message.content.lower().startswith("!mk "):
        msg = message.content[3:]
        # Directly converts English to Spanish (Traditional)
        translated_message = translator.translate(msg, dest="mk")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    if message.content.lower().startswith("!ro "):
        msg = message.content[3:]
        # Directly converts English to Spanish (Traditional)
        translated_message = translator.translate(msg, dest="ro")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
    if message.content.lower().startswith("!tr "):
        msg = message.content[3:]
        # Directly converts English to Spanish (Traditional)
        translated_message = translator.translate(msg, dest="tr")
        await message.channel.send("{} ` ` -> `{}`".format(message.author.mention, translated_message.text))
keep_alive.keep_alive()   
client.run(os.getenv('TOKEN'))
