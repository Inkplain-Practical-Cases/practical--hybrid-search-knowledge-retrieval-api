"""Verify SQLite request and event FK with no raw search payload."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit

def test_request_event_schema(tmp_path):
    path = str(tmp_path / "audit.sqlite3")
    request_id = provider_record_request_audit("GET", "/search", 200, 7.0, path)
    with sqlite3.connect(path) as connection:
        assert connection.execute("SELECT COUNT(*) FROM search_api_requests WHERE id=?", (request_id,)).fetchone()[0] == 1
        assert connection.execute("SELECT COUNT(*) FROM search_api_events WHERE request_id=?", (request_id,)).fetchone()[0] == 1
        assert connection.execute("PRAGMA foreign_key_check").fetchall() == []
