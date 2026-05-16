import telebot
import requests
from telebot import apihelper

TOKEN = "8662198598:AAGmAytKdaYG_aTZtm0OMtfDeSY0WEfO4w0"

# HTTP прокси
apihelper.proxy = {
    'https': 'http://87.120.222.214:444'
}

bot = telebot.TeleBot(TOKEN)

lab_tips = {
    "физика": "Для лабораторной по физике: проверь правильность сборки цепи, убедись в надежности контактов.",
    "химия": "Для лабораторной по химии: строго соблюдай пропорции реагентов и технику безопасности.",
    "биология": "Для лабораторной по биологии: внимательно фиксируй наблюдения, делай зарисовки."
}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = ("Привет! Я помощник по лабораторным работам проекта 'Виртуальная лаборатория'.\n\n"
            "Команды:\n"
            "/start - приветствие\n"
            "/labs - список лабораторных работ\n"
            "/tip [тема] - совет по теме (физика, химия, биология)\n"
            "Или просто напиши название работы.")
    bot.reply_to(message, text)

@bot.message_handler(commands=['labs'])
def list_labs(message):
    text = ("Лабораторные работы:\n"
            "1. Сборка электрической цепи (физика)\n"
            "2. Скорость химической реакции (химия)\n"
            "3. Строение клетки (биология)")
    bot.reply_to(message, text)

@bot.message_handler(commands=['tip'])
def give_tip(message):
    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        bot.reply_to(message, "Напиши тему: /tip физика")
        return
    topic = args[1].lower()
    if topic in lab_tips:
        bot.reply_to(message, lab_tips[topic])
    else:
        bot.reply_to(message, "Темы: физика, химия, биология")

@bot.message_handler(func=lambda msg: True)
def handle_lab(message):
    text = message.text.lower()
    if "цепь" in text:
        response = ("Сборка цепи:\n1. Нарисуй схему\n2. Собирай от источника\n3. Проверь контакты")
    elif "реакц" in text or "скорость" in text:
        response = ("Химическая реакция:\n1. Запиши температуру\n2. Добавляй реактив по каплям\n3. Фиксируй изменения")
    elif "клетк" in text or "микроскоп" in text:
        response = ("Микроскоп:\n1. Начни с малого увеличения\n2. Сфокусируй\n3. Зарисуй увиденное")
    else:
        response = ("Напиши: цепь, реакция или клетка. Или используй /tip")
    bot.reply_to(message, response)

print("Бот запущен...")
bot.infinity_polling()