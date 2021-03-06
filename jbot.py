import asyncio, discord
from commands import commands

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# Bot commands
@client.event
async def on_message(message):
    # Display all messages in terminal
    print('[' + str(message.channel) + '] ' + str(message.author) + ': ' +  str(message.content))

    # Stops the bot from acting upon itself
    if message.author == client.user:
        return

    await commands(discord, message, client)

# Fetches bot token from external .txt file
with open('token.txt', 'r') as f:
    token = f.read().strip()

client.run(token)
client.close()
