# 🚀 Telegram AI Bot Platform

A full-stack, production-ready AI-powered web platform connected to Telegram. This project integrates natural language processing with Telegram bot automation through a modern web dashboard.

## 📋 Project Overview

This platform consists of four main components:

1. **Web Dashboard (React Frontend)** - Modern UI for commanding the AI bot
2. **Backend Server (FastAPI)** - REST API handling AI integration and bot coordination
3. **AI Integration** - Support for multiple LLMs (Groq, OpenAI)
4. **Telegram Bot** - Executes commands from the backend

### 🔄 Workflow

```
User Input (Dashboard)
    ↓
Frontend sends to Backend (/api/ai/command)
    ↓
Backend forwards to AI Model (Groq/OpenAI)
    ↓
AI returns structured JSON command
    ↓
Backend validates and forwards to Telegram Bot
    ↓
Bot executes command
    ↓
Results sent back to Dashboard
```

## 🛠️ Tech Stack

- **Backend**: Python 3.11 + FastAPI (async REST API)
- **Frontend**: React 18 (modern UI with hooks)
- **Telegram**: python-telegram-bot (v20.3)
- **AI Models**: Groq, OpenAI APIs
- **Deployment**: Docker + Docker Compose
- **Authentication**: JWT-based token security

## 📁 Project Structure

```
Telegram-aibot/
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── main.py         # FastAPI app setup
│   │   ├── middleware/     # Auth & security
│   │   ├── routes/         # API endpoints
│   │   ├── services/       # Business logic
│   │   └── models/         # Pydantic schemas
│   ├── requirements.txt
│   └── Dockerfile
├── bot/                     # Telegram Bot service
│   ├── app/
│   │   └── bot.py          # Bot logic
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                # React application
│   ├── src/                # React components
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml       # Local dev & deployment
├── .env.example             # Environment template
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.11+ (for local development)
- Node.js 18+ (for frontend development)
- API keys for AI services (Groq or OpenAI)
- Telegram Bot Token from @BotFather

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ahmaddragon11/Telegram-aibot.git
   cd Telegram-aibot
   ```

2. **Create environment file**
   ```bash
   cp .env.example .env
   ```

3. **Update .env with your credentials**
   ```
   AI_API_KEY=your-groq-api-key
   TELEGRAM_BOT_TOKEN=your-telegram-token
   API_KEY=your-secret-api-key
   JWT_SECRET=your-jwt-secret
   BOT_SECRET_KEY=your-bot-secret
   ```

4. **Start all services with Docker Compose**
   ```bash
   docker-compose up -d
   ```

5. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Local Development (Without Docker)

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm start
```

**Bot:**
```bash
cd bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m app.bot
```

## 📚 API Endpoints

All endpoints are documented with Swagger at `http://localhost:8000/docs`

### Health Check
- `GET /health` - Service health status

### AI Integration
- `POST /api/ai/command` - Send natural language command to AI
  - Request: `{ "text": "Tell the main group hello" }`
  - Response: `{ "action": "send_message", "group": "main", "message": "hello" }`

### Bot Management
- `POST /api/bot/execute` - Execute a bot command (internal use)
- `GET /api/bot/status` - Get bot execution status

## 🔐 Authentication

All API endpoints (except `/health`) require authentication via Bearer token in the Authorization header:

```bash
Authorization: Bearer your-api-key
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
python -m pytest tests/
```

### Frontend Tests
```bash
cd frontend
npm test
```

### Integration Tests
```bash
docker-compose up
# Run test suite
```

## 📝 Development Workflow

### Building for Production

```bash
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d
```

### Viewing Logs

```bash
docker-compose logs -f backend
docker-compose logs -f bot
docker-compose logs -f frontend
```

### Stopping Services

```bash
docker-compose down
```

## 🛡️ Security Considerations

1. **API Keys**: Never commit `.env` files. Use `.env.example` as template
2. **JWT Tokens**: Set a strong `JWT_SECRET` in production
3. **Bot Secret**: Verify requests from bot service using `BOT_SECRET_KEY`
4. **CORS**: Configure allowed origins for frontend
5. **Rate Limiting**: Implement on production API
6. **HTTPS**: Use HTTPS in production deployments

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes
3. Test thoroughly
4. Commit with clear messages: `git commit -m "feat: add new feature"`
5. Push to branch: `git push origin feature/my-feature`
6. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation

---

**Build Status**: Currently in development - Step 1 Complete ✅