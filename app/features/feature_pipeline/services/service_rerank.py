# Rerank scoped search results: single-responsibility retrieval service.
def service_rerank(s: dict) -> dict:
    # Keep the top two fusion-ranked documents deterministically.
    s["ranked"]=sorted(s["fused"],key=lambda item:(-item["score"],item["id"]))[:2]
    return s
