import yfinance as yf
import telebot
import time
import pandas as pd

# إعدادات البوت
TELEGRAM_TOKEN = 'ضع_توكن_البوت_هنا'
CHAT_ID = 'ضع_رقم_CHAT_ID_هنا'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# إعدادات المراقبة
SYMBOLS_FILE = 'symbols.txt'
CHECK_INTERVAL = 15
PERCENT_CHANGE_THRESHOLD = 3.0

# قراءة قائمة الأسهم
with open(SYMBOLS_FILE, 'r') as f:
    symbols = [line.strip() for line in f.readlines() if line.strip() != '']

print(f'📈 Monitoring {len(symbols)} symbols...')

# تابع الحالة السابقة لكل سهم
previous_prices = {}

def check_stocks():
    global previous_prices
    data = yf.download(tickers=' '.join(symbols), period='1d', interval='1m', progress=False, threads=True)

    for symbol in symbols:
        try:
            stock_data = data['Close'][symbol]
            latest_price = stock_data.iloc[-1]
            first_price = stock_data.iloc[0]

            percent_change = ((latest_price - first_price) / first_price) * 100

            if percent_change >= PERCENT_CHANGE_THRESHOLD:
                if symbol not in previous_prices or previous_prices[symbol] < PERCENT_CHANGE_THRESHOLD:
                    message = f'🚨 سهم {symbol} ارتفع +{percent_change:.2f}% \nالسعر الآن: {latest_price:.2f}'
                    bot.send_message(chat_id=CHAT_ID, text=message)
                    print(message)

                previous_prices[symbol] = percent_change

        except Exception as e:
            print(f'خطأ في السهم {symbol}: {e}')

while True:
    try:
        check_stocks()
    except Exception as e:
        print(f'❌ Error in main loop: {e}')
    
    time.sleep(CHECK_INTERVAL)