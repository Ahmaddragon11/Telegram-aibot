from pydantic import BaseModel, Field
from typing import Optional, Any, Dict, List
from datetime import datetime


# ============ Request Models ============

class CommandRequest(BaseModel):
    """Model for AI command requests"""
    text: str = Field(..., min_length=1, max_length=1000, description="Natural language command")
    user_id: Optional[str] = Field(None, description="User ID making the request")
    context: Optional[Dict[str, Any]] = Field(None, description="Additional context for the AI")


class BotExecuteRequest(BaseModel):
    """Model for bot execution requests"""
    action: str = Field(..., description="Action to execute (e.g., send_message)")
    target: str = Field(..., description="Target (e.g., group name, user ID)")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Action parameters")
    request_id: Optional[str] = Field(None, description="Unique request ID for tracking")


class LoginRequest(BaseModel):
    """Model for user login"""
    username: str = Field(..., min_length=1)
    password: str = Field(..., min_length=6)


# ============ Response Models ============

class AICommandResponse(BaseModel):
    """Response from AI processing"""
    status: str = Field(default="success", description="success or error")
    action: str = Field(..., description="Action type")
    target: Optional[str] = Field(None, description="Target for the action")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Action parameters")
    confidence: float = Field(default=1.0, description="Confidence score (0-1)")
    raw_response: Optional[str] = Field(None, description="Raw AI response for debugging")
    message: Optional[str] = Field(None, description="Human-readable message")


class BotExecutionResult(BaseModel):
    """Result of bot command execution"""
    status: str = Field(default="success", description="success, pending, or failed")
    request_id: Optional[str] = Field(None, description="Request ID")
    action: str = Field(..., description="Executed action")
    result: Optional[Dict[str, Any]] = Field(None, description="Execution result")
    error: Optional[str] = Field(None, description="Error message if failed")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class HealthResponse(BaseModel):
    """Health check response"""
    status: str = Field(default="healthy")
    backend: str = Field(default="running")
    ai_service: str = Field(default="connected")
    bot_service: str = Field(default="connected")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ErrorResponse(BaseModel):
    """Standard error response"""
    status: str = Field(default="error")
    code: str = Field(..., description="Error code")
    message: str = Field(..., description="Error message")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")


class AuthResponse(BaseModel):
    """Authentication response"""
    status: str = Field(default="success")
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer")
    expires_in: int = Field(default=3600, description="Token expiration in seconds")


class CommandLogEntry(BaseModel):
    """Log entry for a command"""
    id: str = Field(..., description="Command ID")
    user_id: Optional[str] = Field(None)
    input_text: str = Field(...)
    ai_action: str = Field(...)
    status: str = Field(...)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    result: Optional[Dict[str, Any]] = Field(None)
