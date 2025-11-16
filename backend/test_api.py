"""
Quick test script to verify the FastAPI backend is working
Run this after starting the backend with: uvicorn app.main:app --reload
"""

import requests
import json

BASE_URL = "http://localhost:8000"
API_KEY = "your-secret-api-key-here"  # Change this to match your .env

def test_health():
    """Test health endpoint (no auth required)"""
    print("\n🔍 Testing Health Endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200

def test_root():
    """Test root endpoint"""
    print("\n🔍 Testing Root Endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200

def test_ai_command_without_auth():
    """Test AI command without authentication (should fail)"""
    print("\n🔍 Testing AI Command Without Auth (Should Fail)...")
    response = requests.post(
        f"{BASE_URL}/api/ai/command",
        json={"text": "Hello world"}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 403

def test_ai_command_with_auth():
    """Test AI command with authentication"""
    print("\n🔍 Testing AI Command With Auth...")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(
        f"{BASE_URL}/api/ai/command",
        json={"text": "Tell the main group hello"},
        headers=headers
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200

def test_bot_status():
    """Test bot status endpoint"""
    print("\n🔍 Testing Bot Status Endpoint...")
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(
        f"{BASE_URL}/api/bot/status",
        headers=headers
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Telegram AI Bot Backend - Quick Test Suite")
    print("=" * 60)
    
    try:
        test_root()
        test_health()
        test_ai_command_without_auth()
        test_ai_command_with_auth()
        test_bot_status()
        
        print("\n" + "=" * 60)
        print("✅ All tests passed!")
        print("=" * 60)
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Make sure the backend is running: uvicorn app.main:app --reload")
