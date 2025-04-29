import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea!')
    

@bot.command()
async def saludar(ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    
    if mensaje == 'hola':
        
        await ctx.send('Hola, ¿cómo estás?')
        
    elif mensaje == 'que onda':
        
        await ctx.send('Todo bien')
    
    elif mensaje == 'klk':
        
        await ctx.send('Todo bien')
        
    
    if mensaje == 'adios':
        
        await ctx.send('adios, que estes bien')
        
    elif mensaje == 'chao':
        
        await ctx.send('hasta luego')
    
    elif mensaje == 'bye':
        
        await ctx.send('chao')
        
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send(f'{slapped} just got slapped for {reason}')


token = ''

bot.run(token)