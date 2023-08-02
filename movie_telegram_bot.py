from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler,filters,ContextTypes
import requests
from bs4 import BeautifulSoup
import re
import random

def hor_pick():

	ac = []
	URL = "https://www.imdb.com/search/title/?title_type=feature&genres=horror&explore=genres"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, "html.parser")
	#print(soup)
	m = soup.find_all("h3", class_="lister-item-header")
	for i in m:
		res = i.find_all("a", href=True)
		#print(res)
		res1 = re.findall('[A-Za-z]+',str(res))
		#print(res1)
		res2 = res1[4:len(res1)-1]
		#print(res1[4:len(res1)-1])
		if len(res2)>1:
			name = ""
			for i in range(len(res2)):
				name= name + res2[i]+ " "
			ac.append(str(name))
		if len(res2) == 0:
			pass
		else:
			ac.append(str(res2[0]))
	ac2 = []
	for i in range(0,len(ac),2):
		ac2.append(str(ac[i]))
	#print(ac2)
	return(ac2[random.randint(0,len(ac2))])



def rom_pick():
	rom = []
	URL = "https://www.imdb.com/search/title/?title_type=feature&genres=romance"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, "html.parser")
	#print(soup)
	m = soup.find_all("h3", class_="lister-item-header")
	for i in m:
		res = i.find_all("a", href=True)
		
		res1 = re.findall('[A-Za-z]+',str(res))
		res2 = res1[4:len(res1)-1]
		#print(res1[4:len(res1)-1])
		if len(res2)>1:
			name = ""
			for i in range(len(res2)):
				name= name + res2[i]+ " "
			rom.append(str(name))
		else:
			rom.append(str(res2[0]))
	
	return(rom[random.randint(0,len(rom))])
def ac_pick():
	ac = []
	URL = "https://www.imdb.com/search/title/?title_type=feature&genres=action&explore=genres"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, "html.parser")
	#print(soup)
	m = soup.find_all("h3", class_="lister-item-header")
	for i in m:
		res = i.find_all("a", href=True)
		#print(res)
		res1 = re.findall('[A-Za-z]+',str(res))
		#print(res1)
		res2 = res1[4:len(res1)-1]
		#print(res1[4:len(res1)-1])
		if len(res2)>1:
			name = ""
			for i in range(len(res2)):
				name= name + res2[i]+ " "
			ac.append(str(name))
		if len(res2) == 0:
			pass
		else:
			ac.append(str(res2[0]))
	ac2 = []
	for i in range(0,len(ac),2):
		ac2.append(str(ac[i]))
	#print(ac2)
	return(ac2[random.randint(0,len(ac2))])
		
TOKEN: Final = '5979861792:AAGu68FEIhQRoupqz5HuWyxgBSZXQpmH-SM'
BOT_USERNAME:Final = '@Picky999_bot'

async def start_command(update:Update, context : ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('Hello thanks for trusting me with your movie night choice !')
	
async def help_command(update:Update, context : ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('please type the genre so I can help you choose !')
	
async def choose_command(update:Update, context : ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('gneres supported : horror / actions / romantic')
	
def Handle_response(text: str)-> str:
	
	if "romantic" in text :
		return rom_pick()
	elif "action" in text :
		return ac_pick()
	elif "science fiction" in text : 
		return "interstellar"
	elif "horror" in text :
		return hor_pick()
	else:
		return "Didn't understand :("
		
		
async def handle_message(update:Update, context : ContextTypes.DEFAULT_TYPE):
	message_type = update.message.chat.type
	text = update.message.text
	response = Handle_response(text)
	print("bot :" , response)
	await update.message.reply_text(response)
def main():
	
	
	print("starting ...")
	app = Application.builder().token(TOKEN).build()
	app.add_handler(CommandHandler('start',start_command))
	app.add_handler(CommandHandler('help',help_command))
	app.add_handler(CommandHandler('custom',choose_command))
	
	app.add_handler(MessageHandler(filters.TEXT, handle_message))
	print("checking ..")
	app.run_polling(poll_interval=1)
main()
