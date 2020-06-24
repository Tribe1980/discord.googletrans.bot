import os
import discord
from discord.ext import commands
import googletrans
import keep_alive


PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')

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

    # Help translate command
    if message.content.startswith("!help"):
        await message.channel.send("Hello! {} \nUse this command to Translate into specific text:" 
        "\n!en = translate to English" 
        "\n!jp = translate to Chinese" 
        "\n!jp = translate to Chinese"
        "\n!it = translate to Italian"
        "\n!de = translate to German"
        "\n!es = Translate to Spanish"
        "\n!fr = Translate to French"
        "\n!nl = Translate to Dutch"
        "\n!ru = Translate to Russian"
        "\n!pt = Translate to Portughese"
        "\n!bn = Translate to Bengali"
        "\n!th = translate to Thai"
        .format(message.author.mention))

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
keep_alive.keep_alive()   
client.run(os.getenv('TOKEN'))
