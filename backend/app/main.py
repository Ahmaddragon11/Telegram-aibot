from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.config import settings
from app.middleware.auth import AuthMiddleware
from app.routes import health, ai, bot

# Create FastAPI app
app = FastAPI(
    title="Telegram AI Bot Platform",
    description="A production-ready AI-powered web platform connected to Telegram",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add authentication middleware
app.add_middleware(AuthMiddleware)

# Include routers
app.include_router(health.router)
app.include_router(ai.router)
app.include_router(bot.router)


@app.on_event("startup")
async def startup_event():
    """Startup event"""
    print("🚀 Telegram AI Bot Backend Starting...")
    print(f"📝 Debug Mode: {settings.debug}")
    print(f"🤖 AI Provider: {settings.ai_provider}")
    print(f"🔑 API Documentation: http://{settings.backend_host}:{settings.backend_port}/docs")


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event"""
    print("🛑 Telegram AI Bot Backend Shutting Down...")


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint"""
    return {
        "message": "🚀 Telegram AI Bot Backend API",
        "version": "1.0.0",
        "docs": "http://localhost:8000/docs",
        "health": "http://localhost:8000/health"
    }


@app.get("/api/health", tags=["Health"])
async def api_health():
    """API health check (no auth required)"""
    return {
        "status": "healthy",
        "service": "telegram-aibot-backend",
        "ai_provider": settings.ai_provider
    }


@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Handle 404 errors"""
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "code": "NOT_FOUND",
            "message": "Endpoint not found",
            "path": str(request.url)
        }
    )


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """Handle 500 errors"""
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "code": "INTERNAL_ERROR",
            "message": "Internal server error"
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host=settings.backend_host,
        port=settings.backend_port,
        reload=settings.debug
    )

