import discord
from discord.ext import commands
import re
from datetime import datetime, timedelta
from secret_key import TOKEN

# Configurar intents
intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name} has connected to Discord!")

@bot.command(name="sleep_cycle")
async def sleep_cycle(ctx):
    mensagem = (
        "**Olá! Sou o bot do Ciclo do Sono.**\n\n"
        "*Aqui estão os comandos que você pode usar:* \n\n"
        "**1. Para saber a melhor hora para acordar:**\n"
        "Digite `!hora_dormir` seguido da hora em que você vai dormir.\n"
        "**Exemplo:** `!hora_dormir 22h00` ou `!hora_dormir 22:00`\n\n"
        "**2. Para saber a melhor hora para dormir:**\n"
        "Digite `!hora_acordar` seguido da hora em que você precisa acordar no dia seguinte.\n"
        "**Exemplo:** `!hora_acordar 06h00` ou `!hora_acordar 06:00`\n\n"
        "**3. Para obter mais informações sobre o que é um ciclo do sono:**\n"
        "Digite `!info` para ver uma breve explicação sobre o ciclo do sono.\n\n"
    )
    await ctx.send(mensagem)

@bot.command(name="hora_dormir")
async def hora_acordar(ctx, hora: str):
    # Usar expressões regulares para extrair a hora e os minutos
    match = re.match(r"(\d{1,2})[h:](\d{2})", hora)

    if match:
        horas, minutos = map(int, match.groups())
        if 0 <= horas < 24 and 0 <= minutos < 60:
            hora_formatada = datetime.strptime(f"{horas:02d}:{minutos:02d}", "%H:%M")
            intervalo = timedelta(minutes=90)
            lista_horas = []
            for i in range(0, 7):
                nova_hora = hora_formatada + i * intervalo
                lista_horas.append(nova_hora.strftime("%H:%M"))
            resposta = "\n".join(f"**{i+1}º Ciclo Completo:** {hora}" for i, hora in enumerate(lista_horas[1:]))

            await ctx.send(
                f"**CICLO DO SONO**\n\n"
                f"Se você for dormir às **{lista_horas[0]}** e deseja acordar no final de um ciclo de sono, "
                f"atente-se ào seu ciclo de descanso:\n\n{resposta}\n\n"
                f"Portanto, se você acordar por volta das **{lista_horas[-1]}**, estará no final de um ciclo de sono completo.\n"
                f"Espero ter ajudado!"
            )

        else:
            await ctx.send("A hora fornecida está fora do intervalo válido. Certifique-se de que está entre 00:00 e 23:59.")
    else:
        await ctx.send("Formato de hora inválido. Use o formato `HHhMM` ou `HH:MM`.")

@bot.command(name="hora_acordar")
async def hora_acordar(ctx, hora: str):
    # Usar expressões regulares para extrair a hora e os minutos
    match = re.match(r"(\d{1,2})[h:](\d{2})", hora)

    if match:
        horas, minutos = map(int, match.groups())
        if 0 <= horas < 24 and 0 <= minutos < 60:
            hora_formatada = datetime.strptime(f"{horas:02d}:{minutos:02d}", "%H:%M")
            intervalo = timedelta(minutes=90)
            lista_horas = []
            for i in range(0, 7):
                nova_hora = hora_formatada - i * intervalo
                lista_horas.append(nova_hora.strftime("%H:%M"))
            resposta = "\n".join(f"**{i+1}º Ciclo Completo:** {hora}" for i, hora in enumerate(lista_horas[-2::-1]))

            await ctx.send(
                f"**CICLO DO SONO**\n\n"
                f"Se você precisar acordar às **{lista_horas[0]}** e deseja ter uma boa noite de descanso, "
                f"atente-se ao seu ciclo do sono:\n\n{resposta}\n\n"
                f"Portanto, se você dormir por volta das **{lista_horas[-1]}**, conseguirá ter um ciclo de sono completo.\n"
                f"Espero ter ajudado!"
            )

        else:
            await ctx.send("A hora fornecida está fora do intervalo válido. Certifique-se de que está entre 00:00 e 23:59.")
    else:
        await ctx.send("Formato de hora inválido. Use o formato `HHhMM` ou `HH:MM`.")

@bot.command(name="info")
async def info(ctx):
    mensagem = (
        "🛌 **Sobre o Ciclo do Sono**\n\n"
        "O ciclo do sono dura cerca de 90 minutos e inclui as fases NREM (sono leve e profundo) e REM (sonhos). Acordar no final de um ciclo pode ajudar você a se sentir mais descansado e energizado. 5 - 6 ciclos são ideais para uma boa noite de sono.\n\n"
    )
    await ctx.send(mensagem)

bot.run(TOKEN)
