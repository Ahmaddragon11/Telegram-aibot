from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from app.models.schemas import CommandRequest, AICommandResponse, ErrorResponse
from app.middleware.auth import verify_api_key

router = APIRouter(prefix="/api/ai", tags=["AI"])
security = HTTPBearer()


@router.post("/command", response_model=AICommandResponse)
async def process_command(
    request: CommandRequest,
    credentials = Depends(security)
):
    """
    Process a natural language command with AI
    
    - **text**: The natural language command to process
    - **user_id**: Optional user ID for tracking
    - **context**: Optional additional context
    
    Returns structured JSON command from AI
    """
    # Verify authentication
    await verify_api_key(credentials)
    
    # TODO: This will be implemented in Step 3 with Gemini AI
    return AICommandResponse(
        status="success",
        action="pending",
        message="AI processing stub - will be implemented in Step 3"
    )


@router.get("/status")
async def get_ai_status(credentials = Depends(security)):
    """Get AI service status"""
    await verify_api_key(credentials)
    
    return {
        "status": "ready",
        "provider": "gemini",
        "model": "gemini-pro"
    }

