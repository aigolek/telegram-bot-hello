import random
import requests
import telebot
from telebot import types

new_echo_bot = telebot.TeleBot("xxx") 

@new_echo_bot.message_handler(commands=['start'])
def send_welcome(message):
	new_echo_bot.reply_to(message, "Howdy, how are you doing?")

# @new_echo_bot.message_handler(commands=['help'])
# def send_choice(message):
#     markup = types.ReplyKeyboardMarkup(row_width=2)
#     itembtn1 = types.KeyboardButton('Almaty')
#     itembtn2 = types.KeyboardButton('New York')
#     itembtn3 = types.KeyboardButton('San Francisco')
#     markup.add(itembtn1, itembtn2, itembtn3)

#     chat_id = message.chat.id
#     new_echo_bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)

# Warm Up tasks: 
# Task 1 

@new_echo_bot.message_handler(content_types=['text'])
def send_good_bye(message):
    goodbye_prompts = ['bye', 'good bye', 'arividerchi', 'see ya', 'see you', 'later']
    text = message.text.lower()
    if text in goodbye_prompts:
        new_echo_bot.send_message(message.chat.id, 'Good bye, fella!')    

# Task 2  
    text = message.text
    is_question = message.text.find('?') > -1
    answers = [
        "The answer lies in your heart",
        "I do not know",
        "Almost certainly",
        "No",
        "Yes",
        "Why do you need to ask?",
        "Go away. I do not wish to answer at this time.",
        "Time will only tell",
    ]
    if is_question:
        new_echo_bot.send_message(message.chat.id, random.choice(answers))        

# Task 3
# joke topics
    text = message.text.lower()
    JOKE_API_URL = "http://api.icndb.com/jokes/random"
    if text.find('joke') > -1:
        res = requests.get(JOKE_API_URL) 
        print (res.status_code)
        print (res.json()['value']['joke'])
        if res.status_code == 200:
            new_echo_bot.send_message(message.chat.id, res.json()['value']['joke'])   

# weather topic
    # city = "Almaty"
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Almaty!')
    itembtn2 = types.KeyboardButton('New York')
    itembtn3 = types.KeyboardButton('San Francisco')
    markup.add(itembtn1, itembtn2, itembtn3)

    chat_id = message.chat.id
    # new_echo_bot.send_message(chat_id, "Choose one letter:", reply_markup=markup)
    city = message.text
    WEATHER_API_URL="http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=xxx"
    chat_id = message.chat.id
    if city:
        res = requests.get(WEATHER_API_URL) 
        if res.status_code == 200:
            print(markup)
            new_echo_bot.send_message(message.chat.id, "It is " + str(res.json()['main']['temp']) + " degrees in " + city + ': ' + res.json()['weather'][0]['description'], markup)     

# USD rate to KZT topic
    text = message.text.lower()
    CURRENCY_API_URL = "https://free.currconv.com/api/v7/convert?q=USD_KZT&compact=ultra&apiKey=xxx"
    if text.find('usd') > -1:
        res = requests.get(CURRENCY_API_URL) 
        print (res.status_code)
        print (res.json())
        if res.status_code == 200:
            new_echo_bot.send_message(message.chat.id, "KZT to USD: " + str(res.json()['USD_KZT']))  
new_echo_bot.polling()    