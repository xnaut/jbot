# Imports
import datetime
from random import randint

PF= '.' # The symbol at the beginning of all commands

# Main commands
PF_HELP = PF + 'help'
PF_RANDNUM = PF + 'randnum'
PF_REPEAT = PF + 'repeat'
PF_QUOTE = PF + 'q'

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

async def commands(discord, message, client):
    async def quote_embed(author, channel, color):
        em = discord.Embed(description=message.content, color=color)
        em.set_author(name=author.display_name, icon_url=author.avatar_url)
        em.set_footer(text=time(message.timestamp))

        await client.send_message(channel, embed=em)

    # COMMAND: Quote message
    if message.content.startswith(PF_QUOTE):
        tmp = message.content.replace(PF_QUOTE, '').strip().lower()

        async for message in client.logs_from(message.channel, limit=10000):
            if tmp in message.content.lower() and message.content.startswith(PF_QUOTE) == False:
                await quote_embed(message.author, message.channel, colors['green'])
                return

    # COMMAND: Help
    if message.content.startswith(PF_HELP):
        with open('help.txt', 'r') as f:
            em = discord.Embed(title='JBot Help', description=f.read(), color=colors['green'])
            await client.send_message(message.channel, embed=em)

    # COMMAND: Repeats anything the user says
    if message.content.startswith(PF_REPEAT):
        try:
            await client.delete_message(message)

        finally:
            await client.send_message(message.channel, message.content.replace('.repeat', ''))

    # COMMAND: Chooses random number between 1 & 1000
    if message.content.startswith(PF_RANDNUM):
        await client.send_message(message.channel, randint(0, 10000))
