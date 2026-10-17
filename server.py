"""LedgerLoop demo server (Python 3.8+, standard library only).
Serves the site and proxies MiniMoth OTP calls so the API key stays server-side.
Run:  python server.py   ->  http://localhost:3000
"""
import json, os, urllib.request, urllib.error
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

KEY = os.environ.get("MINIMOTH_API_KEY",
      "mm_test_b68cbb0a1584567476f9c29c88bd08bc9b08d697c5cbca9babadacbe2549fe1c3a63e648cf609a7938231fde0b2966ab")
ROUTES = {"/api/otp/send": "/v1/otp/send", "/api/otp/verify": "/v1/otp/verify"}
FILES = {"/": "index.html", "/index.html": "index.html", "/llms.txt": "llms.txt",
         "/robots.txt": "robots.txt", "/sitemap.xml": "sitemap.xml"}
TYPES = {".html": "text/html; charset=utf-8", ".txt": "text/plain; charset=utf-8", ".xml": "application/xml"}
HERE = os.path.dirname(os.path.abspath(__file__))

class H(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype):
        self.send_response(code); self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)

    def do_GET(self):
        name = FILES.get(self.path.split("?")[0])
        if not name: return self._send(404, b"Not found", "text/plain")
        with open(os.path.join(HERE, name), "rb") as f:
            self._send(200, f.read(), TYPES.get(os.path.splitext(name)[1], "text/plain"))

    def do_POST(self):
        target = ROUTES.get(self.path.split("?")[0])
        if not target: return self._send(404, b'{"message":"Unknown route"}', "application/json")
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        req = urllib.request.Request("https://api.minimoth.dev" + target, data=body, method="POST",
              headers={"X-Api-Key": KEY, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=15) as r: code, out = r.status, r.read()
        except urllib.error.HTTPError as e: code, out = e.code, e.read()
        except Exception as e:
            code, out = 502, json.dumps({"message": "Could not reach MiniMoth: %s" % e}).encode()
        self._send(code, out, "application/json")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    print("LedgerLoop on http://localhost:%d" % port)
    ThreadingHTTPServer(("0.0.0.0", port), H).serve_forever()
