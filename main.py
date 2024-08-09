import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_CHANNEL_ID = int(os.getenv("TARGET_CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True


class AskMeAnythingBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


client = AskMeAnythingBot()


@client.tree.command(name="ama", description="匿名で質問ができるぞ！")
@app_commands.describe(question="質問したいことを書きましょう")
async def ama(interaction: discord.Interaction, question: str):
    await interaction.response.defer(ephemeral=True)

    target_channel = client.get_channel(TARGET_CHANNEL_ID)

    if target_channel:
        await target_channel.send(f"名無しさんからの質問「{question}」")
        await interaction.followup.send("あなたの質問がこっそり送信されました😎", ephemeral=True)
    else:
        await interaction.followup.send("Error: チャンネルが見つからないよ？🧐", ephemeral=True)


@client.event
async def on_ready():
    print(f"{client.user} が Discord に接続")


client.run(BOT_TOKEN)
