"""Run the whole site locally (same code as on Vercel):  python dev_server.py  ->  http://localhost:8000"""
import mimetypes, os, sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "api"))
import co2, nox


class H(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=os.path.join(HERE, "public"), **k)

    def do_GET(self):
        if self.path.startswith("/api/co2"):
            return co2.handler.do_GET(self)
        if self.path.startswith("/api/nox"):
            return nox.handler.do_GET(self)
        return super().do_GET()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    print("http://localhost:%d" % port)
    ThreadingHTTPServer(("0.0.0.0", port), H).serve_forever()
