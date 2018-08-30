import telepot
from pprint import pprint

telepot.api.set_proxy("https://186.200.35.37:3128")
bot = telepot.Bot('684539582:AAFYcidGBScltH_nd07xpAIwimIDJ4SndLI')

pprint(bot.getMe())
upd=0
# print(bot.getUpdates(offset=upd))

# offset=939343314
while(True):
    s=bot.getUpdates(offset=upd)
    if len(s) > 0:
        print(s)
        print(s[0].get('message').get('text'))
        upd = s[-1]['update_id'] +1
            
            



# [{u'message': {u'date': 1459927254, u'text': u'/start', u'from': {u'username': u'adilkhash', u'first_name': u'Adil', u'id': 31337}, u'message_id': 1, u'chat': {u'username': u'adilkhash', u'first_name': u'Adil', u'type': u'private', u'id': 7350}}, u'update_id': 649179764}]
# bot.sendMessage(176748136,'Hey!')













# import telebot
# from telebot import apihelper
# import socket
# import socks
# 
# ip = '98.174.90.36'  # change your proxy's ip
# port = 14474  # change your proxy's port
# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
# socket.socket = socks.socksocket
# apihelper.proxies = {'https':'socks5://98.174.90.36:14474'}
# 
# bot = telebot.TeleBot("684539582:AAFYcidGBScltH_nd07xpAIwimIDJ4SndLI")
# 
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")
# 
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
# 
# bot.polling()