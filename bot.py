import os
from flask import Flask, request
import requests

app = Flask(__name__)

# توکن ربات تو - همین توکن خودت رو بذار
BOT_TOKEN = "8243990371:AAF_fFScvmH91n8LyayPvgpLYOor0Qr7krs"

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    update = request.get_json()
    
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message'].get('text', '')
        
        if text.startswith('/start'):
            parts = text.split(' ')
            if len(parts) > 1:
                serial = parts[1]
                # پاسخ تستی - بعداً کامل می‌شه
                response = f"✅ تست: کالای اصل\nسریال: {serial}"
            else:
                response = "لطفاً QR کد روی کالا را اسکن کنید."
            
            # ارسال پاسخ
            send_message(chat_id, response)
    
    return 'OK'

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, json=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
