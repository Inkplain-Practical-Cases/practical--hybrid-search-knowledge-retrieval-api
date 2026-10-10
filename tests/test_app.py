from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_retrieval_chain():
    r=client.post("/search",json={"tenant_id":"t","query":"search"})
    assert r.status_code==200
    assert "ranked" in r.json()
def test_tenant_required():
    assert client.post("/search",json={"tenant_id":"","query":"search"}).status_code==422
