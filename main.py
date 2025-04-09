from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.main_router import api_router  # This is where `api_router` lives

app = FastAPI(
    title="FocusForge API",
    version="0.1.0",
    description="A productivity and focus tracking backend",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS (adjust for production!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["https://yourdomain.com"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your app routers
app.include_router(api_router)  # This uses `api/routes/users/__init__.py`


# Optional: Health check route
@app.get("/ping")
async def ping():
    return {"status": "ok"}


# # Optional startup/shutdown hooks
# @app.on_event("startup")
# async def on_startup():
#     print("App started")


# @app.on_event("shutdown")
# async def on_shutdown():
#     print("App shutting down")
