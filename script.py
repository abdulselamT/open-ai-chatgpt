from constants import API_KEY
import telebot
from telebot import types
import openai
bot = telebot.TeleBot(API_KEY,parse_mode=None)
def answer_from_gpt(ask):
	openai.api_key = ""
	response = openai.Completion.create(
	  		model="text-davinci-003",
	  		prompt=ask,
	  		temperature=0.9,
	  		max_tokens=150,
	  		top_p=1,
	  		frequency_penalty=0,
	  		presence_penalty=0.6,
	  		stop=[" Human:", " AI:"]
			)
	text = response['choices'][0]['text']
	return text




@bot.message_handler(commands=['start'])
def send_welcome(msg):
	bot.send_message(chat_id=msg.chat.id,text="please write me a question ?")





@bot.message_handler(func=lambda message : True)
def send_welcome(msg):
	print(msg.chat.id)
	answer=answer_from_gpt(msg.text)
	bot.send_message(chat_id=msg.chat.id,text=answer)







bot.infinity_polling()
