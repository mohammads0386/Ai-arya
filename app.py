"""
آریا — دستیار هوشمند فارسی
یک اپلیکیشن کامل پایتونی (Flask) که هم سایت را سرو می‌کند و هم با Anthropic API صحبت می‌کند.
طراحی شده برای اجرای لوکال و دیپلوی آنلاین (Render / Railway / Fly.io / ...).
"""

import os
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"
MODEL = "claude-sonnet-4-6"

SYSTEM_PROMPT = """تو آریا هستی — یک دستیار هوشمند فارسی با شخصیت گرم، دوستانه و باهوش.
- همیشه به فارسی روان و طبیعی صحبت می‌کنی
- گرم، صمیمی و شوخ‌طبع هستی
- وقتی نمی‌دونی چیزی رو، صادقانه می‌گی
- از ایموجی‌ها گاهی استفاده می‌کنی تا مکالمه گرم‌تر باشه
- اگه سوال فنی باشه، دقیق و کامل جواب می‌دی
- اگه کسی پرسید کی هستی، بگو «آریا هستم، یک دستیار هوشمند فارسی»"""


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    """برای چک کردن سلامت سرور توسط سرویس‌های دیپلوی (Render/Railway)"""
    return jsonify({"status": "ok", "api_key_set": bool(ANTHROPIC_API_KEY)})


@app.route("/api/chat", methods=["POST"])
def chat():
    if not ANTHROPIC_API_KEY:
        return jsonify({"error": {"message": "کلید API روی سرور تنظیم نشده است."}}), 500

    data = request.get_json(force=True) or {}
    messages = data.get("messages", [])

    if not messages:
        return jsonify({"error": {"message": "پیامی ارسال نشده است."}}), 400

    try:
        resp = requests.post(
            ANTHROPIC_URL,
            headers={
                "Content-Type": "application/json",
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
            },
            json={
                "model": MODEL,
                "max_tokens": 1024,
                "system": SYSTEM_PROMPT,
                "messages": messages,
            },
            timeout=60,
        )
        return jsonify(resp.json()), resp.status_code

    except requests.exceptions.Timeout:
        return jsonify({"error": {"message": "زمان پاسخ تمام شد. دوباره امتحان کن."}}), 504
    except Exception as e:
        return jsonify({"error": {"message": str(e)}}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    print(f"✅ آریا روی http://localhost:{port} اجرا شد")
    print(f"🔑 کلید API: {'تنظیم شده ✓' if ANTHROPIC_API_KEY else '❌ تنظیم نشده!'}")
    app.run(host="0.0.0.0", port=port, debug=False)
