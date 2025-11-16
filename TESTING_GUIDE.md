# 🧪 Step 2 - Verification & Testing Guide

## ✅ تحقق من الملفات المُنشأة

```bash
# تحقق من بنية المشروع
ls -la /workspaces/Telegram-aibot/backend/app/

# يجب أن تجد:
# ✓ main.py
# ✓ config.py
# ✓ middleware/auth.py
# ✓ models/schemas.py
# ✓ routes/health.py
# ✓ routes/ai.py
# ✓ routes/bot.py
# ✓ services/ai_service.py
```

## 🚀 خيارات التشغيل

### الخيار 1: التشغيل المباشر (الموصى به للتطوير)

```bash
# 1. انتقل إلى مجلد المشروع
cd /workspaces/Telegram-aibot

# 2. نسخ ملف البيئة
cp .env.example .env

# 3. تعديل .env بمفاتيحك (اختياري للاختبار الأساسي)
# vim .env

# 4. انتقل إلى المجلد الخلفي
cd backend

# 5. أنشئ بيئة افتراضية
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 6. ثبت المتطلبات
pip install -r requirements.txt

# 7. شغّل الخادم
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### الخيار 2: مع Docker Compose

```bash
# من جذر المشروع
cd /workspaces/Telegram-aibot

# تأكد من وجود .env
cp .env.example .env

# شغّل الخدمات
docker-compose up

# أو شغّل Backend فقط
docker-compose up backend
```

## 📝 اختبار الـ API

### الطريقة 1: Swagger UI (التفاعلية - الموصى بها)

بعد بدء الخادم، انتقل إلى:
```
http://localhost:8000/docs
```

ستجد:
- جميع الـ endpoints
- القدرة على اختبار كل endpoint مباشرة
- توثيق تلقائي لكل معامل
- نماذج الطلب والاستجابة

### الطريقة 2: ReDoc (التوثيق الجميل)

```
http://localhost:8000/redoc
```

### الطريقة 3: باستخدام cURL

```bash
# 1. فحص الصحة (بدون مصادقة)
curl http://localhost:8000/health

# 2. الحصول على معلومات الـ API (بدون مصادقة)
curl http://localhost:8000/

# 3. معالجة أمر AI (مع مصادقة)
curl -X POST http://localhost:8000/api/ai/command \
  -H "Authorization: Bearer your-secret-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{"text": "Tell the main group hello"}'

# 4. حالة خدمة AI
curl -X GET http://localhost:8000/api/ai/status \
  -H "Authorization: Bearer your-secret-api-key-here"

# 5. حالة Telegram Bot
curl -X GET http://localhost:8000/api/bot/status \
  -H "Authorization: Bearer your-secret-api-key-here"

# 6. تنفيذ أمر Bot
curl -X POST http://localhost:8000/api/bot/execute \
  -H "Authorization: Bearer your-secret-api-key-here" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "send_message",
    "target": "main",
    "parameters": {"message": "Hello from API!"}
  }'

# 7. الحصول على السجلات
curl -X GET "http://localhost:8000/api/bot/logs?limit=10" \
  -H "Authorization: Bearer your-secret-api-key-here"
```

### الطريقة 4: استخدام Python Test Script

```bash
# من مجلد backend
python test_api.py
```

**النتيجة المتوقعة**:
```
✅ All tests passed!
```

### الطريقة 5: استخدام Python مباشرة

```python
import requests

BASE_URL = "http://localhost:8000"
API_KEY = "your-secret-api-key-here"

# فحص الصحة
response = requests.get(f"{BASE_URL}/health")
print(response.json())

# معالجة أمر
headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.post(
    f"{BASE_URL}/api/ai/command",
    json={"text": "Hello world"},
    headers=headers
)
print(response.json())
```

## 🐛 استكشاف الأخطاء

### المشكلة: "ModuleNotFoundError"

```bash
# الحل: ثبت المتطلبات
pip install -r requirements.txt
```

### المشكلة: "Connection refused"

```bash
# تأكد من أن الخادم يعمل
# الخادم يجب أن يكون على المنفذ 8000
netstat -tuln | grep 8000
```

### المشكلة: "401 Unauthorized"

```bash
# تحقق من API_KEY في .env
# تأكد من استخدام Bearer token في رؤوس الطلب
# Authorization: Bearer your-api-key-here
```

### المشكلة: "CORS error"

```bash
# تأكد من أن frontend URL في CORS_ORIGINS
# افتح STEP2_GUIDE.md وراجع قسم CORS
```

## 📊 ما يجب توقعه

### 1. استجابة /health (بدون مصادقة)

```json
{
  "status": "healthy",
  "backend": "running",
  "ai_service": "connected",
  "bot_service": "connected",
  "timestamp": "2024-11-16T10:30:00"
}
```

### 2. استجابة /api/ai/command (مع مصادقة)

```json
{
  "status": "success",
  "action": "pending",
  "message": "AI processing stub - will be implemented in Step 3"
}
```

### 3. استجابة /api/bot/status (مع مصادقة)

```json
{
  "status": "ready",
  "connected": true,
  "uptime": "unknown"
}
```

## ✅ Checklist الاختبار

- [ ] الخادم يبدأ بدون أخطاء
- [ ] `/health` يرجع 200 status
- [ ] `/api/health` يرجع 200 status
- [ ] `/docs` يفتح Swagger UI
- [ ] `/redoc` يفتح ReDoc
- [ ] `/api/ai/command` بدون auth يرجع 403
- [ ] `/api/ai/command` مع auth يرجع 200
- [ ] `/api/bot/status` يرجع 200
- [ ] جميع الـ endpoints موثقة تلقائياً

## 📈 Performance Testing

```bash
# استخدم Apache Bench أو similar
ab -n 100 -c 10 http://localhost:8000/health

# أو باستخدام wrk
wrk -t4 -c100 -d30s http://localhost:8000/health
```

## 🔐 اختبار الأمان

```bash
# 1. جرب الوصول بدون token
curl http://localhost:8000/api/ai/command

# يجب أن ترى: 403 Forbidden

# 2. جرب مع token خاطئ
curl -H "Authorization: Bearer wrong-key" \
  http://localhost:8000/api/ai/command

# يجب أن ترى: 401 Unauthorized

# 3. جرب مع API Key صحيح
curl -H "Authorization: Bearer your-secret-api-key-here" \
  -X POST http://localhost:8000/api/ai/command \
  -H "Content-Type: application/json" \
  -d '{"text": "test"}'

# يجب أن ترى: 200 Success
```

## 📚 المراجع

- **STEP2_GUIDE.md** - دليل التنفيذ الشامل
- **API_REFERENCE.md** - مرجع API كامل
- **STRUCTURE.md** - بنية المشروع
- **README.md** - دليل المشروع الرئيسي

---

✅ **بعد التحقق من جميع الخطوات، يكون لديك خادم FastAPI عامل تماماً!**

⏭️ **الخطوة التالية**: Step 3 - Gemini AI Integration
