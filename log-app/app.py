import secrets
import time
import sys
import os

from threading import Thread
from datetime import datetime
from flask import Flask
from flask import render_template


app = Flask(__name__)
string = secrets.token_hex(32)
role = os.getenv("ROLE")
log_file_path = "/logs/time.log"


@app.route("/")
def index():
    return f"[{datetime.now()}] {string}"

def main():
    while True:
        timestamp = f"[{datetime.now()}]"

        #print(f"[{timestamp}] {string}", file=sys.stdout, flush=True)

        if role == "writer":
            with open(log_file_path, 'a') as log_file:
                log_file.write(f'{timestamp}\n')
        else:
            with open(log_file_path, 'r') as log_file:
                lines = log_file.readlines()
                if lines:
                    print(f"{lines[-1].strip()} {string}", file=sys.stdout, flush=True)

        time.sleep(5)

thread = Thread(target=main)
thread.start()
