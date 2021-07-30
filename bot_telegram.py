import telebot

from parser_my import Parser

token = "Your Token"
bot = telebot.TeleBot(token)

parser = Parser()

keyboard = telebot.types.ReplyKeyboardMarkup(True)

keyboard.row('BTC')
keyboard.row('ETH')
keyboard.row('EOS')


def send_message_func(id, text):
    bot.send_message(id, text, reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def answer(message):
    send_message_func(message.chat.id, "Choose the cryptocurrency")


@bot.message_handler(commands=['help'])
def answer(message):
    send_message_func(message.chat.id, '''
    What this bot can do:
    This is a simple crypto-analyzer.
    commands:
    /start - bot ask you for the cryptocurrency.
    You can also choose some of the most popular crypto on the keyboard. Then bot send you 
    the latest analytics, for currency you chose, from https://ru.tradingview.com. 
    /help - bot send the message you are currently reading :)
    /new - bot send you the newest article from https://ru.tradingview.com 
    other functions are in progress''')

@bot.message_handler(content_types=['text'])
def main(message):
    id = message.chat.id
    user_crypto = message.text
    send_message_func(id, parser.get_link(user_crypto))
    send_message_func(572445254, id)


bot.polling(none_stop=True)
