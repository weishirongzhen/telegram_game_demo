import logging

import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_game(chat_id=update.effective_chat.id, game_short_name='your_hame_name')


async def play_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    game_url = "your_game_url"
    await context.bot.answer_callback_query(callback_query_id=update.callback_query.id, url=game_url)


if __name__ == '__main__':
    application = ApplicationBuilder().token('your_bot_token').build()

    start_handler = CommandHandler('info', info)
    send_game_handler = CommandHandler('start', start)

    play_game_handler = CallbackQueryHandler(play_game)

    application.add_handler(start_handler)
    application.add_handler(send_game_handler)

    application.add_handler(play_game_handler)




    application.run_polling()
