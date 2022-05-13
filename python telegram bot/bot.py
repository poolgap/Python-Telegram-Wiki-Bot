from array import array
from ast import Pass
import config
import telebot
import wikipedia, re

bot = telebot.TeleBot(config.token)
wikipedia.set_lang('ru')



@bot.message_handler(commands=['start'])
def start(message):
    WelcMess = f"Привет, {message.from_user.first_name}! \n"
    bot.send_message(message.chat.id, WelcMess + 'Что вы хотите найти в современной энциклопедии?', parse_mode="html")

@bot.message_handler(content_types=['text'])
def mess(message):
    word = message.text.strip().lower()
    try:
        final_message = wikipedia.summary(word)  
    except wikipedia.exceptions.PageError:
        final_message = ""
    
    bot.send_message(message.chat.id, final_message, parse_mode='html')


if __name__ == '__main__':
     bot.infinity_polling()
