import secrets
import time
import sys


string = secrets.token_hex(32)

while True:
    print(string, file=sys.stdout, flush=True)
    time.sleep(5)
