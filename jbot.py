import asyncio, discord, time
from commands import commands
from fun import fun
from utility import utility

client = discord.Client()

start_time = time.time()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

COMMAND_PREFIX = '.'

# Bot commands
@client.event
async def on_message(message):

    # Display all messages in terminal
    print('[{0}] {1}: {2}'.format(message.channel, message.author, message.content))

    # Stops the bot from acting upon itself
    if message.author == client.user:
        return

    # Always on commands. Includes main features, e.g. help and quote.
    await commands(COMMAND_PREFIX, discord, message, client)

    # Commands that serve little purpose. e.g. repeat and rock, paper, scissors.
    await fun(COMMAND_PREFIX, discord, message, client)

    # Useful commands. e.g. web search and unit conversion.
    #await utility(COMMAND_PREFIX, discord, message, client)

    if message.content.startswith('.uptime'):
        await client.send_message(message.channel, '{0} seconds'.format(round(time.time() - start_time)))


# Fetches bot token from external .txt file
with open('token.txt', 'r') as f:
    token = f.read().strip()

client.run(token)
client.close()
