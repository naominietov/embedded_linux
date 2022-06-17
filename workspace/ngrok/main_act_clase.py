from fastapi import FastAPI
from datetime import datetime
from getmac import get_mac_address

app = FastAPI()

@app.get("/realtime")
def read_root(secret: str = ""):
    eth_mac = get_mac_address(interface="eth0")

    return {"A01706095": secret, "mac": eth_mac}

# uvicorn main:app --reload --port 9600
# ngrok http 9600