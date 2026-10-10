# Input contract: Pydantic validates fields at the external boundary.
from pydantic import BaseModel, Field
class SearchRequest(BaseModel):
    tenant_id: str = Field(min_length=1)
    query: str = Field(min_length=1)
