from fastapi import FastAPI

from app.api.routes import health
from app.config import settings

app = FastAPI(
    title="${{ values.name }}",
    description="${{ values.description }}",
    version="0.1.0",
)

app.include_router(health.router, tags=["health"])


@app.get("/")
async def root() -> dict[str, str]:
    return {"service": settings.service_name, "status": "running"}