#!/bin/bash
# Quick setup and test script for Step 2

echo "========================================="
echo "🚀 Step 2 - Backend Setup & Test"
echo "========================================="

# Navigate to backend directory
cd /workspaces/Telegram-aibot/backend

echo "📦 Installing Python dependencies..."
pip install -q -r requirements.txt

echo "✅ Dependencies installed!"

echo ""
echo "📝 Creating .env file..."
cp ../.env.example ../.env
echo "✅ .env file created (update with your credentials)"

echo ""
echo "🧪 Running Python import tests..."
python -c "
from app.main import app
from app.config import settings
from app.models.schemas import CommandRequest, AICommandResponse
from app.middleware.auth import create_access_token, verify_token
from app.routes import health, ai, bot

print('✅ All imports successful!')
print('📝 FastAPI App Loaded')
print('📝 Settings Loaded')
print('📝 All routes loaded')
"

echo ""
echo "========================================="
echo "✅ Step 2 Backend Setup Complete!"
echo "========================================="
echo ""
echo "🚀 To start the backend:"
echo "   cd /workspaces/Telegram-aibot/backend"
echo "   uvicorn app.main:app --reload"
echo ""
echo "📚 Then visit: http://localhost:8000/docs"
echo "========================================="
