import telebot
from telebot.types import Message
from tok import * 


token = token

bot=telebot.TeleBot(token)

current_question = {}

questions = [
  
    "Сколько тебе лет?",
    "Какая у тебя профессия?",
    "Какой годовой доход у тебя?",
    "Какая у тебя заработная плата в месяц на руки?",
    "Сколько у тебя банковских счетов?",
    "Сколько у тебя кредитных карт?",
    "Сколько у тебя займов?",
    "Сколько запросов по кредитной истории ты делал?",
    "Как долго у тебя кредитная история?",
    "Сколько ты инвестируешь ежемесячно?",
    "Каков твой опыт в платежах по кредитам?",
    "Каков ежемесячный баланс?"

]

@bot.message_handler(commands=['start'])
def start_message(message: Message):

    current_question[message.chat.id] = 0
    bot.send_message(message.chat.id, "Привет, хочешь взять кредит? Ответь на несколько вопросов.")
    handle_survey(message)

def handle_survey(message: Message):
    chat_id = message.chat.id

    if current_question[chat_id] < len(questions):
        current_question_text = questions[current_question[chat_id]]
        bot.send_message(chat_id, current_question_text)
        current_question[chat_id] += 1  # Increment the question index
    else:
        bot.send_message(chat_id, "Спасибо за ответы! Мы рассмотрим ваш запрос.")

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message: Message):
    text = message.text
    # Split the text into separate parts using the '=' character as a delimiter
    parts = text.split('=')

    # Create a dictionary to map the column names to their corresponding values
    values = {
        "age": parts[0],
        "occupation": parts[1],
        "annual_income": parts[2],
        "monthly_inhand_salary": parts[3],
        "num_bank_accounts": parts[4],
        "num_credit_card": parts[5],
        "num_of_loan": parts[6],
        "num_credit_inquiries": parts[7],
        "credit_history_age": parts[8],
        "amount_invested_monthly": parts[9],
        "payment_behaviour": parts[10],
        "monthly_balance": parts[11]
    }

    print(values)


bot.polling() 

# возраст, годой доход = месячный доход * 12, месячный доход, кол-во кредитных карт, точно такое же кол-во,
# колличество займов, количество запросов на кредит, кредитная история стаж, сумма ежемесячных инвестиций
# ежемесячный баланс

# check_data_set = {

#     'age' : False,
#     'annual_income' : False,
#     'monthly_inhand_salary' : False ,
#     'num_bank_accounts' : False,
#     'num_credit_card' : False,
#     'num_of_loan' : False,
#     'num_credit_inquiries' : False,
#     'credit_history_age' : False,
#     'amount_invested_monthly' : False,
#     'monthly_balance' : False

# }