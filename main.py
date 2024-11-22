from datetime import timedelta
import os
from dotenv import load_dotenv  # Import load_dotenv

import discord
from discord.ext import commands
from discord import app_commands
from langdetect import detect

load_dotenv()  # Load environment variables from the .env file

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GENERAL_CHANNEL_ID = 1308875744843272275
FRENCH_GENERAL_CHANNEL_ID = 1309133060700114985
TIMEOUT_DURATION = 10  # Default timeout duration in minutes

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    # Sync the commands with the bot globally
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s) globally.")
    except Exception as e:
        print(f"Error syncing commands: {e}")


@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Filter messages to only respond in the general channel
    # if message.channel.id != GENERAL_CHANNEL_ID:
    #     return

    # Detect language of the message if it is longer than 3 characters
    if len(message.content) > 3:
        try:
            language = detect(message.content)

        except Exception as e:
            print(f"Error detecting language: {e}")
            return

        # Check if the message is in French
        if language == 'fr':
            print(f"French message detected from {message.author}. Deleting message and timing out user.")
            # Delete the original message
            await message.delete()

            # Timeout the user for the specified duration if the bot has permission
            if message.guild.me.guild_permissions.moderate_members:
                try:
                    await message.author.timeout(timedelta(minutes=TIMEOUT_DURATION), reason="Sent a message in French in the general channel")
                    print(f"User {message.author} has been timed out for {TIMEOUT_DURATION} minutes.")
                except Exception as e:
                    print(f"Error timing out user: {e}")
            else:
                print("Bot lacks permission to timeout members.")

            # Send an embed response to the channel, mentioning the user
            embed = discord.Embed(
                title="No French in General Chat!",
                description=f"{message.author.mention}, please refrain from using French in <#{GENERAL_CHANNEL_ID}>. Use <#{FRENCH_GENERAL_CHANNEL_ID}> instead. 🥖❌ You have been timed out for {TIMEOUT_DURATION} minutes.",
                color=discord.Color.red()
            )
            await message.channel.send(embed=embed)


@bot.tree.command(name="set_general_channel", description="Sets the general channel ID.")
@app_commands.describe(channel_id="The ID of the general channel.")
async def set_general_channel(interaction: discord.Interaction, channel_id: str) -> None:
    global GENERAL_CHANNEL_ID
    GENERAL_CHANNEL_ID = channel_id
    print(f"General channel ID set to: {GENERAL_CHANNEL_ID}")
    await interaction.response.send_message(f"General channel has been set to <#{GENERAL_CHANNEL_ID}>.", ephemeral=True)


@bot.tree.command(name="set_french_channel", description="Sets the French general channel ID.")
@app_commands.describe(channel_id="The ID of the French general channel.")
async def set_french_channel(interaction: discord.Interaction, channel_id: str) -> None:
    global FRENCH_GENERAL_CHANNEL_ID
    FRENCH_GENERAL_CHANNEL_ID = channel_id
    print(f"French general channel ID set to: {FRENCH_GENERAL_CHANNEL_ID}")
    await interaction.response.send_message(f"French general channel has been set to <#{FRENCH_GENERAL_CHANNEL_ID}>.", ephemeral=True)


@bot.tree.command(name="set_timeout_duration", description="Sets the timeout duration in minutes.")
@app_commands.describe(minutes="The timeout duration in minutes.")
async def set_timeout_duration(interaction: discord.Interaction, minutes: int) -> None:
    global TIMEOUT_DURATION
    TIMEOUT_DURATION = minutes
    print(f"Timeout duration set to: {TIMEOUT_DURATION} minutes")
    await interaction.response.send_message(f"Timeout duration has been set to {TIMEOUT_DURATION} minutes.", ephemeral=True)


bot.run(TOKEN)
