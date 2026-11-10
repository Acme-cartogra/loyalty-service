from fastapi import FastAPI

app = FastAPI(title="loyalty-service", version="1.0.0")

@app.get("/actuator/health")
def health(): return {"status": "UP"}

@app.get("/loyaltys")
def route_0(): return {"status": "ok"}

@app.post("/loyaltys")
def route_1(): return {"status": "ok"}

@app.get("/loyaltys/{id}")
def route_2(): return {"status": "ok"}
