import telebot

# Создаем объект бота
bot = telebot.TeleBot('6305832366:AAE7bDANfSymlLY9R5Wb8ypbQMH3pHP3QRs')

bot.send_message(1199404728, "Отправляю прокси")

file_path = 'test.txt'

bot.send_document(1199404728, open(file_path, 'rb'))
