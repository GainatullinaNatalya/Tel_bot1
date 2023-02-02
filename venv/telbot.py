from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_you(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/time\n/help')

async def now_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def summ(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')


app = ApplicationBuilder().token("5666399861:AAEvMM48IkKI6Bi0V3RzyuwnwuCbgw9QRvE").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", now_time))
app.add_handler(CommandHandler("help", help_you))
app.add_handler(CommandHandler("sum", summ))

app.run_polling()