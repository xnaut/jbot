from datetime import datetime
from random import randint

pf = '.'

# Main commands
pf_help = pf + 'help'
pf_randint = pf +'randint'
pf_repeat = pf + 'repeat'
pf_quote = pf + 'q'

# Owner commands
pf_disable = pf + 'disable'


async def commands(discord, message, client):
    async def quote_embed(author, channel):
        em = discord.Embed(description=message.content, color=0x6DC066)
        em.set_author(name=author.display_name, icon_url=author.avatar_url)
        em.set_footer(text=message.timestamp)
        await client.send_message(channel, embed=em)

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

    # Help
    if message.content.startswith(pf_help):
        f = open('help.txt', 'r')
        em = discord.Embed(title='JBot Help', description=f.read(), color=0x6DC066)
        await client.send_message(message.channel, embed=em)
        f.close()

    # Repeats anything the user says
    if message.content.startswith(pf_repeat):
        await client.delete_message(message)
        await client.send_message(message.channel, message.content.replace("$repeat", ""))

    # Chooses random number between 1 & 1000
    if message.content.startswith(pf_randint):
        await client.send_message(message.channel, randint(1, 1000))
