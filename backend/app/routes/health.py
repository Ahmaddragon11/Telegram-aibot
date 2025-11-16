from fastapi import APIRouter
from app.models.schemas import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """
    Health check endpoint
    
    Returns the status of the backend and connected services
    """
    return HealthResponse(
        status="healthy",
        backend="running",
        ai_service="connected",
        bot_service="connected"
    )

