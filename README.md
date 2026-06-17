# آریا — دستیار هوشمند فارسی 🤖

یک اپلیکیشن وب کامل با پایتون (Flask) که از Anthropic API برای صحبت کردن استفاده می‌کند.

## ساختار پروژه

```
aria-ai/
├── app.py              ← سرور اصلی Flask
├── templates/
│   └── index.html      ← صفحه چت
├── requirements.txt    ← کتابخانه‌های لازم
├── Procfile             ← برای دیپلوی روی Render/Heroku
└── runtime.txt          ← نسخه پایتون
```

---

## 🖥️ اجرای لوکال (روی کامپیوتر خودت)

### ۱. نصب کتابخانه‌ها
```bash
cd aria-ai
pip install -r requirements.txt --break-system-packages
```

### ۲. کلید API رو بگیر
به [console.anthropic.com](https://console.anthropic.com) برو، حساب بساز و یک API key بساز.

### ۳. کلید رو تنظیم کن و اجرا کن

**لینوکس / مک:**
```bash
export ANTHROPIC_API_KEY=sk-ant-...
python3 app.py
```

**ویندوز (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY="sk-ant-..."
python app.py
```

### ۴. مرورگر رو باز کن
```
http://localhost:3000
```

---

## 🌐 دیپلوی آنلاین (رایگان)

### روش ۱: Render.com (پیشنهادی — رایگان و ساده)

۱. پروژه رو در یک ریپازیتوری GitHub قرار بده (private یا public)
۲. وارد [render.com](https://render.com) شو و حساب بساز
۳. روی **New +** بزن → **Web Service**
۴. ریپازیتوری گیت‌هابت رو وصل کن
۵. تنظیمات:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
۶. در بخش **Environment Variables** اضافه کن:
   - Key: `ANTHROPIC_API_KEY`
   - Value: کلید API خودت
۷. روی **Create Web Service** بزن

بعد از چند دقیقه، یک آدرس مثل `https://aria-ai.onrender.com` به‌ت می‌ده — همینه، آنلاین شدی! 🎉

### روش ۲: Railway.app

۱. وارد [railway.app](https://railway.app) شو
۲. **New Project** → **Deploy from GitHub repo**
۳. ریپازیتوری رو انتخاب کن
۴. در تب **Variables**:
   - `ANTHROPIC_API_KEY` = کلید خودت
۵. Railway به صورت خودکار `Procfile` رو تشخیص می‌ده و دیپلوی می‌کنه

### روش ۳: Fly.io / PythonAnywhere
مشابه بالا — فقط باید `ANTHROPIC_API_KEY` رو به عنوان متغیر محیطی (Environment Variable) تنظیم کنی.

---

## ⚠️ نکته امنیتی مهم

کلید API هیچ‌وقت داخل کد یا فایل HTML نباید نوشته شود. این برنامه طوری طراحی شده که کلید فقط روی **سرور** (در Environment Variable) ذخیره می‌شود و مرورگر کاربر هرگز آن را نمی‌بیند — این دقیقاً همان دلیلی است که این پروژه به جای کار مستقیم در مرورگر، از یک بک‌اند پایتونی استفاده می‌کند.

---

## ✏️ شخصی‌سازی

برای تغییر شخصیت آریا، متغیر `SYSTEM_PROMPT` در فایل `app.py` را ویرایش کن.
برای افزودن اطلاعات اختصاصی خودت (مثل اطلاعات شرکت یا محصول)، آن‌ها را داخل `SYSTEM_PROMPT` اضافه کن یا روش RAG را با یک دیتابیس برداری (مثل FAISS) پیاده‌سازی کن.
