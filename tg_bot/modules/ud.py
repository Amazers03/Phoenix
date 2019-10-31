from telegram import Update, Bot, ParseMode
from telegram.ext import run_async

from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot import dispatcher

from requests import get

@run_async
def ud(bot: Bot, update: Update):
  message = update.effective_message
  text = message.text[len('/ud '):]
  results = get(f'http://api.urbandictionary.com/v0/define?term={text}').json()
  reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
  message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)

__help__ = """
 - /ud <expression> :- Returns the top definition of the word or expression on Urban Dictionary.
"""

__mod_name__ = "Urban Dictionary"
  
ud_handle = DisableAbleCommandHandler("ud", ud)

dispatcher.add_handler(ud_handle)
