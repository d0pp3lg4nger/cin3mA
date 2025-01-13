import discord
import asyncio
import yt_dlp as youtube_dl
from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.typing = True
intents.guilds = True
intents.voice_states = True
intents.message_content = True

# YoutubeDL options
ytdl_format_options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
ffmpeg_options = {
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


# Define the command prefix for the bot
bot = commands.Bot(command_prefix='c!', intents=intents)

# Function to get the audio source from a youtube video
def get_audio_source(url):
    info = ytdl.extract_info(url, download=False)
    return discord.FFmpegPCMAudio(info['url'], **ffmpeg_options)

# Event to run when the bot is mentioned
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if bot.user in message.mentions:
        if message.author.voice:
            channel = message.author.voice.channel
            try:
                vc = await channel.connect()
                
                music_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
                source = get_audio_source(music_url)
                
                vc.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
                
                while vc.is_playing():
                    await asyncio.sleep(1)
                    
                await vc.disconnect()
            except discord.errors.ClientException:
                await message.channel.send('Já estou em um canal de voz.')
            except discord.errors.InvalidArgument:
                await message.channel.send('Canal de voz invalido.')
        else:
            await message.channel.send('Olá imbogno!')
    
    await bot.process_commands(message)

# Help command to display the bot's commands
bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Cin3mA Bot', description='Bot para o servidor New Lands', color=0x00ff00)
    embed.add_field(name='c!status', value='Mostra o status do bot', inline=False)
    embed.add_field(name='c!hello', value='Cumprimenta o usuário', inline=False)
    embed.add_field(name='c!somar', value='Realiza a soma entre dois numeros', inline=False)    
    await ctx.send(embed=embed)

# Define the command to display the bot's status
@bot.command()
async def status(ctx):
    await ctx.send(f'{bot.user.name} está online!')
    
# Simple command to display a message
@bot.command()
async def hello(ctx):
    await ctx.send('Olá imbogno!')
    
@bot.command()
async def iago(ctx):
    await ctx.send('Iago gay')
    
@bot.command()
async def bernie(ctx):
    gif_url = 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcno0eGFhbTF3MmFzdHdpanBleDdrbTEzNHA1NGJvODhlOTZ6djVteCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/h8sRbOtj55JACfGn8R/giphy.gif'
    await ctx.send(gif_url)
    
# Move a member to a voice channel
@bot.command()
async def mover(ctx, member: discord.Member, channel: discord.VoiceChannel):
    if member.voice is None:
        await ctx.send('Membro não está em um canal de voz.')
        return
    try:
        await member.move_to(channel)
    except discord.Forbidden:
        await ctx.send('Não tenho permissão para mover membros.')
    except discord.HTTPException:
        await ctx.send('Erro ao mover membro.')
        
# Command to troll a member
@bot.command()
async def arrastao(ctx, member: discord.Member):
    if member.voice is None:
        await ctx.send(f'{member.mention} não está em um canal de voz.')
        return

    # Get all the voice channels in the guild
    voice_channels = [channel for channel in ctx.guild.channels if isinstance(channel, discord.VoiceChannel)]

    # Get the channel where the member is
    member_channel = member.voice.channel
    
    try:
        for _ in range(3):
            for channel in voice_channels:
                if member.voice is not None:
                    await member.move_to(channel)
                    await asyncio.sleep(1)
                    
            for channel in reversed(voice_channels):
                if member.voice is not None:
                    await member.move_to(channel)
                    await asyncio.sleep(1)
        
        await member.move_to(member_channel)
    except discord.Forbidden:
        await ctx.send('Não tenho permissão para mover membros.')
    except discord.HTTPException:
        await ctx.send('Erro ao mover membro.')
        


# Command to sum two numbers
@bot.command()
async def somar(ctx, num1: int, num2: int):
    await ctx.send(f'A soma de {num1} + {num2} é igual a {num1 + num2}')
    
# TOKEN
bot.run('TOKEN')