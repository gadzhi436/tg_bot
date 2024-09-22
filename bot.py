import telebot
from config import TOKEN
import traceback

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text']) #слушаем бота
def get_text(message):
    print(message.text)
    print(type(message.text))
    if message.text.isdigit():
        print("работает")
    if message.text == "/start": #проверям сообщение от пользователя
        bot.send_message(message.from_user.id, "Здравствуй, мой дорогой друг!\nКак тебя зовут?") #отвечаем пользователю
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "напиши: Привет")
    else:
        bot.send_message(message.from_user.id, "я тебя не понимаю, напиши '/help'")

# Обработка ошибок
try:
    bot.polling(none_stop=True, interval=0)
except:
    print(f"ашипка:\n{traceback.format_exc()}")