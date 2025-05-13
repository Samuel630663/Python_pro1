import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea!')
    
    
practicas_ecologicas = [
    "Almacena el aceite, .",
    "Usar bolsas de tela en lugar de plástico.",
    "Apagar las luces al salir de una habitación.",
    "Usar transporte público o bicicleta en lugar de coche.",
    "Reducir el consumo de agua al ducharse o lavar los dientes.",
    "Plantar árboles y cuidar el medio ambiente.",
    "Comprar productos locales y de temporada.",
    "Evitar el uso de productos desechables.",
    "Separar los residuos en casa para reciclar.",
    "Utilizar bombillas LED para ahorrar energía."
]

@bot.command()
async def practicas(ctx):
    mensaje = random.choice(practicas_ecologicas)
    await ctx.send(mensaje)
    
    
    
token = ""
    
    
bot.run(token)