# main.py
from fastapi import FastAPI, Request
from datetime import datetime, timezone
from zoneinfo import ZoneInfo  # Python 3.9+

app = FastAPI()

TARGET_TZ = ZoneInfo("Asia/Kolkata")

def get_client_ip(request: Request) -> str:
    # Prefer X-Forwarded-For if behind reverse proxy / LB (common)
    xff = request.headers.get("x-forwarded-for")
    if xff:
        # X-Forwarded-For can contain multiple IPs: "client, proxy1, proxy2"
        return xff.split(",")[0].strip()
    # Fallback to direct client address
    client = request.client
    return client.host if client else "unknown"

@app.get("/")
async def root(request: Request):
    now_aware = datetime.now(timezone.utc).astimezone(TARGET_TZ)
    return {
        "timestamp": now_aware.isoformat(),  # e.g. "2025-12-11T23:15:00+05:30"
        "ip": get_client_ip(request)
    }

#uvicorn main:app --host 0.0.0.0 --port 8000