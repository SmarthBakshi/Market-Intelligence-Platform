"""API v1 router configuration."""

from fastapi import APIRouter

from app.api.v1.endpoints import auth, projects, sources, insights, reports

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(sources.router, prefix="/sources", tags=["sources"])
api_router.include_router(insights.router, prefix="/insights", tags=["insights"])
api_router.include_router(reports.router, prefix="/reports", tags=["reports"])
