import discord
from discord.ext import commands
import random
import os

description = "Эм это я тот самый сын маминой подруги который любит биологию,я был созданый великим человеком.Я разкажу про глобальное потепления"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)
@bot.event
async def on_ready():
  print(f'Logged in as {bot.user} (ID: {bot.user.id})')
print('------')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def Glnerd(ctx):
    await ctx.send(f'Эм это я тот самый сын маминой подруги который любит биологию,я был спрограмирован великим человеком.Я разкажу про глобальное потепления:nerd:!')
@bot.command()
async def Glcomads(ctx):
    await ctx.send(f' Мои команды:?Globaltempkr ?Globaltempthen ?Globaltempresson и ?Globaltempimg ?Globaltsslki:nerd:.!')
@bot.command()
async def Globaltempkr(ctx):
    await ctx.send(f'Что такое глобальное потепление?Ок сейчас разкажу:Глобальное потепление - это неуклонное повышение средней температуры Земли, измеряемое повышением глобальной температуры поверхности, вызванное или находящееся под влиянием непрерывных выбросов парниковых газов, таких как диоксид углерода и ХФУ, такие как метан и закись азота, а также других загрязнителей воздуха, загрязняющих более 90% атмосферы и влияющих на чувствительность климата и уровень осадков:nerd:!')
@bot.command()
async def Globaltempthen(ctx):
    await ctx.send(f' Основная причина глобального потепления — деятельность человека. Люди сжигают ископаемое топливо (уголь, нефть, газ), в результате чего в атмосферу выбрасываются газы — углекислый газ, метан, оксид азота, фторированные газы. Они ведут к возникновению парникового эффекта, потому что способны поглощать много солнечного тепла. На долю углекислого газа приходится 64% антропогенных причин глобального потепления:nerd:!')
@bot.command()
async def Globaltsslki(ctx):
    await ctx.send(f' Ссылки:https://www.un.org/ru/global-issues/climate-change https://yandex.ru/video/preview/14802010931453091581 https://yandex.ru/video/preview/11780711322646551427:nerd:!')
@bot.command()
async def Globaltempimg(ctx):
  img_name = random.choice(os.listdir('images'))
  with open(f'images/{img_name}', 'rb') as f:
    picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
bot.run('')

