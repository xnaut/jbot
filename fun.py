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

    # COMMAND: Chooses random number between 1 & 10,000
    if message.content.startswith(PF_RANDNUM):
        await client.send_message(message.channel, randint(0, 10000))

    # COMMAND: Rock, paper, scissors
    if message.content.startswith(PF_RPS):
        rps = {
            'rock': 'paper',
            'paper': 'scissors',
            'scissors': 'rock'
        }

        bot_ans = list(rps)[randint(0, 2)]
        user_ans = message.content.replace(PF_RPS, '').strip()

        if user_ans in rps:
            if bot_ans == user_ans:
                await client.send_message(message.channel, 'I chose {0}. We tied!'.format(bot_ans))
                return
                
            if bot_ans == rps[user_ans]:
                await client.send_message(message.channel, 'I chose {0}. You lose!'.format(bot_ans))

            else:
                await client.send_message(message.channel, 'I chose {0}. You win!'.format(bot_ans))

        else:
            await client.send_message(message.channel, 'Invalid answer')
