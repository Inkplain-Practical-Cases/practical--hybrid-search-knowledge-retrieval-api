# Implement keyword retrieval: single-responsibility retrieval service.
def service_keyword_search(s: dict) -> dict:
    # Deterministic scoped corpus for offline retrieval tests.
    corpus = [{"id":"d1","tenant_id":s["tenant_id"],"text":"enterprise hybrid search API"}, {"id":"d2","tenant_id":s["tenant_id"],"text":"vector knowledge retrieval"}]
    query=s["query"].lower()
    s["keyword_hits"]=[{"id":d["id"],"score":float(len(set(query.split()) & set(d["text"].split())))} for d in corpus if d["tenant_id"]==s["tenant_id"]]
    return s
