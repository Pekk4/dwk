import secrets
import time
import sys
from threading import Thread
from datetime import datetime
from flask import Flask
from flask import render_template


app = Flask(__name__)
string = secrets.token_hex(32)


@app.route("/")
def index():
    return f"[{datetime.now()}] {string}"

def main():
    while True:
        print(f"[{datetime.now()}] {string}", file=sys.stdout, flush=True)

        time.sleep(5)

thread = Thread(target=main)
thread.start()
