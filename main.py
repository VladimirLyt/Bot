import telebot
from telebot import types
token = '6019618022:AAHpQmczWOJXOKaVpyO5ec6jFRh9S_lHOAI'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет, я бот созданный для объясния игры Лига Легенд')
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item4 = types.KeyboardButton('Персонаж')
	item5 = types.KeyboardButton('Предметы')
	item8 = types.KeyboardButton('Наш сервер')
	markup.add(item4,item5, item8)
	bot.send_message(message.chat.id, 'Выберите какая категория вас интересует', parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def message_reply(message):
	# Буря Людена инф
	with open('1.txt', 'r', encoding='utf-8') as f:
		stuff= f.read()
	photo = open('буря людена.webp', 'rb')
	with open('lux.txt', 'r', encoding='utf-8') as f:
		luxt = f.read()
	lux = open('люкс.webp', 'rb')
	# Страдания Лиандры инф
	with open('2.txt', 'r', encoding='utf-8') as f:
		stuff1 = f.read()
	photo1 = open('Страдания Лиандри.webp', 'rb')
	if message.text == 'Персонаж':
		markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item6 = types.KeyboardButton('Люкс')
		markup2.add(item6)
		bot.send_message(message.chat.id, 'Персонажи', parse_mode='html', reply_markup=markup2)
	elif message.text == 'Предметы':
		markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item1 = types.KeyboardButton("Страдания Лиандри")
		item2 = types.KeyboardButton("Буря Людена")
		markup3.add(item1, item2)
		bot.send_message(message.chat.id, 'Предметы', parse_mode='html', reply_markup=markup3)
	elif message.text == 'Люкс':
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item4 = types.KeyboardButton('Персонаж')
		item5 = types.KeyboardButton('Предметы')
		markup.add(item4, item5)
		bot.send_message(message.chat.id, 'Выберите какая категория вас интересует', parse_mode='html',
						 reply_markup=markup)

		bot.send_photo(message.chat.id, lux)
		bot.send_message(message.chat.id, luxt)
		bot.send_message(message.chat.id, parse_mode='html', reply_markup=markup)
	#Сервер
	elif message.text=="Наш сервер":
		bot.send_message(message.chat.id,"https://discord.gg/jtESKcQt/")

		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item4 = types.KeyboardButton('Персонаж')
		item5 = types.KeyboardButton('Предметы')
		markup.add(item4, item5)
		bot.send_message(message.chat.id, 'Выберите какая категория вас интересует', parse_mode='html',
						 reply_markup=markup)
	#Буря Людена
	elif message.text == "Буря Людена":
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, stuff)

		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item4 = types.KeyboardButton('Персонаж')
		item5 = types.KeyboardButton('Предметы')
		markup.add(item4, item5)
		bot.send_message(message.chat.id, 'Выберите какая категория вас интересует', parse_mode='html',
						 reply_markup=markup)
	#Страдания Лиандры
	elif message.text == "Страдания Лиандри":
		bot.send_photo(message.chat.id, photo1)
		bot.send_message(message.chat.id, stuff1)

		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		item4 = types.KeyboardButton('Персонаж')
		item5 = types.KeyboardButton('Предметы')
		markup.add(item4, item5)
		bot.send_message(message.chat.id, 'Выберите какая категория вас интересует', parse_mode='html',
						 reply_markup=markup)
	#Ошибка
	else:
		bot.send_message(message.chat.id, 'Выберите из предложенного списка')
bot.infinity_polling(none_stop=True, interval=0)