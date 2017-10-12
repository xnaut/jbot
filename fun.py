from random import randint

async def fun(command_prefix, discord, message, client):
    PF_DICE = command_prefix + 'dice'
    PF_RANDNUM = command_prefix + 'randnum'
    PF_REPEAT = command_prefix + 'repeat'
    PF_RPS = command_prefix + 'rps'

    # COMMAND: Rolls a die with 6 sides
    if message.content.startswith(PF_DICE):
        await client.send_message(message.channel, randint(1, 6))

    # COMMAND: Repeats anything the user says
    if message.content.startswith(PF_REPEAT):
        try:
            await client.delete_message(message)

        finally:
            await client.send_message(message.channel, message.content.replace(PF_REPEAT, ''))

    # COMMAND: Chooses random number between 1 & 1000
    if message.content.startswith(PF_RANDNUM):
        await client.send_message(message.channel, randint(0, 10000))

    # COMMAND: Rock, paper, scissors
    if message.content.startswith(PF_RPS):
        rps = ('rock', 'paper', 'scissors')

        bot_answer = rps[randint(0, 2)]
        player_answer = message.content.replace(PF_RPS, '').strip()

        print(bot_answer)
        print(player_answer)

        if player_answer in rps:
            if player_answer == bot_answer:
                await client.send_message(message.channel, 'Tie!')

            if player_answer == rps[0] and bot_answer == rps[1]:
                await client.send_message(message.channel, 'I chose {0}, you lose!'.format(rps[1]))

            if player_answer == rps[1] and bot_answer == rps[2]:
                await client.send_message(message.channel, 'I chose {0}, you lose!'.format(rps[2]))

            if player_answer == rps[2] and bot_answer == rps[1]:
                await client.send_message(message.channel, 'I chose {0}, you lose!'.format(rps[1]))

        else:
            await client.send_message(message.channel, 'Invalid answer')
