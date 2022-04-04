import telebot

CHAVE_API = "5047033784:AAEMIoMRS-WleYm-6BOAQp4uY_kLMP-Mxzo"

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=["start"])
def responder(message):
    bot.reply_to(message, "Oi Antonio, vamos ver Netflix ?")


bot.polling()