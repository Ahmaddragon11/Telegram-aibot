# 📚 Backend API Reference - Step 2

## قائمة الـ API Endpoints الكاملة

### 🟢 Public Endpoints (No Authentication Required)

#### 1. Root Endpoint
```
GET /
```
**الغرض**: معلومات عن API
**الاستجابة**:
```json
{
  "message": "🚀 Telegram AI Bot Backend API",
  "version": "1.0.0",
  "docs": "http://localhost:8000/docs",
  "health": "http://localhost:8000/health"
}
```

---

#### 2. Health Check
```
GET /health
```
**الغرض**: التحقق من صحة الخدمة
**الاستجابة**:
```json
{
  "status": "healthy",
  "backend": "running",
  "ai_service": "connected",
  "bot_service": "connected",
  "timestamp": "2024-11-16T10:30:00"
}
```

---

#### 3. API Health
```
GET /api/health
```
**الغرض**: التحقق من صحة API
**الاستجابة**:
```json
{
  "status": "healthy",
  "service": "telegram-aibot-backend",
  "ai_provider": "gemini"
}
```

---

### 🔴 Protected Endpoints (Authentication Required)

**ملاحظة**: جميع الطلبات التالية تحتاج إلى `Authorization` header:
```
Authorization: Bearer your-api-key-here
```

---

#### 4. Process AI Command
```
POST /api/ai/command
```
**الغرض**: معالجة أمر طبيعي مع AI (Gemini)
**رؤوس الطلب**:
```
Authorization: Bearer your-api-key-here
Content-Type: application/json
```
**جسم الطلب**:
```json
{
  "text": "Tell the main group hello",
  "user_id": "user123",
  "context": {
    "group_name": "main",
    "language": "en"
  }
}
```
**الاستجابة** (في الخطوة 3):
```json
{
  "status": "success",
  "action": "send_message",
  "target": "main",
  "parameters": {
    "message": "hello"
  },
  "confidence": 0.95,
  "message": "Command processed successfully"
}
```

---

#### 5. Get AI Status
```
GET /api/ai/status
```
**الغرض**: الحصول على حالة خدمة AI
**الاستجابة**:
```json
{
  "status": "ready",
  "provider": "gemini",
  "model": "gemini-pro"
}
```

---

#### 6. Execute Bot Command
```
POST /api/bot/execute
```
**الغرض**: تنفيذ أمر على Telegram bot (للاستخدام الداخلي)
**جسم الطلب**:
```json
{
  "action": "send_message",
  "target": "main",
  "parameters": {
    "message": "Hello from AI!",
    "parse_mode": "HTML"
  },
  "request_id": "req_123456"
}
```
**الاستجابة** (في الخطوة 4):
```json
{
  "status": "success",
  "request_id": "req_123456",
  "action": "send_message",
  "result": {
    "message_id": 12345,
    "sent_at": "2024-11-16T10:30:00"
  },
  "timestamp": "2024-11-16T10:30:05"
}
```

---

#### 7. Get Bot Status
```
GET /api/bot/status
```
**الغرض**: الحصول على حالة Telegram Bot
**الاستجابة**:
```json
{
  "status": "ready",
  "connected": true,
  "uptime": "unknown"
}
```

---

#### 8. Get Bot Logs
```
GET /api/bot/logs?limit=50
```
**الغرض**: الحصول على سجل الأوامر المنفذة
**المعاملات**:
- `limit` (اختياري): عدد السجلات (افتراضي: 50)

**الاستجابة**:
```json
{
  "total": 0,
  "logs": []
}
```

---

## 🔐 Authentication Methods

### Method 1: API Key
```bash
curl -X GET http://localhost:8000/api/ai/status \
  -H "Authorization: Bearer your-secret-api-key-here"
```

### Method 2: JWT Token
```bash
# الحصول على token أولاً
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "admin",
    "password": "password123"
  }'

# ثم استخدام Token
curl -X GET http://localhost:8000/api/ai/status \
  -H "Authorization: Bearer <jwt-token>"
```

---

## ⚠️ Error Responses

### 401 Unauthorized
```json
{
  "status": "error",
  "code": "UNAUTHORIZED",
  "message": "Invalid credentials"
}
```

### 403 Forbidden
```json
{
  "status": "error",
  "code": "FORBIDDEN",
  "message": "Missing authorization header"
}
```

### 404 Not Found
```json
{
  "status": "error",
  "code": "NOT_FOUND",
  "message": "Endpoint not found",
  "path": "/api/endpoint"
}
```

### 500 Internal Server Error
```json
{
  "status": "error",
  "code": "INTERNAL_ERROR",
  "message": "Internal server error"
}
```

---

## 📊 Pydantic Models

### CommandRequest
```python
{
  "text": str,              # Natural language command (1-1000 chars)
  "user_id": str | null,    # Optional user ID
  "context": dict | null    # Optional additional context
}
```

### AICommandResponse
```python
{
  "status": str,            # "success" or "error"
  "action": str,            # Action type
  "target": str | null,     # Target
  "parameters": dict,       # Action parameters
  "confidence": float,      # Confidence score (0-1)
  "raw_response": str | null,  # Raw AI response
  "message": str | null     # Human-readable message
}
```

### BotExecuteRequest
```python
{
  "action": str,            # Action to execute
  "target": str,            # Target (group/user)
  "parameters": dict,       # Action parameters
  "request_id": str | null  # Optional request ID
}
```

### BotExecutionResult
```python
{
  "status": str,            # "success", "pending", or "failed"
  "request_id": str | null, # Request tracking ID
  "action": str,            # Executed action
  "result": dict | null,    # Execution result
  "error": str | null,      # Error message if failed
  "timestamp": datetime     # Execution timestamp
}
```

---

## 🧪 Testing Examples

### cURL Examples

```bash
# 1. Health check (public)
curl http://localhost:8000/health

# 2. Process AI command (protected)
curl -X POST http://localhost:8000/api/ai/command \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Send hello to main group",
    "user_id": "user1"
  }'

# 3. Get AI status (protected)
curl -X GET http://localhost:8000/api/ai/status \
  -H "Authorization: Bearer your-api-key"

# 4. Execute bot command (protected)
curl -X POST http://localhost:8000/api/bot/execute \
  -H "Authorization: Bearer your-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "send_message",
    "target": "main",
    "parameters": {"message": "Hello!"}
  }'
```

---

## 📖 Documentation URLs

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

---

**اُنشئ بواسطة**: GitHub Copilot
**التاريخ**: November 16, 2024
**الإصدار**: 1.0.0 - Step 2 Complete
