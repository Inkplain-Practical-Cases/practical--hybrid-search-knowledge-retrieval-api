# Fuse hybrid ranking scores: single-responsibility retrieval service.
def service_fuse_scores(s: dict) -> dict:
    # Weighted normalized fusion keeps score computation transparent.
    scores={r["id"]:r["score"]*.5 for r in s["keyword_hits"]}
    for hit in s["semantic_hits"]:
        scores[hit["id"]]=scores.get(hit["id"],0)+hit["score"]*.5
    s["fused"]=[{"id":k,"score":round(v,3)} for k,v in scores.items()]
    return s
