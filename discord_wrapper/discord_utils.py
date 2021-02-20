import os
import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('discord_bot_token')

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} is connected on {client.guilds[0]}")


@client.event
async def on_message(message):
    if message.author.name == "DjRogerinho":
        return
    message_fmt = f'{message.author.name} said: {message.content}'
    print(message_fmt)
    if message.content == "99!":
        await message.channel.send("Cool cool cool cool cool!")


client.run(TOKEN)
