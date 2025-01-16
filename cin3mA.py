import discord
import asyncio
import random
import os
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.typing = True
intents.guilds = True
intents.voice_states = True
intents.message_content = True

EXEMPT_USER_ID = 424574968504909825

# Spotify API
load_dotenv("token.env")
spotify = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

# Define the command prefix for the bot
bot = commands.Bot(command_prefix='c!', intents=intents)

# Event to play a specific song when the bot is mentioned
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Verify if the bot was mentioned
    if bot.user in message.mentions:
        # Verify if the author is in a voice channel
        if message.author.voice:
            channel = message.author.voice.channel
            try:
                # Connect to the voice channel
                vc = await channel.connect()

                # Load the audio file
                audio_source = discord.FFmpegPCMAudio('intro.mp3')

                # Play the audio file
                if not vc.is_playing():
                    vc.play(audio_source)

                    # Wait until the audio file finishes playing
                    while vc.is_playing():
                        await asyncio.sleep(1)

                # Disconnect from the voice channel
                await vc.disconnect()
            except discord.ClientException:
                await message.channel.send('Já estou em um canal de voz.')
            except discord.InvalidArgument:
                await message.channel.send('Canal de voz inválido.')
            except Exception as e:
                await message.channel.send(f'Ocorreu um erro: {e}')
        else:
            await message.channel.send('Pilantra!')

    await bot.process_commands(message)

# Help command to display the bot's commands
bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title='Cin3mA Bot', description='Bot para o servidor New Lands', color=0x00ff00)
    embed.add_field(name='c!status', value='Mostra o status do bot', inline=False)
    embed.add_field(name='c!hello', value='Cumprimenta o usuário', inline=False)
    embed.add_field(name='c!somar num num', value='Realiza a soma entre dois numeros', inline=False)    
    embed.add_field(name='c!mover @membro', value='Move um membro para um canal de voz', inline=False)
    embed.add_field(name='c!arrastao @membro', value='Bagunçar a vida de alguém', inline=False)
    embed.add_field(name='c!bernometro @membro', value='Mostra a intenção de um membro', inline=False)
    embed.add_field(name='c!iago', value='O que será que ele é?', inline=False)
    embed.add_field(name='c!igor', value='O que será que ele é?', inline=False)
    embed.add_field(name='c!bernie', value='O que será que ele é?', inline=False)
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
    
# Generate a random number
@bot.command()
async def igor(ctx):
    await ctx.send(f'Igor está {random.randint(0, 100)}% 🐒 hoje!')
    
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
        
@bot.command()
async def convocar(ctx, member: discord.Member):
    if ctx.author.id == EXEMPT_USER_ID:
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            await ctx.send("Não tenho permissão para apagar mensagens.")
            return
        except discord.HTTPException:
            await ctx.send("Erro ao tentar apagar a mensagem.")
            return
        
        # Verify if the member is in a voice channel
        if member.voice is None:
            await ctx.send('#%@#&!$(#$!2193#!&#)')
            return
        
        # Search for the voice channel
        channel = discord.utils.get(ctx.guild.voice_channels, name='🛋aA Alta Ordem!😈')
        if channel is None:
            await ctx.send('Canal de voz não encontrado.')
            return
        
        try:
            # Move the member to the voice channel
            await member.move_to(channel)
        except discord.Forbidden:
            await ctx.send('1')
        except discord.HTTPException:
            await ctx.send('2')

# Command to troll a member
@bot.command()
@commands.cooldown(1, 120, commands.BucketType.user)  # Cooldown: 1 uso a cada 120 segundos por usuário
async def arrastao(ctx, member: discord.Member):
    
    # Verify if the user is exempt from the cooldown
    if ctx.author.id == EXEMPT_USER_ID:
        # Reset the cooldown for the command
        arrastao.reset_cooldown(ctx)
    
    if member.voice is None:
        await ctx.send(f'{member.mention} não está em um canal de voz.')
        return
       
     
    # Get all the voice channels in the guild
    voice_channels = [channel for channel in ctx.guild.channels if isinstance(channel, discord.VoiceChannel)]

    # Get the channel where the member is
    member_channel = member.voice.channel
    
    try:
        #for _ in range(3):
        for channel in voice_channels:
            if channel.name != '🛋aA Alta Ordem!😈':       
                if member.voice is not None:
                    await member.move_to(channel)
                    await asyncio.sleep(0.1)
                    
        for channel in reversed(voice_channels):
            if channel.name != '🛋aA Alta Ordem!😈':    
                if member.voice is not None:
                    await member.move_to(channel)
                    await asyncio.sleep(0.1)
        
        await member.move_to(member_channel)
    except discord.Forbidden:
        await ctx.send('Não tenho permissão para mover membros.')
    except discord.HTTPException:
        await ctx.send('Erro ao mover membro.')
        
# Handle cooldown errors
@arrastao.error
async def arrastao_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'O comando está em cooldown! Tente novamente em {round(error.retry_after, 2)} segundos.')

@bot.command()
async def bernometro(ctx, member: discord.Member):
    await ctx.send(f'{member.mention} tem {random.randint(0, 100)}% de intenção.')
    
# Command to sum two numbers
@bot.command()
async def somar(ctx, num1: int, num2: int):
    await ctx.send(f'A soma de {num1} + {num2} é igual a {num1 + num2}')
    
# TOKEN
load_dotenv("token.env")
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)