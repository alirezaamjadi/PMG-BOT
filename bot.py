import json
import os
import random
from datetime import datetime
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    ConversationHandler,
    CallbackQueryHandler
)
from config import TOKEN, ADMIN_USERNAME

DATA_FILE = "data.json"
(TEAM1, TEAM2, AMOUNT, USERS, SUBJECT, CONFIRM_BET, ADD_USER) = range(7)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"bets": [], "accounts": {}}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    data.setdefault("bets", [])
    data.setdefault("accounts", {})
    return data

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def build_main_keyboard():
    kb = [["1️⃣ شرط جدید"], ["2️⃣ شرط‌های جاری"], ["3️⃣ حساب"], ["4️⃣ درباره بات"]]
    return ReplyKeyboardMarkup(kb, resize_keyboard=True)

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏷️ به ربات خوش آمدی! یکی از گزینه‌ها رو انتخاب کن:", reply_markup=build_main_keyboard())

async def main_menu(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text
    if txt in ["لغو", "/cancel"]:
        return await start(update, ctx)

    if txt.startswith("1"):
        await update.message.reply_text("📌 نام تیم اول را وارد کنید:", reply_markup=ReplyKeyboardMarkup([["لغو"]], resize_keyboard=True))
        return TEAM1

    elif txt.startswith("2"):
        data = load_data()
        ongoing = [b for b in data.get("bets", []) if b.get("status") == "ongoing"]
        if not ongoing:
            await update.message.reply_text("🔍 شرط فعالی وجود ندارد.", reply_markup=build_main_keyboard())
            return ConversationHandler.END

        text = "📋 شرط‌های جاری:\n\n"
        buttons = []
        for b in ongoing:
            try:
                bid = b["bet_id"]
                created_at = b.get("created_at", "نامشخص")
                team1 = b.get("team1", "نامشخص")
                team2 = b.get("team2", "نامشخص")
                amount = b.get("amount", "؟")
                users = b.get("users", "؟")
                subject = b.get("subject", "؟")

                text += (
                    f"┌──── شرط #{bid} ────┐\n"
                    f"📅 تاریخ: {created_at}\n"
                    f"🆚 مسابقه: {team1} VS {team2}\n"
                    f"💰 مبلغ: {amount} تومان\n"
                    f"👥 افراد: {users}\n"
                    f"📝 موضوع: {subject}\n"
                    f"└────────────────────┘\n\n"
                )
                buttons.append([InlineKeyboardButton(f"❌ حذف شرط #{bid}", callback_data=f"delete_{bid}")])
            except KeyError:
                continue

        await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(buttons))
        return ConversationHandler.END

    elif txt.startswith("3"):
        data = load_data()
        accs = data["accounts"]
        if accs:
            text = "\n".join([f"👤 {n}: {v} امتیاز" for n, v in accs.items()])
        else:
            text = "👥 هیچ حسابی ثبت نشده."
        await update.message.reply_text(text, reply_markup=build_main_keyboard())
        await update.message.reply_text("➕ برای افزودن امتیاز:\nافزودن [اسم] [مقدار]\nیا «لغو» برای منو", reply_markup=ReplyKeyboardMarkup([["لغو"]], resize_keyboard=True))
        return ADD_USER

    elif txt.startswith("4"):
        await update.message.reply_text("🤖 ساخته‌شده توسط علیرضا امجدی – ۱۴۰۴ / ۲۰۲۵\nبرای مدیریت شرط‌های دوستانه", reply_markup=build_main_keyboard())
        return ConversationHandler.END

    else:
        await update.message.reply_text("لطفاً یکی از گزینه‌های منو رو انتخاب کن.", reply_markup=build_main_keyboard())
        return ConversationHandler.END

async def get_team1(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["team1"] = update.message.text
    await update.message.reply_text("📌 نام تیم دوم رو وارد کن:", reply_markup=ReplyKeyboardMarkup([["لغو"]], resize_keyboard=True))
    return TEAM2

async def get_team2(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["team2"] = update.message.text
    await update.message.reply_text("💰 مبلغ شرط (تومان):", reply_markup=ReplyKeyboardMarkup([["لغو"]], resize_keyboard=True))
    return AMOUNT

async def get_amount(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text
    if not txt.isdigit():
        await update.message.reply_text("❗ مبلغ باید عدد باشه. دوباره بنویس:", reply_markup=ReplyKeyboardMarkup([["لغو"]], resize_keyboard=True))
        return AMOUNT
    ctx.user_data["amount"] = txt
    await update.message.reply_text("👥 بین چه کسانی بسته می‌شود؟ مثال: @ali @reza", reply_markup=ReplyKeyboardMarkup([["لغو"]], resize_keyboard=True))
    return USERS

async def get_users(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["users"] = update.message.text
    await update.message.reply_text("✏️ موضوع شرط رو بنویس:", reply_markup=ReplyKeyboardMarkup([["لغو"]], resize_keyboard=True))
    return SUBJECT

async def get_subject(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data["subject"] = update.message.text
    now = datetime.now().strftime("%H:%M – %d/%m/%Y")
    bid = random.randint(10000, 99999)
    ctx.user_data["bet_id"], ctx.user_data["created_at"] = bid, now

    msg = (f"┌{'─'*36}┐\n"
           f"│ 💰 مبلغ: {ctx.user_data['amount']} تومان\n"
           f"│ 🔢 کد: {bid}   📅 {now}\n"
           f"│ 🆚 {ctx.user_data['team1']} VS {ctx.user_data['team2']}\n"
           f"│ 👥 بین: {ctx.user_data['users']}\n"
           f"│ 📝 موضوع: {ctx.user_data['subject']}\n"
           f"└{'─'*36}┘")
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ تایید", callback_data="confirm_bet")],
        [InlineKeyboardButton("❌ لغو", callback_data="cancel_bet")]
    ])
    await update.message.reply_text(msg, reply_markup=kb)
    return CONFIRM_BET

async def confirm_bet(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    b = ctx.user_data
    data = load_data()
    data["bets"].append({**b, "status": "ongoing"})
    save_data(data)
    await q.edit_message_text("✅ شرط ثبت شد و در لیست جاری قرار گرفت.")
    ctx.user_data.clear()
    return ConversationHandler.END

async def cancel_bet(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    await q.edit_message_text("❌ ثبت شرط لغو شد.")
    ctx.user_data.clear()
    return ConversationHandler.END

async def delete_bet(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    bid = q.data.split("_")[1]
    data = load_data()
    before = len(data["bets"])
    data["bets"] = [b for b in data["bets"] if str(b.get("bet_id", "")) != bid]
    save_data(data)
    if before == len(data["bets"]):
        await q.edit_message_text("⚠️ شرط یافت نشد یا قبلاً حذف شده.")
    else:
        await q.edit_message_text(f"✅ شرط #{bid} با موفقیت حذف شد.")
    return ConversationHandler.END

async def add_user_score(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    txt = update.message.text
    if txt in ["لغو", "/cancel"]:
        ctx.user_data.clear()
        await update.message.reply_text("❌ عملیات لغو شد.", reply_markup=build_main_keyboard())
        return ConversationHandler.END  # ✅ این خط رو اضافه کردیم

    parts = txt.split()
    if len(parts) == 3 and parts[0] == "افزودن" and parts[2].isdigit():
        data = load_data()
        name = parts[1]
        amount = int(parts[2])
        data["accounts"][name] = data["accounts"].get(name, 0) + amount
        save_data(data)
        await update.message.reply_text(f"✅ به {name} عدد {amount} اضافه شد.", reply_markup=build_main_keyboard())
        return ConversationHandler.END

    await update.message.reply_text("❗ فرمت نادرست. مثال:\nافزودن علی 50\nیا «لغو» برای منو", reply_markup=ReplyKeyboardMarkup([["لغو"]], resize_keyboard=True))
    return ADD_USER


async def cancel(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ctx.user_data.clear()
    return await start(update, ctx)

# 📡 راه‌اندازی ربات
app = ApplicationBuilder().token(TOKEN).build()

conv = ConversationHandler(
    entry_points=[MessageHandler(filters.TEXT & ~filters.COMMAND, main_menu)],
    states={
        TEAM1: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_team1)],
        TEAM2: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_team2)],
        AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_amount)],
        USERS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_users)],
        SUBJECT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_subject)],
        CONFIRM_BET: [
            CallbackQueryHandler(confirm_bet, pattern="^confirm_bet$"),
            CallbackQueryHandler(cancel_bet, pattern="^cancel_bet$")
        ],
        ADD_USER: [MessageHandler(filters.TEXT & ~filters.COMMAND, add_user_score)]
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

app.add_handler(CommandHandler("start", start))
app.add_handler(conv)
app.add_handler(CallbackQueryHandler(delete_bet, pattern="^delete_\\d+$"))

print("🤖 Bot is running...")
app.run_polling()
