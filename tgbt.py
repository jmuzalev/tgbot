import telepot

telepot.api.set_proxy("https://181.15.155.245:80")
bot = telepot.Bot('684539582:AAFYcidGBScltH_nd07xpAIwimIDJ4SndLI')

print(bot.getMe())















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