import discord
from discord.ext import commands

# Создаем объект Intents
intents = discord.Intents.default()
intents.message_content = True  # Включаем возможность отслеживать содержимое сообщений

# Устанавливаем префикс команд
bot = commands.Bot(command_prefix='!', intents=intents)

# Переменная для хранения счетчика
counter = 0

# Обработчик команды !пал
@bot.command()
async def пал(ctx):
    global counter
    counter += 1
    await ctx.send(f"Настя утопила технику {counter} раз")

# Запуск бота с токеном
bot.run('MTI4NjI1MDY4MDg5MzMxMzA5NQ.GH8JEf.SBINaRJss62v3LgMaDZZ0uHUHBSkD81gl_-k3A')
