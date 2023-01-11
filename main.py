# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import discord
import json

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$kill GradientGlow'):
        await message.channel.send('@GradientGlow is now become DEAD')
    if message.content.startswith('$kill nwtanic'):
        await message.channel.send('I will not kill my beautiful, sexy master.')

# Use token to sign in to Discord
with open('config.json') as config_file:
    config_dict = json.load(config_file)

client.run(config_dict["bot_token"])
