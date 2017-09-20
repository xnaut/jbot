import asyncio
import discord
import logging
from random import randint
from owner_commands import owner_commands

client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Command prefixes
pf = '.'
pf_addquote = pf + 'addquote'
pf_randint = pf +'randint'
pf_repeat = pf + 'repeat'
pf_help = pf + 'help'
pf_quote = pf + 'q'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Log to text file
#def log(channel, user_id, message):
#    # Format - [Channel name] Username: Message
#    log_text = '[' + str(channel) + '] ' + str(user_id) + ': ' + str(message) + '\n'
#
#    print(log_text)
#
#    file = open("log.txt", "a")
#    file.write(str(log_text))
#    file.close()

# Bot commands
@client.event
async def on_message(message):
    # Display all messages in terminal
    print('[' + str(message.channel) + '] ' + str(message.author) + ': ' +  str(message.content))

    async def quote_embed(author, channel):
        em = discord.Embed(description=message.content, color=0x6DC066)
        em.set_author(name=author, icon_url=author.avatar_url)
        await client.send_message(channel, embed=em)

    # Stops the bot from acting upon itself
    if message.author == client.user:
        return

    # Chooses random number between 1 & 1000
    if message.content.startswith(pf_randint):
        await client.send_message(message.channel, randint(1, 1000))

    # Repeats anything the user says
    if message.content.startswith(pf_repeat):
        await client.delete_message(message)
        await client.send_message(message.channel, message.content.replace("$repeat", ""))

    # Adds quotes to quote file
    if message.content.startswith(pf_addquote):
        quote = message.content.replace(pf_addquote + ' ', '`')

        f = open('quotes.txt', 'a')
        f.write(quote + '\n')
        f.close()

        await client.send_message(message.channel, 'Quote added')

    # Help
    if message.content.startswith(pf_help):
        f = open('help.txt', 'r')
        em = discord.Embed(title='JBot Help', description=f.read(), color=0x6DC066)
        await client.send_message(message.channel, embed=em)
        f.close()

    # Quote message
    if message.content.startswith(pf_quote):
        tmp = message.content.replace(pf_quote, '').strip().lower()

        async for message in client.logs_from(message.channel, limit=1000):

            message_sent = False

            if tmp in message.content.lower() and message.content.startswith(pf_quote) == False:
                await quote_embed(message.author, message.channel)
                message_sent = True
                return

        if message_sent == False:
            await client.send_message(message.channel, 'No matches found.')

# Fetches bot token from external .txt file
f = open('token.txt', 'r')
token = f.read()
f.close()
token = token.strip()
client.run(token)
client.close()
