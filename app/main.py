# Application entry point: builds the FastAPI app and mounts the feature router.
from fastapi import FastAPI
from app.features.feature_pipeline.router import router
app = FastAPI(title="Tenant-scoped search request")
app.include_router(router)

# Source-derived request/event persistence, wired independently of search logic.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
