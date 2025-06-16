from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot("Cotizador3D")

trainer = ListTrainer(bot)
trainer.train([
    "Hola", "¡Hola! Usa !cotizar [gramos] [material] en Discord."
])

print("Di 'salir' para terminar.")
while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        break
    print("Bot:", bot.get_response(user_input))