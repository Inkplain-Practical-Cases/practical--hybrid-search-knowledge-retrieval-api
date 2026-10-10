# Implement semantic retrieval adapter: single-responsibility retrieval service.
def service_vector_search(s: dict) -> dict:
    # Stand-in semantic provider: stable embeddings represented by fixture scores.
    s["semantic_hits"]=[{"id":"d1","score":0.83},{"id":"d2","score":0.72}]
    return s
