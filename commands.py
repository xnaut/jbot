# Imports
import datetime
from random import randint

PF= '.' # The symbol at the beginning of all commands

colors = {
    "green": 0x6DC066,
    "yellow": 0xfffb4c
}

# Functions
def time(time):
    if time.strftime('%d') == str(datetime.datetime.now().day):
        return time.strftime('Today at ' + '%H:%M %p GMT+0')

    else:
        return time.strftime('%b %d at %H:%M %p GMT+0')

async def commands(command_prefix, discord, message, client):
    # Main commands
    PF_HELP = command_prefix + 'help'
    PF_QUOTE = command_prefix + 'q'

    async def quote_embed(author, channel, color):
        em = discord.Embed(description=message.content, color=color)
        em.set_author(name=author.display_name, icon_url=author.avatar_url)
        em.set_footer(text=time(message.timestamp))

        await client.send_message(message.channel, embed=em)

    # COMMAND: Help
    if message.content.startswith(PF_HELP):
        with open('help.txt', 'r') as f:
            em = discord.Embed(title='JBot Help', description=f.read(), color=colors['green'])
            await client.send_message(message.channel, embed=em)

    # COMMAND: Quote message
    if message.content.startswith(PF_QUOTE):
        tmp = message.content.replace(PF_QUOTE, '').strip().lower()

        async for message in client.logs_from(message.channel, limit=10000):
            if tmp in message.content.lower() and message.content.startswith(PF_QUOTE) == False:
                await quote_embed(message.author, message.channel, colors['green'])
                return
