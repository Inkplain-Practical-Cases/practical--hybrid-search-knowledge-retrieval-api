# Thin HTTP door: delegates the request to the injected handler.
from fastapi import APIRouter
from app.features.feature_pipeline.handlers.handle_request import handle_request
from app.features.feature_pipeline.schemas.request import SearchRequest
router = APIRouter()
@router.post("/search")
def submit(body: SearchRequest):
    return handle_request(body)
