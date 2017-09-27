# Imports
import datetime
from random import randint

pf = '.'

# Main commands
pf_help = pf + 'help'
pf_randint = pf +'randint'
pf_repeat = pf + 'repeat'
pf_quote = pf + 'q'

# Experimental Commands
pf_equote = pf + 'eq'

# Colors
green = 0x6DC066
yellow = 0xfffb4c

# Functions
def time(time):
    hour = (int(time.strftime('%I')) - 5) # Temporary fix.
    hour = str(hour)

    if time.strftime('%d') == str(datetime.datetime.now().day):
        return time.strftime('Today at ' + hour + ':%M %p')

    else:
        return time.strftime('%b %d at ' + hour + ':%M %p')


async def commands(discord, message, client):
    async def quote_embed(author, channel, color):
        em = discord.Embed(description=message.content, color=color)
        em.set_author(name=author.display_name, icon_url=author.avatar_url)
        em.set_footer(text=time(message.timestamp))

        await client.send_message(channel, embed=em)

    # COMMAND: Quote message
    if message.content.startswith(pf_quote):
        tmp = message.content.replace(pf_quote, '').strip().lower()

        async for message in client.logs_from(message.channel, limit=500):

            if tmp in message.content.lower() and message.content.startswith(pf_quote) == False:
                await quote_embed(message.author, message.channel, green)
                return

    # COMMAND: Help
    if message.content.startswith(pf_help):
        f = open('help.txt', 'r')
        em = discord.Embed(title='JBot Help', description=f.read(), color=0x6DC066)
        await client.send_message(message.channel, embed=em)
        f.close()

    # COMMAND: Repeats anything the user says
    if message.content.startswith(pf_repeat):
        await client.delete_message(message)
        await client.send_message(message.channel, message.content.replace('$repeat', ''))

    # COMMAND: Chooses random number between 1 & 1000
    if message.content.startswith(pf_randint):
        await client.send_message(message.channel, randint(1, 1000))

    # -- EXPERIMENTAL COMMANDS --
    # Experimental Quote
    def percent(a, b):
        return 100 * a / b

    if message.content.startswith(pf_equote):
        best_match = ['', 0]
        tmp = message.content.replace(pf_equote, '').lower().split()

        async for message in client.logs_from(message.channel, limit=500):
            matches = 0
            tmp2 = message.content.lower().split()

            if message.content.startswith(pf_equote) == False:
                for i in range(0, len(tmp)):
                    for j in range(0, len(tmp2)):
                        if tmp[i] == tmp2[j]:
                            matches += 1

                    if percent(matches, len(tmp)) > best_match[1]:
                        best_match[0] = message.content
                        best_match[1] = percent(matches, len(tmp))

                        if best_match[1] == 100.0:
                            await quote_embed(message.author, message.channel, yellow)
                            break
