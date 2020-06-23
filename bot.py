import discord
import googletrans

# Create a translator object
translator = googletrans.Translator()

# The discord client
client = discord.Client()
# The token that allows client to run the script
# token = ...
token = "NzIzODAwNDYwNjkxMjQzMDc5.Xu3Hqw.V1TV6vnaLaoummm3PamUjNKzx-k"

# Notify on console that the discord bot is ready
@client.event
async def on_ready():
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
        await message.channel.send("Hello! {} " " Use this command to Translate into specific text:" 
        "                                                  !en = translate to English                          " 
        "                                                                                                                    !jp translate to Chinese                                                                 " 
        "                                                                                 !it = translate to Italian                                                                                                                    "
        "                         !de = translate to German                                                                        "
        "                                                                     !es = Translate to Spanish                                                                                "
        "                                                             !fr = Translate to French                                                                                         "
        "                                                    !nl = Translate to Dutch                                                                                             "
        "                                                 !ru = Translate to Russian                                                                                           "
        "                                                 !pt = Translate to Portughese                                                                                      "
        "                                                 !bn = Translate to Bengali                                                                                         "
        "                                                  !th = translate to Thai                          "
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
        translated_message = translator.translate(msg, dest="zh-tw")
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
    
client.run(token)
