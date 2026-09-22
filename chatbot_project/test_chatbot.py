from chatbot import ChatBot

bot = ChatBot()

while True:

    message = input("You: ")

    if message.lower() == "exit":
        break

    response = bot.get_response(message)

    print("Bot:", response)
    