import API as key
from telegram import ext
import responses as R 

def start_command(update, context):
    update.message.reply_text("Type something to get started")

def help_command(update, context):
    update.message.reply_text("If you need help! You should ask for it on Google")

def handle_message(update, context):
    text = str(update.message.text).lower()
    print(text)
    response = R.responses(text)
    # print('fhif')
    update.message.reply_text(response)


def main():
    updater = ext.Updater(key.API_Key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(ext.CommandHandler("start", start_command))
    dp.add_handler(ext.CommandHandler("help", help_command))
    print(ext.Filters.text)
    dp.add_handler(ext.MessageHandler(ext.Filters.text, handle_message))

    updater.start_polling(0)
    updater.idle()


main()