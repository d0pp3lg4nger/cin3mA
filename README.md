# 🎬 cin3mA - Discord Bot

Welcome to **cin3mA**, a Discord bot designed to enhance the fun and interactivity in our server! Whether you're chatting, gaming, or just hanging out, cin3mA brings a variety of commands and features to the table, including the ability to play a specific song when tagged with an `@mention`. 🎵

---

## 🚀 Features

- 🎶 **Play a Song on Mention:**
  - When the bot is tagged, it joins your voice channel and plays a specific song.

- 🎉 **Fun and Interactive Commands:**
  - **c!hello**: Greets the user.
  - **c!status**: Displays the bot's current status.
  - **c!somar [num1] [num2]**: Calculates the sum of two numbers.
  - **c!bernometro @member**: Shows a member's "intention percentage."
  - **c!arrastao @member**: A playful command to shuffle a member through voice channels (cooldown included).
  - **c!mover @member [voice channel]**: Moves a member to a specified voice channel.

- 🤖 **Custom Interactions:**
  - **c!iago** and **c!igor**: Fun, personalized responses for specific names.
  - **c!bernie**: Displays a special gif.

---

## 📋 Commands Overview

| Command                  | Description                                       |
|--------------------------|---------------------------------------------------|
| `c!hello`               | Greets the user.                                 |
| `c!status`              | Displays the bot's online status.                |
| `c!somar [num1] [num2]` | Sums two numbers.                                |
| `c!bernometro @member`  | Shows a member's "intention percentage."         |
| `c!arrastao @member`    | Shuffles a member through voice channels.        |
| `c!mover @member`       | Moves a member to a specified voice channel.     |
| `c!iago`                | Fun, personalized response for "Iago."          |
| `c!igor`                | Fun, personalized response for "Igor."          |
| `c!bernie`              | Sends a special gif response.                    |

---

## ⚙️ How It Works

- **Voice Channel Integration:**
  - If you mention the bot while in a voice channel, it will join your channel and play a predefined MP3 file.
  - After finishing the song, the bot will leave the channel automatically.

- **Cooldown for Commands:**
  - Certain commands, like `c!arrastao`, include cooldowns to avoid spamming.

- **Custom Fun Commands:**
  - Includes playful and unique commands tailored for specific users in the server.

---

## 🛠️ Setup Instructions

1. **Install Dependencies:**
   Make sure you have Python installed along with the following libraries:
   - `discord.py`
   - `wavelink`
   - `asyncio`
   - `spotipy`
   - `python-dotenv`

   Install them using:
   ```bash
   pip install discord.py wavelink asyncio spotipy python-dotenv
   ```

2. **FFmpeg Installation:**
   - Download and install FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).

3. **Environment Setup:**
   - Create a `.env` file in the bot's directory with your Discord bot token and Spotify API credentials:
     ```env
     DISCORD_TOKEN=your_discord_bot_token
     SPOTIPY_CLIENT_ID=your_spotify_client_id
     SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
     ```

4. **Run the Bot:**
   Launch the bot using:
   ```bash
   python bot.py
   ```

---

## 📂 Folder Structure

```
cin3mA/
├── bot.py            # Main bot script
├── .env              # Environment variables
├── requirements.txt  # Dependencies
├── README.md         # This file
├── music.mp3         # Predefined song file
```

---

## 📝 License
This project is for personal use and is shared among friends. Feel free to adapt it to your own server needs.

---

## 🌟 Future Improvements

- Add a queue system for songs.
- Support for YouTube and other streaming platforms.
- More personalized and dynamic commands.
- Enhanced error handling for smoother interactions.

---

Enjoy using **cin3mA** to make your Discord server even more lively! 🎉
