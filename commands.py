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

# Colors
green = 0x6DC066
yellow = 0xfffb4c

# Test

async def commands(discord, message, client):
    async def quote_embed(author, channel, color):
        em = discord.Embed(description=message.content, color=color)
        em.set_author(name=author.display_name, icon_url=author.avatar_url)
        em.set_footer(text=message.timestamp)
        await client.send_message(channel, embed=em)

    # COMMAND: Quote message
    if message.content.startswith(pf_quote):
        match_found = False
        tmp = message.content.replace(pf_quote, '').strip().lower()


        async for message in client.logs_from(message.channel, limit=15):

            if tmp in message.content.lower() and message.content.startswith(pf_quote) == False:
                await quote_embed(message.author, message.channel, green)
                match_found = True
                return

        if match_found == False:
            # This is really error prone. e
            tmp = tmp.split()

            async for message in client.logs_from(message.channel, limit=100):
                matches = 0
                tmp2 = message.content.split()

                for i in range(0, len(tmp)):
                    for x in range(0, len(tmp2)):
                        if tmp[i] == tmp2[x]:
                            matches += 1

                if matches == len(tmp):
                    print('success')
                    await quote_embed(message.author, message.channel, yellow)
                    return

        if match_found == False:
            await client.send_message(message.channel, '0 results found.')


                #print('matches ' + str(matches))
                #print('tmp ' + str(len(tmp)))

    # COMMAND: Help
    if message.content.startswith(pf_help):
        f = open('help.txt', 'r')
        em = discord.Embed(title='JBot Help', description=f.read(), color=0x6DC066)
        await client.send_message(message.channel, embed=em)
        f.close()

    # COMMAND: Repeats anything the user says
    if message.content.startswith(pf_repeat):
        await client.delete_message(message)
        await client.send_message(message.channel, message.content.replace("$repeat", ""))

    # COMMAND: Chooses random number between 1 & 1000
    if message.content.startswith(pf_randint):
        await client.send_message(message.channel, randint(1, 1000))
