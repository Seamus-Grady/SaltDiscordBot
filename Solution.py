import random
import discord
import os

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

replies = ['SaltBot ignored orders!', 'SaltBot turned away!', 'SaltBot pretended not to notice!', 'SaltBot won\'t obey!', 'SaltBot ignored orders and kept sleeping!']
users = {'famoussg': 294235145802874883,
         'swifty': 356273710833074208,
         'gussillypants': 590638706491129857,
         'kushlan': 380766452656898059,
         'lizll12': 690301400265392229,
         'miranna': 562417447978795020,
         'ethereal_blade33': 602319628043157531,
         'jacqueline': 551166872012193794,
         'yerryperez': 636305160997568514}

@client.event
async  def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if 'saltbot go' in message.content.lower():
        if message.author.id == 294235145802874883:
            if 'saltbot go attack ' in message.content.lower():
                await message.channel.send('https://tenor.com/view/salt-grand-blue-throw-the-salt-throw-begone-gif-15107011')
                txt = message.content.lower().split()
                if txt[-1] in users:
                    await message.channel.send('<@' + str(users[txt[-1]])+'>')
                else:
                    await message.channel.send('Sorry I couldn\'t find that user')
            else:
                await message.channel.send('https://tenor.com/view/salt-grand-blue-throw-the-salt-throw-begone-gif-15107011')
        else:
            if message.author.id != 790777091003383838:
                chance = random.randint(0, 1)
                if chance == 0:
                    if 'saltbot go attack ' in message.content.lower():
                        await message.channel.send(
                            'https://tenor.com/view/salt-grand-blue-throw-the-salt-throw-begone-gif-15107011')
                        txt = message.content.split()
                        if txt[-1] in users:
                            await message.channel.send('<@' + str(users[txt[-1]]) + '>')
                        else:
                            await message.channel.send('Sorry I couldn\'t find that user')
                    else:
                        await message.channel.send(
                            'https://tenor.com/view/salt-grand-blue-throw-the-salt-throw-begone-gif-15107011')
                else:
                    await message.channel.send(replies[random.randint(0, 4)])
    elif 'hello saltbot' in message.content.lower():
        await message.channel.send('Hello ' + message.author.name + '\nI am SaltBot I may not be a big bot, but like my brother BreadBot, I am here to serve you\nI have two commands:\nSaltBot go\nSaltBot go attack username\n'
                                                                   'I\'ll upload my master\'s favorite gif with that command and mention the user if using the attack command\n')


client.run(TOKEN)