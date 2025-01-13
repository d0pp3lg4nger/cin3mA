import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.typing = True
intents.message_content = True

# Define the command prefix for the bot
bot = commands.Bot(command_prefix='c!', intents=intents)

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


# Command to sum two numbers
@bot.command()
async def somar(ctx, num1: int, num2: int):
    await ctx.send(f'A soma de {num1} + {num2} é igual a {num1 + num2}')
    
# TOKEN
bot.run('MTMyODQ2MjAwNzUwMTk4Mzc1NQ.G6DFmm.p00eH5oOUqoBK525nBvq1HHyaN_runwr8-MjRQ')