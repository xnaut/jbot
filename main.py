import asyncio
import discord
import logging
from random import randint

client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

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

    # Stops bot from acting upon itself.
    if message.author == client.user:
        return

    def quote_embed():
        em = discord.Embed(description=message.content, color=0x6DC066)
        em.set_author(name=message.author, icon_url=message.author.avatar_url)

    # Chooses random number between 1 & 1000
    if message.content.startswith('$randint'):
        await client.send_message(message.channel, randint(1, 1000))

    # Repeats anything the user says
    if message.content.startswith("$repeat"):
        await client.delete_message(message)
        await client.send_message(message.channel, message.content.replace("$repeat", ""))

    # Adds quotes to quote file
    if message.content.startswith('$addquote'):
        quote = message.content.replace('$addquote ', '`')

        f = open('quotes.txt', 'a')
        f.write(quote + '\n')
        f.close()

        await client.send_message(message.channel, 'Quote added')

    # Help
    if message.content.startswith('$help'):
        f = open('help.txt', 'r')
        em = discord.Embed(title='JBot Help', description=f.read(), color=0x6DC066)
        await client.send_message(message.channel, embed=em)
        f.close()

    # Quote message
    if message.content.startswith('$q'):
        tmp = message.content.replace('.q', '').strip().lower()
        await client.delete_message(message)

        async for message in client.logs_from(message.channel, limit=50):
            if message.content.lower().startswith(tmp):
                em = discord.Embed(description=message.content, color=0x6DC066)
                em.set_author(name=message.author, icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=em)
                return

    if message.content.startswith('.test'):
        test()


    if message.content.startswith('$rand'):
        random = randint(1, 10000)
        counter = 0

        async for message in client.logs_from(message.channel, limit=10000):

            counter += 1

            if counter == random:
                em = discord.Embed(description=message.content, color=0x6DC066)
                em.set_author(name=message.author, icon_url=message.author.avatar_url)
                await client.send_message(message.channel, embed=em)
                return
            #else:
            #    await client.send_message(message.channel, 'Nothing found.')
            #    return

# Fetches bot token from external .txt file
f = open('token.txt', 'r')
token = f.read()
f.close()
token = token.strip()
client.run(token)
client.close()
