"""H-SETS local teaching fixture. Synthetic identities; NOT an authentication example.

Run only on loopback. 'vulnerable' deliberately omits ownership checks and HTML
escaping. No real data, passwords, remote binding, or production deployment.
"""
import argparse
import html
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit

RECORDS = {
    '1': ('alice', 'Alice training record'),
    '2': ('ben', 'Ben training record'),
}


class Handler(BaseHTTPRequestHandler):
    def respond(self, status, body, cookie=None):
        payload = body.encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.send_header('Cache-Control', 'no-store')
        if cookie:
            self.send_header('Set-Cookie', cookie)
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        request = urlsplit(self.path)
        query = parse_qs(request.query, keep_blank_values=True)
        if request.path == '/':
            return self.respond(200, '<h1>H-SETS synthetic local fixture</h1>'
                '<p>Identity switching is a test harness, not real login.</p>'
                '<a href="/switch?user=alice">Use Alice</a> | '
                '<a href="/switch?user=ben">Use Ben</a> | '
                '<a href="/record?id=1">Record 1</a> | '
                '<a href="/record?id=2">Record 2</a>')
        if request.path == '/switch':
            user = query.get('user', [''])[0]
            if user not in ('alice', 'ben'):
                return self.respond(400, 'Unknown synthetic identity')
            return self.respond(200, 'Test identity selected: ' + user,
                'hsets_identity=' + user + '; Path=/; HttpOnly; SameSite=Strict')
        if request.path == '/record':
            cookies = SimpleCookie()
            try:
                cookies.load(self.headers.get('Cookie', ''))
            except Exception:
                return self.respond(400, 'Malformed cookie')
            identity = cookies.get('hsets_identity')
            user = identity.value if identity else None
            if user not in ('alice', 'ben'):
                return self.respond(401, 'Select a synthetic test identity')
            record = RECORDS.get(query.get('id', [''])[0])
            if record is None:
                return self.respond(404, 'Record not found')
            owner, content = record
            if self.server.mode == 'fixed' and owner != user:
                return self.respond(403, 'Forbidden')
            return self.respond(200, html.escape(content))
        if request.path == '/echo':
            value = query.get('text', [''])[0]
            if len(value) > 80:
                return self.respond(400, 'Text exceeds 80 characters')
            rendered = html.escape(value) if self.server.mode == 'fixed' else value
            return self.respond(200, '<p>Training message: ' + rendered + '</p>')
        return self.respond(404, 'Not found')

    def log_message(self, fmt, *args):
        # Synthetic local requests only. Never log real secrets in this fixture.
        print('%s %s' % (self.log_date_time_string(), fmt % args))


def create_server(mode, port=8765):
    if mode not in ('vulnerable', 'fixed'):
        raise ValueError('Unknown fixture mode')
    server = HTTPServer(('127.0.0.1', port), Handler)
    server.mode = mode
    return server


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=['vulnerable', 'fixed'], required=True)
    args = parser.parse_args()
    app = create_server(args.mode)
    print('Local synthetic fixture: http://127.0.0.1:8765 mode=' + args.mode)
    try:
        app.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        app.server_close()
