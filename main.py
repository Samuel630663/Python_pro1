import discord
import random
import os
import requests
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
    
@bot.command()
async def mem(ctx):
    with open('imagenes/mem1.jpg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
    
@bot.command()
async def meme_aleatori(ctx):
    
    nombre_imagen = random.choice(os.listdir('imagenes'))
    
    with open(f'imagenes/{nombre_imagen}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_perro_imagen():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('perro')
async def imagen_perro(ctx):
    
    image_url = get_perro_imagen()
    await ctx.send(image_url)


token = ''

bot.run(token)