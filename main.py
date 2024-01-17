from telebot.types import Message, CallbackQuery
from telebot import TeleBot
import wikipedia
import re


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
TOKEN = '6431574145:AAEIa652Ktc0ImsWBKyHLkZV3JdNXh6Xyjw'


bot = TeleBot(TOKEN,
              parse_mode='HTML')


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
@bot.message_handler(commands=["start"])
def start(message: Message,):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"🌐 Отправьте мне любое слово, и я найду его значение на Wikipedia.")


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
@bot.message_handler(content_types=["text"])
def handle_text(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Сбор информации ...")
    # bot.delete_message(chat_id, message.id)
    bot.reply_to(message, getwiki(message.text))


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
wikipedia.set_lang("ru")


def getwiki(s):
    try:
        ny = wikipedia.page(s)

        wikitext = ny.content[:1000]

        wikimas = wikitext.split('.')

        wikimas = wikimas[:-1]

        wikitext2 = ''

        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                           wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return '<b>❌ В энциклопедии нет информации об этом!</b>'


# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_- 
bot.polling(none_stop=True)
