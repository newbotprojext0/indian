from telegram import TelegramError, Chat, Message
from telegram import Update, Bot
from telegram.error import BadRequest
from telegram.ext import MessageHandler, Filters, CommandHandler
from telegram.ext.dispatcher import run_async
from typing import List
from haruka.modules.helper_funcs.filters import CustomFilters

import telegram
from haruka import dispatcher, SUDO_USERS

@run_async
def leave(bot: Bot, update: Update, args: List[str]):
    if args:
        chat_id = str(args[0])
        del args[0]
        try:
            bot.leave_chat(int(chat_id))
            update.effective_message.reply_text("Done. ")
        except telegram.TelegramError:
            update.effective_message.reply_text("Couldnt leave group.")
    else:
        update.effective_message.reply_text("Send a valid chat id") 

__help__ = ""

__mod_name__ = "Leave"

LEAVE_HANDLER = CommandHandler("leave", leave, pass_args = True, filters=Filters.user(SUDO_USERS))
dispatcher.add_handler(LEAVE_HANDLER)
