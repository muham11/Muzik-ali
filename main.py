from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Assalomu alaykum!\n\n"
        "Muzik Ali Botga xush kelibsiz!"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
