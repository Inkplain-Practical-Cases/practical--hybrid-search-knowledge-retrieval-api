# Handler invokes each search service in stable order with a tenant-scoped request.
from app.features.feature_pipeline.schemas.request import SearchRequest
from app.features.feature_pipeline.services.service_validate import service_validate
from app.features.feature_pipeline.services.service_keyword_search import service_keyword_search
from app.features.feature_pipeline.services.service_vector_search import service_vector_search
def handle_request(body: SearchRequest) -> dict:
    state=service_validate(body.model_dump())
    state=service_keyword_search(state)
    state=service_vector_search(state)
    return state
