import telebot
import random

token = '1904692819:AAFbM2Cf89Znr3olOuJtVQVnYJNrxqiJvew'

bot = telebot.TeleBot(token)

RANDOM_TASKS = ["Пойти пожрать!", "Пойти посрать!", "Пойти гулять!", "Пойти поспать!"]

HELP = """
/help - вывести список доступных команд
/add - добавить задачу в список
/show - напечатать все добавленные задачи
/random - добавить случайную задачу на сегодня
/calc - запускает калькулятор"""

tasks = {}

def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date]. append(task)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет."
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
