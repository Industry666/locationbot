from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from tools.api_tools.api_tools import MyMessageHandler as MMS
from tools.appandDB_config import MY_BOT_TOKEN


MY_TOKEN = MY_BOT_TOKEN

updater = Updater(token=MY_TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', MMS.start_handler))
updater.dispatcher.add_handler(CommandHandler('add', MMS.add))
updater.dispatcher.add_handler(CommandHandler('list', MMS.my_list))
updater.dispatcher.add_handler(CommandHandler('reset', MMS.reset))
updater.dispatcher.add_handler(MessageHandler(Filters.text, MMS.get_location_name, pass_user_data=True))


updater.start_polling()
