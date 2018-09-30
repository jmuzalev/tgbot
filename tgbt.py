#!/usr/bin/python3

import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop
from geopy import  Nominatim


# def on_callback_query(msg):
#     query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
#     print('Callback Query:', query_id, from_id, query_data)

def handle(msg):
#     msg_id = msg['offset']
    chat_id = msg['chat']['id']
    command = msg['text']
    from_id = msg['from']['id'] 
    from_first_name = msg['from']['first_name']
    print(from_id,from_first_name)
    print(msg)
#     flavor = telepot.flavor(msg)
# 
#     summary = telepot.glance(msg, flavor=flavor)
#     print (flavor, summary)
    print (command)

    if command=='/start':
        bot.sendMessage(chat_id, "C ночевкой\nС палатками\nС костром\nС алкоголем\nС рыбалкой\nС лодкой\nБез высокой вероятности разбить ебало")
    elif "Сядешь" in command or 'сядешь' in command:
        bot.sendMessage(chat_id, "Ты сядешь")
    elif 'Ковер' in command or 'ковер' in command:
        bot.sendMessage(chat_id, "А ковёр, блядь, обоссали тебе")
    elif "Друг" in command or 'друг' in command or 'друзья' in command:
        bot.sendMessage(chat_id, "Дружок с развальцованным очком?..")
    elif "Правила" in command or 'правила' in command:
        bot.sendMessage(chat_id, "тут не Вьетнам. Это — боулинг. Здесь есть правила.")
    elif "Обиделся" in command or 'обиделся' in command:
        bot.sendMessage(chat_id, "Он ранимый, очень ранимый!")
    elif "заткнись" in command or 'Заткнись' in command:
        bot.sendMessage(chat_id, "Донни, заткнись нахуй. Когда мы играем?")
    elif "Похуй" in command or 'похуй' in command or 'Похую' in command or 'похую' in command:
        bot.sendMessage(chat_id, "Он нигилист")
    elif "Расскажи историю" in command:
        bot.sendMessage(chat_id, "Ну что ты! Я тебе сейчас расскажу, вот смотри, Я тебе хорошую сейчас расскажу! Смотри, я… вот у нас здесь мух много...\
         ой-ой… мух много, понимаешь? Смотри, мухи, они тебе спать мешают, мухи. А я вот, давай я здесь насру, и они все прилетят сюда, и мы их убьем,\
          слышишь? И тебе тогда спать, ой, спать будет хорошо. Давай? Я насру, а мухи все прилетят, сюда, к нам. Ну, куда им ещё, ихнее место-то тока \
          здесь, и… ооой… хочешь, я насру здесь? И мухи, и мы их убьем! Ну что, срать?")
    elif "семерки" in command:
        bot.sendMessage(chat_id, "Бердянск потом я вспоминаю как… Там море такое, типа черного моря такое, Азов что ли... Там я срал, блядь. Голый залез\
         в море и насрал. Был пьяный тоже. \"Три семерки\" тоже выпил... Оно же по всему Союзу — «Три семёрки»! Понимаешь? ")
    elif "Отжимайся" in command or 'отжимайся' in command or 'Отжимяйся' in command or 'отжимяйся' in command:
        bot.sendMessage(chat_id, "У нас, когда отжимаешься, жопу лучше не подставлять! ")
    elif ("Хлеб" in command or 'хлеб' in command) and 'ели' in command:
        bot.sendMessage(chat_id, "Хлеб ели! Но говно-то не жрали!")    
    elif len(command)>100:
        bot.sendMessage(chat_id,'Убери это говно отсюда, блядь! Ёб твою мать, блядь! И весь пол засрал! Мудак, блядь, ну ты мудак. Я тебя сейчас убью\
         нахуй, а тебя, бля, сейчас убью, блядь!')
    elif 'Грустно' in command or 'грустно' in command:
        bot.sendMessage(chat_id,'Я зеленый слоник, я веселый головастик! Я зеленый слоник, я веселый головастик! Тиииик!')
    elif 'песн' in command:
        bot.sendMessage(chat_id,'Слушай, давай я тебе спою чего-нибудь? Ну вот, а песня такая, про цирк. Называется «Зеленый слоник». И там… Ну… \
        Я сейчас быстро спою, ну просто когда тебя увели, я эту песню сочинил. Там, значит, аккорды первые такие: "Там! Та-тарам-тара-там! \
        Та-тара-тара-там-трататара-тара-там, та-та! Зеленый слоник в наш в оркестр пришел, зеленый слоник наш трубу принес, когда ребята уходили,\
         зеленый слоник на трубе играл! Играл, пло то… про то! Подожди, сейчас, сейчас, подожди, сейчас я вспомню, сейчас, секунду… Значит… \
         Та-тара-тара-тара-та-та-та-та! Играл про то, как плохо в клетке жить, как плохо есть ху… сейчас, подожди… Как плохо есть проклятую еду,\
          как плохо всем, а хуже всего ему — зеленому слонику! Та-трай-та-та!.. Ну? Ну такая песня просто… Ну, я тебе её просто хотел, ну, исполнить,\
           понимаешь, эту песенку…') 
    elif 'бюджет' in command:
        bot.sendMessage(chat_id,'Чтоооооооооооооо?')   
    elif 'покушать' in command:
        bot.sendMessage(chat_id,'Бомжи?')   
    elif 'отдохнул' in command:
        bot.sendMessage(chat_id,'Как поспал, братишка?')
    elif 'очко' in command:
        bot.sendMessage(chat_id,'Президентское')
        
    elif 'Агламазово' in command:
        geolocator = Nominatim(user_agent="poehavsybottg")
        place="Ryazan, Ryazan Oblast, Russia"
        location = geolocator.geocode(place)
        latitude,longitude= location.latitude, location.longitude
        bot.sendLocation(chat_id, latitude, longitude)
    elif 'Агломазово' in command:
        bot.sendLocation(chat_id,54.487803, 40.243803)
        
    elif 'Петух' in command or 'петух' in command or 'петуш' in command or 'Петуш' in command:
        print('Петух здесь'+str(from_first_name))
#         bot.answerCallbackQuery(msg_id, text='Петух здесь') 
        bot.sendPhoto(chat_id,open('/root/eclipse-workspace/tgbot/photo.jpg','rb'))   
    
    elif ('Пока' in command or 'пока' in command) and ('сто' in command or 'Сто' in command):
        bot.sendMessage(chat_id, "Стоит у меня шишка, ёпт, стоит! Сядь лучше!")
    elif command=='🐓' :
        bot.sendMessage(chat_id, "Петух здесь ты")
    elif command=='Что' or command=='Чтоо' or command=='Чтооо' or command=='Чтоооооооооо' or command=='Что!' or command=='Что?':
        bot.sendMessage(chat_id, "Кафедра!!!!!!")    
    elif 'кафедр' in command or 'Кафедр' in command:
        bot.sendMessage(chat_id, "Чтоооооооооооооооооооооооооооооо!")  
    elif 'Говно' in command or 'говно' in command:
        bot.sendMessage(chat_id,'Иди под струю, сука! Мойся! ')  
        
#telepot.api.set_proxy("https://171.98.244.135:8080")
bot = telepot.Bot('684539582:AAFYcidGBScltH_nd07xpAIwimIDJ4SndLI')


MessageLoop(bot,handle).run_as_thread()
# MessageLoop(bot,{'chat': handle,
#                   'callback_query': on_callback_query}).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)

# import telepot
# from pprint import pprint
# 
# telepot.api.set_proxy("https://186.200.35.37:3128")
# bot = telepot.Bot('684539582:AAFYcidGBScltH_nd07xpAIwimIDJ4SndLI')
# 
# pprint(bot.getMe())
# upd=0
# # print(bot.getUpdates(offset=upd))
# 
# # offset=939343314
# while(True):
#     s=bot.getUpdates(offset=upd)
#     if len(s) > 0:
#         print(s)
#         print(s[0].get('message').get('text'))
#         upd = s[-1]['update_id'] +1
#             
#             



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
