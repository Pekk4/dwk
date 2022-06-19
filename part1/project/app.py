from flask import Flask
import os, sys


app = Flask(__name__)

@app.route("/")
def index():
    return "Hähää!"

def main():
    print(f"Server started in port {os.getenv('PORT')}", file=sys.stdout, flush=True)

main()
