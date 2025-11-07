import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

class TelegramBot:
    def __init__(self, token: str, group_chat_id: int):
        self.token = token
        self.group_chat_id = group_chat_id
        self.application = ApplicationBuilder().token(self.token).build()

        
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text("Привет! Я бот.")

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await context.bot.copy_message(
            chat_id=self.group_chat_id,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )

        

    def run(self) -> None:
        self.application.run_polling()

if __name__ == '__main__':
    TOKEN = '8121514569:AAFJR5MNhVLk1ac0kuxu7m7X4CBzo88dMfE'
    GROUP_CHAT_ID = -5007465480
    bot = TelegramBot(TOKEN, GROUP_CHAT_ID)
    bot.run()


