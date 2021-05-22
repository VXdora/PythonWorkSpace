import discord

TOKEN = 'ODQ0ODM0MzI1MjM3MDcxODky.YKYLRw.KOhZsuQQJsQFZXwOlWYI72vGyYE'

client = discord.Client()

@client.event
async def on_ready():
    print('successed login')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '/neko':
        await message.channel.send('にゃーん')

client.run(TOKEN)
