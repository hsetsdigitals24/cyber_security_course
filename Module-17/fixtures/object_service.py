"""H-SETS local cloud-concept simulator. Loopback only; not production storage."""
import hmac
import json
import os
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(os.environ.get("HSETS_STORE", "store")).resolve()
ROOT.mkdir(parents=True, exist_ok=True)
OBJECT = ROOT / "document.txt"
AUDIT = ROOT / "audit.jsonl"
TOKENS = {role: os.environ.get("HSETS_" + role.upper() + "_TOKEN", "")
          for role in ("reader", "writer")}
if not all(TOKENS.values()) or len(set(TOKENS.values())) != 2:
    raise SystemExit("Set distinct nonempty reader and writer tokens.")
PORT = int(os.environ.get("HSETS_PORT", "8765"))

class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Never log headers or tokens.

    def reply(self, status, body=b"", role="anonymous"):
        record = {"time": datetime.now(timezone.utc).isoformat(),
                  "role": role, "method": self.command,
                  "path": "/object" if self.path == "/object" else "other",
                  "status": status}
        with AUDIT.open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(record) + "\n")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def access(self):
        supplied = self.headers.get("Authorization", "")
        for role, token in TOKENS.items():
            if hmac.compare_digest(supplied, "Bearer " + token):
                return role
        return None

    def do_GET(self):
        role = self.access()
        if role is None:
            return self.reply(401)
        if self.path != "/object" or not OBJECT.exists():
            return self.reply(404, role=role)
        self.reply(200, OBJECT.read_bytes(), role)

    def do_PUT(self):
        role = self.access()
        if role is None:
            return self.reply(401)
        if role != "writer":
            return self.reply(403, role=role)
        if self.path != "/object":
            return self.reply(404, role=role)
        try:
            length = int(self.headers.get("Content-Length", "-1"))
        except ValueError:
            return self.reply(400, role=role)
        if not 0 <= length <= 4096:
            return self.reply(413, role=role)
        body = self.rfile.read(length)
        if len(body) != length:
            return self.reply(400, role=role)
        OBJECT.write_bytes(body)
        self.reply(204, role=role)

    def do_DELETE(self):
        role = self.access()
        if role is None:
            return self.reply(401)
        if role != "writer":
            return self.reply(403, role=role)
        if self.path != "/object" or not OBJECT.exists():
            return self.reply(404, role=role)
        OBJECT.unlink()
        self.reply(204, role=role)

if __name__ == "__main__":
    HTTPServer(("127.0.0.1", PORT), Handler).serve_forever()

