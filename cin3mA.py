import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.typing = True
intents.message_content = True

# Define the command prefix for the bot
bot = commands.Bot(command_prefix='c!', intents=intents)

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
    


# Command to sum two numbers
@bot.command()
async def somar(ctx, num1: int, num2: int):
    await ctx.send(f'A soma de {num1} + {num2} é igual a {num1 + num2}')
    
# TOKEN
bot.run('TOKEN')