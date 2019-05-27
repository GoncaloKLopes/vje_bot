import discord
import os

BITES_FOLDER = "sound_bites"
TOKEN = os.environ["DISCORD_VJ_EMMIE_BOT"]
INVOKE = "!vje"

client = discord.Client()


@client.event
async def on_ready():
    print("VJ EMMIE ON DA MICROPHONE!")


@client.event
async def on_message(message):
    if message.content.startsWith(INVOKE):
