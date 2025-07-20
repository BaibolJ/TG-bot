import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ВСТАВЬ СЮДА СВОЙ ТОКЕН
BOT_TOKEN = '7836683973:AAHJ8pc5K-07uq_uTNqcjK__6jSxu6_ycgc'


# Стартовое сообщение
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['📦 Заказать', 'ℹ️ О нас'], ['🕑 График', '💬 Контакты']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Добро пожаловать! Что вас интересует?", reply_markup=reply_markup)


# Обработка сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == '📦 Заказать':
        await update.message.reply_text("Введите ваш заказ в формате: \nИмя - Телефон - Что хотите заказать")
    elif text == 'ℹ️ О нас':
        await update.message.reply_text("Мы — локальный бизнес. Принимаем заказы 24/7.")
    elif text == '🕑 График':
        await update.message.reply_text("Работаем с 9:00 до 21:00 ежедневно.")
    elif text == '💬 Контакты':
        await update.message.reply_text("📞 +996 555 12 34 56\n📍 Бишкек, ул. Примерная 12")
    else:
        await update.message.reply_text("Спасибо! Ваш заказ получен. Мы скоро свяжемся с вами.")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    from keep_alive import keep_alive

    keep_alive()
    app.run_polling()
