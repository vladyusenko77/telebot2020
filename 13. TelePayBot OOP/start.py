from lib.db_manager import db_manager
from lib.settings import *
import telebot
#import config
from datetime import datetime

__URL = "https://api.covid19api.com/summary"
db_object = db_manager(host, user, passwd, database, __URL)
covid_19_data = db_object.get_all_data()
bot = telebot.TeleBot(token)
#db_object.save_all_data(covid_19_data)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,"-Актуальна інформація про поширення👋Kоронавірусної інфекції 🤧 [𝐂𝐎𝐕𝐈𝐃-19] ☠️\n-ведіть назву країни 🌏 щоб побачити статистику🚫\n-приклад 🔴Ukraine🔴 Або скорочено uk,ukr,ukra,ukrai...✈️")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    countr = message.text
    coron = db_object.show_country(countr)
    if message.text == countr:
        for item in coron:
            bot.send_message(message.from_user.id, "_______🌏 [𝐂𝐎𝐕𝐈𝐃-19] 🌏_______"+"\n✈️ Країна ✈️ → " + str(item[1]) +
                             "\n🤧 Кількість захворювань 🤧 → " + str(item[4]) + "\n🤧 Кількість захворювань за добу 🤧 → " + str(item[5]) + "\n☠️ Кількість смертей ☠️ → " + str(item[6]) + "\n☠️ Кількість смертей за добу ☠️ → " + str(item[5]) + "\n💊 Кількість вилікуваних 💊 → " + str(item[8]) + "\n💊 Кількість вилікуваних за добу 💊 → " + str(item[7]))

if __name__ == "__main__":
    print("[" + str(datetime.now()) + "] Running...")
    bot.infinity_polling(True)

