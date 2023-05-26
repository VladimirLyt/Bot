import telebot
from telebot import types
token = '6019618022:AAHpQmczWOJXOKaVpyO5ec6jFRh9S_lHOAI'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет, я бот созданный для объяснения предметов в игре Лига Легенд')
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Страдания Лиандри")
	item2 = types.KeyboardButton("Буря Людена")
	item3 = types.KeyboardButton("Наш сервер")
	markup.add(item1, item2, item3)
	bot.send_message(message.chat.id, 'Выберите какой предмет вас интересует', parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def message_reply(message):
	# Буря Людена инф
	with open('1.txt', 'r', encoding='utf-8') as f:
		stuff= f.read()
	photo = open('буря людена.webp', 'rb')
	# Страдания Лиандры инф
	with open('2.txt', 'r', encoding='utf-8') as f:
		stuff1 = f.read()
	photo1 = open('Страдания Лиандри.webp', 'rb')
	#Сервер
	if message.text=="Наш сервер":
		bot.send_message(message.chat.id,"https://discord.gg/jtESKcQt/")
	#Буря Людена
	elif message.text == "Буря Людена":
		bot.send_photo(message.chat.id, photo)
		bot.send_message(message.chat.id, stuff)
	#Страдания Лиандры
	elif message.text == "Страдания Лиандри":
		bot.send_photo(message.chat.id, photo1)
		bot.send_message(message.chat.id, stuff1)
	#Ошибка
	else:
		bot.send_message(message.chat.id, 'Выберите из предложенного списка')
bot.polling(none_stop=True, interval=0)