import os
import sys
import subprocess
import shutil
import http.server
import functools
import threading
import time
import webbrowser

HERE = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
BROWSER_CANDIDATES = ["chrome", "msedge", "firefox"]


def find_browser():
    for name in BROWSER_CANDIDATES:
        p = shutil.which(name)
        if p:
            return p
    return None


def main():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=HERE)
    httpd = http.server.HTTPServer(("127.0.0.1", 0), handler)
    port = httpd.server_address[1]
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    url = f"http://127.0.0.1:{port}/index.html"
    exe = find_browser()
    if exe:
        subprocess.Popen([exe, "--app=" + url])
    else:
        webbrowser.open(url)
    while t.is_alive():
        time.sleep(1)
    httpd.shutdown()


if __name__ == "__main__":
    main()
