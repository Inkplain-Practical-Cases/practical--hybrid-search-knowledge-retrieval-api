# Handler orchestrates the complete tenant-scoped search pipeline.
from app.features.feature_pipeline.schemas.request import SearchRequest
from app.features.feature_pipeline.services.service_validate import service_validate
from app.features.feature_pipeline.services.service_keyword_search import service_keyword_search
from app.features.feature_pipeline.services.service_vector_search import service_vector_search
from app.features.feature_pipeline.services.service_fuse_scores import service_fuse_scores
from app.features.feature_pipeline.services.service_rerank import service_rerank
from app.features.feature_pipeline.services.service_citations import service_citations
def handle_request(body: SearchRequest) -> dict:
    state=service_validate(body.model_dump())
    state=service_keyword_search(state)
    state=service_vector_search(state)
    state=service_fuse_scores(state)
    state=service_rerank(state)
    state=service_citations(state)
    return state
