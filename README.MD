# 🤖🇫🇷❌ Anti French Bot

This 🤖 is designed to 🛡️ a Discord server by 🔍 detecting and 🚫 blocking messages written in 🇫🇷 (French) in a specific 🗨️ general chat 📺. If a message in 🇫🇷 is detected, the 🤖 will 🗑️ delete the message and ⏲️ timeout the user for a set period. The 🤖 also provides several ➡️ commands for server 🛠️ admins to customize its behavior.

## ⭐ Features

- 🔍 Detects messages written in 🇫🇷 in the specified general 📺.
- 🗑️ Deletes the message and ⏲️ times out the user for a set ⏱️ duration.
- Provides ➡️ commands for 🛠️ admins to configure:
  - The general 📺 channel ID to monitor.
  - The 🇫🇷-specific 📺 channel for users to use instead.
  - The ⏱️ duration of the ⏲️ for users posting messages in 🇫🇷.

## 📝 Commands

The 🤖 provides the following ➡️ commands for server 🛠️ admins:

1. **/set\_general\_channel**: Sets the 📺 channel that should be monitored for 🇫🇷 messages.
2. **/set\_french\_channel**: Sets the 📺 channel where 🇫🇷 messages are allowed.
3. **/set\_timeout\_duration**: Sets the ⏱️ duration (in 🕒 minutes) for which a user should be ⏲️ timed out after posting a 🇫🇷 message in the general 📺.

## 📦 Requirements

- 🐍 Python 3.8+
- 🤖 discord.py
- 🌱 python-dotenv
- 🌐 langdetect

## ⚙️ Installation

1. 🌀 Clone this 📦 repository:

   ```sh
   git clone https://github.com/Pelotrio/AntiFrenchBot.git
   ```

2. Navigate to the project 📂 directory:

   ```sh
   cd AntiFrenchBot
   ```

3. Install the required 📦 packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` 📄 file in the root 📂 directory of the project and ➕ add your Discord 🤖 token:

   ```env
   DISCORD_BOT_TOKEN=YOUR_DISCORD_BOT_TOKEN_HERE
   ```

## ▶️ Usage

Run the 🤖 with the following command:

```sh
python main.py
```

Once the 🤖 is running, it will start 👀 monitoring the specified 📺 channel for 🇫🇷 messages and 🎬 act accordingly.

## 🌱 Environment Variables

- **DISCORD\_BOT\_TOKEN**: Your Discord 🤖 token.

## 🤝 Contributing

Contributions are 👋 welcome! If you find a 🐛 bug or have a ⭐ feature request, feel free to open an 🗂️ issue or create a 🔀 pull request.

