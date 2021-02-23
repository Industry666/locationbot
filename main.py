from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from tools.api_tools.api_tools import MyMessageHandler as MMS
from tools.appandDB_config import MY_BOT_TOKEN
import os
from main_app_config import app_url


MY_TOKEN = MY_BOT_TOKEN
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(token=MY_TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', MMS.start_handler))
updater.dispatcher.add_handler(CommandHandler('add', MMS.add))
updater.dispatcher.add_handler(CommandHandler('list', MMS.my_list))
updater.dispatcher.add_handler(CommandHandler('reset', MMS.reset))
updater.dispatcher.add_handler(MessageHandler(Filters.text, MMS.get_location_name, pass_user_data=True))

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=MY_TOKEN)
updater.bot.set_webhook(app_url + MY_TOKEN)

updater.start_polling()
