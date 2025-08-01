# config.py

import os

class Config:
    # Telegram Bot Credentials
    API_ID = int(os.environ.get("API_ID", "14689508"))  # আপনার API ID দিন
    API_HASH = os.environ.get("API_HASH", "79413cfe2d8cc93ddf1815ef588e80d5")  # আপনার API Hash দিন
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8453330161:AAG1Dsk_XmN5Ki0HybLLAZl7ARvCHV1hXvQ")  # আপনার Bot Token দিন

    # Channel and Admin Details
    # আপনার ফাইল স্টোর চ্যানেলের আইডি দিন। এটি অবশ্যই একটি integer হতে হবে।
    # আইডি বের করার জন্য চ্যানেলের যেকোনো পোস্টের লিঙ্ক কপি করুন। যেমন: https://t.me/c/1234567890/2
    # এখানে চ্যানেল আইডি হলো -1001234567890
    FILE_STORE_CHANNEL = int(os.environ.get("FILE_STORE_CHANNEL", "-1002808415500"))

    # যে অ্যাডমিনের সাথে যোগাযোগ করতে বলা হবে
    CONTACT_ADMIN = os.environ.get("CONTACT_ADMIN", "@Nobita_X_Surya")

    # Welcome Message এর জন্য ছবি (ঐচ্ছিক)
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/e08591039671c75dec218-67c62b623b67df2c7f.jpg")

    # Database (For Render/Heroku)
    # যদি ডাটাবেস ব্যবহার করতে চান, তার URL এখানে দিন। আপাতত এটি প্রয়োজন নেই।
    DB_URL = os.environ.get("DB_URL", mongodb+srv://s3614371925809272310:s3614371925809272310@cluster0.ufhhuzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)