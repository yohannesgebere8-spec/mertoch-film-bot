import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

WELCOME = """
🎬 ሰላም! ወደ Mertoch Film Bot እንኳን በደህና መጡ!

ከታች ያሉትን ምርጫዎች ይጠቀሙ 👇
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🎬 ፊልሞች", callback_data="movies"),
            InlineKeyboardButton("🔎 ፊልም ፈልግ", callback_data="search"),
        ],
        [
            InlineKeyboardButton("🆕 አዳዲስ ፊልሞች", callback_data="new"),
            InlineKeyboardButton("⭐ ተወዳጅ", callback_data="popular"),
        ],
        [
            InlineKeyboardButton("📂 ምድቦች", callback_data="categories"),
            InlineKeyboardButton("ℹ️ ስለ Bot", callback_data="about"),
        ],
    ]

    await update.message.reply_text(
        WELCOME,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "movies":
        text = "🎬 የሚገኙ ፊልሞች\n\nአሁን ፊልሞች እየተዘጋጁ ነው።"

    elif query.data == "search":
        text = "🔎 ፊልም ለመፈለግ የፊልሙን ስም በMessage ላክ።"

    elif query.data == "new":
        text = "🆕 አዳዲስ ፊልሞች\n\nበቅርቡ ይጨመራሉ።"

    elif query.data == "popular":
        text = "⭐ ተወዳጅ ፊልሞች\n\nበቅርቡ ይጨመራሉ።"

    elif query.data == "categories":
        text = "📂 የፊልም ምድቦች\n\n🎭 Drama\n😂 Comedy\n💥 Action\n❤️ Romance"

    elif query.data == "about":
        text = "ℹ️ Mertoch Film Bot\n\nየፊልም መፈለጊያና መዳረሻ Bot።"

    else:
        text = "❌ ያልታወቀ ምርጫ።"

    keyboard = [
        [InlineKeyboardButton("🔙 ወደ ዋና ገጽ", callback_data="home")]
    ]

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def home(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton("🎬 ፊልሞች", callback_data="movies"),
            InlineKeyboardButton("🔎 ፊልም ፈልግ", callback_data="search"),
        ],
        [
            InlineKeyboardButton("🆕 አዳዲስ ፊልሞች", callback_data="new"),
            InlineKeyboardButton("⭐ ተወዳጅ", callback_data="popular"),
        ],
        [
            InlineKeyboardButton("📂 ምድቦች", callback_data="categories"),
            InlineKeyboardButton("ℹ️ ስለ Bot", callback_data="about"),
        ],
    ]

    await query.edit_message_text(
        WELCOME,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is not set")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(home, pattern="^home$"))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Mertoch Film Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
