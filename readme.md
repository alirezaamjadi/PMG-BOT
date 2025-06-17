
![Screenshot 2025-06-17 053206](https://github.com/user-attachments/assets/77559b97-2f9b-4ed3-b71f-0729ba3d21b0)


# 🎯🤖 PMG Bot | ربات پیش‌بینی مسابقات جایزه دار 🏆🎉

╔════════════════════════════════════════════════════════════════════╗  
║                                                                    ║  
║  🇮🇷 **معرفی**                                                    ║  
║  PMG Bot ربات تلگرامی مدیریت پیش‌بینی مسابقات جایزه‌دار است.    ║  
║  به شما امکان می‌دهد شرط‌ها را ثبت، مدیریت و نتیجه‌ها را وارد کنید.║  
║  🛠 ساخته شده توسط: علیرضا امجدی - سال 2025                        ║  
║  🐍 زبان برنامه‌نویسی: پایتون                                      ║  
║                                                                    ║  
║  📦 **اجزای پروژه**                                               ║  
║  - `bot.py`: کد اصلی ربات با تمام منطق و گفتگوها                   ║  
║  - `config.py`: شامل توکن ربات و نام کاربری ادمین                   ║  
║  - `data.json`: ذخیره شرط‌ها و حساب کاربران                        ║  
║                                                                    ║  
║  ⚙️ **نصب و راه‌اندازی**                                          ║  
║  1️⃣ نصب پایتون 3.13+                                               ║  
║  2️⃣ نصب کتابخانه تلگرام:                                          ║  
║     ```bash                                                        ║  
║     pip install python-telegram-bot --upgrade                     ║  
║     ```                                                           ║  
║  3️⃣ وارد کردن توکن در `config.py`                                ║  
║  4️⃣ اجرای ربات:                                                  ║  
║     ```bash                                                        ║  
║     python bot.py                                                 ║  
║     ```                                                           ║  
║                                                                    ║  
║  🎮 **آموزش کار با ربات**                                        ║  
║  🔹 منوی اصلی:                                                    ║  
║     1️⃣ شرط جدید                                                  ║  
║     2️⃣ شرط‌های جاری                                             ║  
║     3️⃣ حساب                                                      ║  
║     4️⃣ درباره بات                                                ║  
║  🔹 ثبت شرط جدید:                                                 ║  
║     وارد کردن نام تیم‌ها، مبلغ، کاربران شرکت‌کننده، موضوع        ║  
║     تایید یا لغو ثبت شرط                                          ║  
║  🔹 مدیریت شرط‌های جاری:                                         ║  
║     مشاهده، حذف شرط یا ثبت نتیجه                                 ║  
║  🔹 مدیریت حساب‌ها:                                              ║  
║     مشاهده امتیاز، افزودن امتیاز با دستور `افزودن نام مقدار`    ║  
║     لغو عملیات با «لغو» یا `/cancel`                             ║  
║                                                                    ║  
║  🖼 **نمونه تصاویر**                                              ║  
║  | منوی اصلی | شرط جدید | شرط‌های جاری | مدیریت حساب‌ها |          ║  
║  |---|---|---|---|                                                ║  
║                                                                    ║  
║  📝 **لایسنس و شرایط استفاده**                                   ║  
║  پروژه تحت مجوز MIT است. لطفا پیش از استفاده یا تغییر، با سازنده هماهنگ کنید.║  
║                                                                    ║  
║  📬 **تماس با سازنده**                                            ║  
║  علیرضا امجدی                                                    ║  
║  Telegram: @YourTelegramUsername                                  ║  
║  Email: your.email@example.com                                   ║  
║                                                                    ║  
║  🤖 **تشکر و قدردانی**                                           ║  
║  با کمک‌های کوچک هوش مصنوعی توسعه یافته است.                    ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝  

---  

🇺🇸 **PMG Bot - Prize Match Guessing Telegram Bot**

---  

╔════════════════════════════════════════════════════════════════════╗  
║                                                                    ║  
║  🚀 **Introduction**                                              ║  
║  PMG Bot is a Telegram bot to manage prize-based match predictions.║  
║  You can create, manage, and record bet results with ease.         ║  
║  🛠 Created by: Alireza Amjadi - 2025                             ║  
║  🐍 Language: Python                                              ║  
║                                                                    ║  
║  📦 **Project Components**                                        ║  
║  - `bot.py`: Main bot logic and conversations                    ║  
║  - `config.py`: Bot token & admin username                        ║  
║  - `data.json`: Data storage for bets and user accounts           ║  
║                                                                    ║  
║  ⚙️ **Installation & Setup**                                     ║  
║  1️⃣ Install Python 3.13+                                         ║  
║  2️⃣ Install telegram lib:                                       ║  
║     ```bash                                                    ║  
║     pip install python-telegram-bot --upgrade                 ║  
║     ```                                                       ║  
║  3️⃣ Put your bot token in `config.py`                         ║  
║  4️⃣ Run the bot:                                              ║  
║     ```bash                                                    ║  
║     python bot.py                                             ║  
║     ```                                                       ║  
║                                                                    ║  
║  🎮 **How to Use**                                               ║  
║  🔹 Main menu options:                                           ║  
║     1️⃣ New Bet                                                ║  
║     2️⃣ Ongoing Bets                                           ║  
║     3️⃣ Accounts                                               ║  
║     4️⃣ About Bot                                              ║  
║  🔹 Create new bet:                                            ║  
║     Enter teams, amount, participants, and subject             ║  
║     Confirm or cancel the bet                                  ║  
║  🔹 Manage ongoing bets:                                       ║  
║     View, delete, or record results                            ║  
║  🔹 Manage accounts:                                          ║  
║     View points, add points with `add username amount` command ║  
║     Cancel with "cancel" or `/cancel`                         ║  
║                                                                    ║  
║  🖼 **Sample Screenshots**                                      ║  
║  | Main Menu | New Bet | Ongoing Bets | Accounts |             ║  
║  |---|---|---|---|                                               ║  
║                                                                    ║  
║  📝 **License & Usage**                                         ║  
║  MIT license. Please coordinate with author before usage or      ║  
║  redistribution.                                                ║  
║                                                                    ║  
║  📬 **Contact**                                                ║  
║  Alireza Amjadi                                                ║  
║  Email: alirezaamjaid1387@example.com                               ║  
║                                                                    ║  
║  🤖 **Acknowledgements**                                       ║  
║  Developed with minor AI assistance.                           ║  
║                                                                    ║  
╚════════════════════════════════════════════════════════════════════╝  
