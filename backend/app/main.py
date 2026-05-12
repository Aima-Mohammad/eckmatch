from fastapi import FastAPI

app = FastAPI(
    title="EckMatch API",
    description="Internal regulatory reconciliation platform",
    version="0.1.0",
)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint for monitoring and load balancer probes."""
    return {"status": "ok", "service": "eckmatch-api"}
