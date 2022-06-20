import os
import sys
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def main():
    print(f"Server started in port {os.getenv('PORT')}", file=sys.stdout, flush=True)

main()
