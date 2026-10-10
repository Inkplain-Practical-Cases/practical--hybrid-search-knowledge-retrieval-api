from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_hybrid_search_citations():
    r=client.post("/search",json={"tenant_id":"t","query":"search"})
    assert r.status_code==200
    assert len(r.json()["citations"])==2
    assert r.json()["evaluation"]["unique_sources"]==2
