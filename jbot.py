import asyncio, discord
from commands import commands
from fun import fun

client = discord.Client()

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

    await commands(COMMAND_PREFIX, discord, message, client)
    await fun(COMMAND_PREFIX, discord, message, client)

# Fetches bot token from external .txt file
with open('token.txt', 'r') as f:
    token = f.read().strip()

client.run(token)
client.close()
