"""Interactive client for the loopback H-SETS simulator."""
import getpass
import sys
import urllib.error
import urllib.request
from pathlib import Path

method = input("Method GET/PUT/DELETE: ").strip().upper()
if method not in {"GET", "PUT", "DELETE"}:
    raise SystemExit("Unsupported method")
token = getpass.getpass("Token (blank for anonymous): ")
data = None
if method == "PUT":
    data = Path(input("Synthetic input file path: ").strip()).read_bytes()
headers = {"Authorization": "Bearer " + token} if token else {}
request = urllib.request.Request("http://127.0.0.1:8765/object",
                                 data=data, headers=headers, method=method)
try:
    response = urllib.request.urlopen(request, timeout=5)
except urllib.error.HTTPError as error:
    response = error
print("HTTP", response.code)
body = response.read()
if body:
    print(body.decode("utf-8", errors="replace"))
    output = input("Save response to a NEW evidence file (blank to skip): ").strip()
    if output:
        with open(output, "xb") as stream:
            stream.write(body)

