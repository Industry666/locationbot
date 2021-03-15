from tools.api_tools.database.db import ConnDB


class MyMessageHandler:

    @staticmethod
    def start_handler(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Привет! В этом боте ты можешь добавлять места которые ты хочешь посетить.\n"
                                      "Введи команду /add для добавления места.\n"
                                      "Введи команду /list для вывода сохраненных мест.\n"
                                      "Введи команду /reset для удаления сохраненных мест.\n")

    @staticmethod
    def add(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Введи название локации которую хочешь посетить:")

    @staticmethod
    def get_location_name(update, context):
        user = update.effective_user
        value = update.message.text
        conn = ConnDB.get_connect()
        ConnDB.add_message(conn, user.id, update.message.text)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Локация '{value}' сохранена.")

    @staticmethod
    def my_list(update, context):
        user = update.effective_user
        conn = ConnDB.get_connect()
        result = ConnDB.get_list_location(conn, user.id)
        empty_list = []
        result_list = []
        for i in result:
            result_list += i
        if result_list == empty_list:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Ты еще не добавил ни одного места.")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Список твоих мест:")
            for x in range(len(result_list)):
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"{result_list[x]}")

    @staticmethod
    def reset(update, context):
        user = update.effective_user
        conn = ConnDB.get_connect()
        ConnDB.remove_all_locations(conn, user.id)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Список твоих мест удален.")
