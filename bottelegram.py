import telebot

CHAVE_API = "CHAVE_API"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["start"])
def responder(message):
    bot.reply_to(message, "Oi Antonio, vamos ver Netflix ?")


bot.polling()