from telegram import *
from telegram.ext import *
import logging
from datetime import datetime
import nmap


bot = Bot("1620033467:AAEyovsyVS8IMYt57RxznNf1sfr-H9Uxf5I")

#print(bot.get_me())
updater =Updater("1620033467:AAEyovsyVS8IMYt57RxznNf1sfr-H9Uxf5I",use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
#------------------------chat
def reponse_time(input_text):
	user_message = str(input_text).lower()

	if user_message in ("hello", "hi", "sup", "chào", "hey"):
		return "Hey! welcome back my master!"
	if user_message in ("khoẻ không", "ổn không"):
		return "tôi rất ổn , còn ngài thì sao , master!"
	if user_message in ("time", "time?", " mấy giờ rồi"):
		now =  datetime.now()
		date_time = now.strftime("%d/%m/%y, %H:%M:%S")

		return str(date_time)
	return " tôi không hiểu bạn đang nói gì master!"	




def handle_message(update, context):
	text = str(update.message.text).lower()
	respone = reponse_time(text)

	update.message.reply_text(respone)
def error_pass(update:Update,context=CallbackContext):
	print(f"update {update} cause error {context.error}")



def test_function(update:Update,context=CallbackContext):
	bot.send_message(

		chat_id=update.effective_chat.id,
		text="tôi là bot và tôi đang hoạt động",

		)
start_value=CommandHandler('helo',test_function)
dispatcher.add_handler(start_value)
def secret_show(update:Update,context=CallbackContext):
	bot.send_message(
		chat_id=update.effective_chat.id,
		text="mật khẩu là ****",
		)
start_value=CommandHandler('secret',secret_show)
dispatcher.add_handler(start_value)
def start_conmmand(update:Update,context=CallbackContext):
	update.message.reply_text('Type someting random to get start!')
start_value=CommandHandler('startt',start_conmmand)
dispatcher.add_handler(start_value)
def help_command(update:Update, context=CallbackContext):
	update.message.reply_text('If you need help! you should go to hospital!')
start_value=CommandHandler('help',help_command)
dispatcher.add_handler(start_value)


#----------------scan port ----------------
def port():
	pass
#def scan_port(update:Update,context=CallbackContext):
	

def showkeyboard(update:Update,context=CallbackContext):
	keyboard = [[

		InlineKeyboardButton('About Author',callback_data='ABOUT'),
		InlineKeyboardButton('Scan',callback_data='Scan'),
		InlineKeyboardButton('Click me',callback_data='click'),

	]]
	reply_markup = InlineKeyboardMarkup(keyboard)
	update.message.reply_text('Please Choose:',reply_markup=reply_markup)
	dispatcher.add_handler(start_value)
#dispatcher.add_handler(MessageHandler(Filters.text,showkeyboard))


def button(update:Update,context=CallbackContext):
	query = update.callback_query

	choice = query.data
	if choice =='ABOUT':

		bot.send_message(

		chat_id=update.effective_chat.id,
		text="hey , would u like to join in funny group? click the link : XXX.XXX",
		{
			keyboard = [[

					InlineKeyboardButton('Scan',callback_data='Scan'),
					InlineKeyboardButton('Click me',callback_data='click'),

				]]
			reply_markup = InlineKeyboardMarkup(keyboard)
			update.message.reply_text('Please nề:',reply_markup=reply_markup)
		}

		)
		
		# keyboard = [[

		# InlineKeyboardButton('Scan',callback_data='Scan'),
		# InlineKeyboardButton('Click me',callback_data='click'),

		# 	]]
		# reply_markup = InlineKeyboardMarkup(keyboard)
		# update.message.reply_text('Please Choose 1 or 2:',reply_markup=reply_markup)
		# #dispatcher.add_handler(start_value)
		# dispatcher.add_handler(MessageHandler(Filters.text,showkeyboard) )
		# return aboutme
	if choice=='Scan':
		bot.send_message(

		chat_id=update.effective_chat.id,
		text="scan cl ,tự mà làm mày",

		)
	if choice == 'click':
		bot.send_message(
		chat_id=update.effective_chat.id,
		text="you are hacked, ngồi đó đợi đi bro, tôi có địa chỉ nhà bạn rồi!",
		)

updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, bot))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

def aboutme(update:Update,context=CallbackContext):
	keyboard = [[

		InlineKeyboardButton('Scan',callback_data='Scan'),
		InlineKeyboardButton('Click me',callback_data='click'),

	]]
	reply_markup = InlineKeyboardMarkup(keyboard)
	update.message.reply_text('Please Choose 1 or 2:',reply_markup=reply_markup)
dispatcher.add_handler(start_value)
dispatcher.add_handler(MessageHandler(Filters.text,showkeyboard) )
#dispatcher.add_handler(MessageHandler(Filters.text,handle_message))
start_value=CommandHandler('aboutme',aboutme)
def Scanweb(update:Update,context=CallbackContext):
	
	query = update.callback_query
	query.answer()
	keyboard  = [
		[
			InlineKeyboardButton('About Author',callback_data='ABOUT'),
			InlineKeyboardButton('Click me',callback_data='click'),
		]
	]
	reply_markup=InlineKeyboardMarkup(keyboard)
	query.edit_message_text(
        text="Quet cl ne", reply_markup=reply_markup
    )
start_value=CommandHandler('scanw',Scanweb)

#------------------------Command---------------------------------

updater.start_polling()
updater.idle()