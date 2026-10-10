# Final retrieval step: return stable evidence IDs and simple quality coverage.
def service_citations(s: dict) -> dict:
    s["citations"]=[{"source_id":x["id"],"rank":i+1} for i,x in enumerate(s["ranked"])]
    s["evaluation"]={"returned":len(s["citations"]),"unique_sources":len({x["source_id"] for x in s["citations"]})}
    return s
