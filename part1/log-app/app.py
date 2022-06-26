import secrets
import time
import sys
from threading import Thread
from datetime import datetime
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
    return string

def main():
    global string

    while True:
        string = f"[{datetime.now()}] {secrets.token_hex(32)}"

        print(string, file=sys.stdout, flush=True)

        time.sleep(5)

thread = Thread(target=main)
thread.start()
