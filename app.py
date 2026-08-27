import os
import sys
import threading
import http.server
import functools
import webview

HERE = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))


def serve():
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=HERE)
    httpd = http.server.HTTPServer(("127.0.0.1", 0), handler)
    port = httpd.server_address[1]
    return httpd, port


def main():
    httpd, port = serve()
    t = threading.Thread(target=httpd.serve_forever, daemon=True)
    t.start()
    webview.create_window(
        "吉他弦音播报练习",
        f"http://127.0.0.1:{port}/index.html",
        width=760,
        height=720,
        min_size=(420, 560),
    )
    webview.start()
    httpd.shutdown()


if __name__ == "__main__":
    main()
