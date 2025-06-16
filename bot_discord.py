import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Diccionario para guardar datos temporales por usuario
user_data = {}

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def cotizar(ctx):
    # Inicia la cotización
    user_data[ctx.author.id] = {}  # Almacena datos del usuario
    await ctx.send("🛠️ **Cotización de impresión 3D**\n"
                   "1️⃣ ¿Qué material usarás? (Ej: PLA, ABS, PETG):")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        # Paso 1: Material
        material_msg = await bot.wait_for("message", check=check, timeout=60)
        material = material_msg.content.upper()
        user_data[ctx.author.id]["material"] = material

        # Paso 2: Costo del rollo
        await ctx.send("2️⃣ 💵 ¿Cuánto cuesta el rollo completo (en MXN)? Ej: 500")
        rollo_msg = await bot.wait_for("message", check=check, timeout=60)
        user_data[ctx.author.id]["costo_rollo"] = float(rollo_msg.content)

        # Paso 3: Gramos del rollo
        await ctx.send("3️⃣ ⚖️ ¿Cuántos gramos tiene el rollo completo? Ej: 1000")
        gramos_rollo_msg = await bot.wait_for("message", check=check, timeout=60)
        user_data[ctx.author.id]["gramos_rollo"] = float(gramos_rollo_msg.content)

        # Paso 4: Gramos usados en la pieza
        await ctx.send("4️⃣ 🔍 ¿Cuántos gramos usará la pieza? Ej: 200")
        gramos_pieza_msg = await bot.wait_for("message", check=check, timeout=60)
        user_data[ctx.author.id]["gramos_pieza"] = float(gramos_pieza_msg.content)

        # Paso 5: Horas de impresión
        await ctx.send("5️⃣ ⏱️ ¿Cuántas horas tardará la impresión? Ej: 7")
        horas_msg = await bot.wait_for("message", check=check, timeout=60)
        user_data[ctx.author.id]["horas"] = float(horas_msg.content)

        # Paso 6: Costo por hora (electricidad, desgaste)
        await ctx.send("6️⃣ ⚡ ¿Costo por hora de impresión (electricidad/desgaste)? Ej: 10")
        costo_hora_msg = await bot.wait_for("message", check=check, timeout=60)
        user_data[ctx.author.id]["costo_hora"] = float(costo_hora_msg.content)

        # Cálculos finales
        costo_material = (user_data[ctx.author.id]["gramos_pieza"] / user_data[ctx.author.id]["gramos_rollo"]) * user_data[ctx.author.id]["costo_rollo"]
        costo_tiempo = user_data[ctx.author.id]["horas"] * user_data[ctx.author.id]["costo_hora"]
        total = costo_material + costo_tiempo

        # Respuesta final
        embed = discord.Embed(title="✅ **Cotización Final**", color=0x00ff00)
        embed.add_field(name="Material", value=user_data[ctx.author.id]["material"], inline=False)
        embed.add_field(name="Gramos usados", value=f"{user_data[ctx.author.id]['gramos_pieza']}g", inline=True)
        embed.add_field(name="Costo material", value=f"${costo_material:.2f} MXN", inline=True)
        embed.add_field(name="Tiempo", value=f"{user_data[ctx.author.id]['horas']} horas", inline=True)
        embed.add_field(name="Costo tiempo", value=f"${costo_tiempo:.2f} MXN", inline=True)
        embed.add_field(name="**Total estimado**", value=f"**${total:.2f} MXN**", inline=False)
        await ctx.send(embed=embed)

    except asyncio.TimeoutError:
        await ctx.send("⌛ **Tiempo agotado**. Usa `!cotizar` de nuevo.")
    except ValueError:
        await ctx.send("❌ **Error**: Asegúrate de ingresar números válidos.")

bot.run(TOKEN)