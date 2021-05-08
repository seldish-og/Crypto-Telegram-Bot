import telebot

from parser import result

token = "Your Token"
bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('XRP')
keyboard.row('BTC')
keyboard.row('ETH')
keyboard.row('LTC')
keyboard.row('ENJ')
keyboard.row('EOS')


def send(id, text):
    bot.send_message(id, text, reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def answer(message):
    send(message.chat.id, "Choose the cryptocurrency")


@bot.message_handler(commands=['help'])
def answer(message):
    send(message.chat.id, '''
    What this bot can do:
    This is a simple crypto-analyzer.
    commands:
    /start - bot ask you for the cryptocurrency.
    You can also choose some of the most popular crypto on the keyboard. Then bot send you 
    the latest analytics, for currency you chose, from https://ru.tradingview.com. 
    /help - bot send the message you are currently reading :)
    /new - bot send you the newest article from https://ru.tradingview.com 
    other functions are in progress''')


@bot.message_handler(commands=['new'])
def answer(message):
    send(message.chat.id, result()[0]['link'])


@bot.message_handler(content_types=['text'])
def main(message):
    id = message.chat.id
    msg = message.text
    for i in result():
        if msg in i['title'].split(',')[0]:
            send(id, result()[result().index(i)]['link'])
            break
    else:
        send(id, 'Sorry, bot cannot find any new analytics for your crypto(')


bot.polling(none_stop=True)
