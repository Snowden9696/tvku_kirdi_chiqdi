from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "7914331254:AAHVS5y5v1zMUnFZ3pj5-mJEc-qQrEkFTn8"

async def delete_join_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.delete_message(
            chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )
    except Exception as e:
        print(f"❌ Xatolik: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, delete_join_message))

print("🤖 Bot ishga tushdi va yangi a'zolar xabarlari o'chirilmoqda...")
app.run_polling()
