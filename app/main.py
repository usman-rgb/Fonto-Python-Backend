from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import (
    auth_router,
    nfts_router,
    collections_router,
    bids_router,
    wallet_router,
    blog_router,
    help_router,
    dashboard_router,
    rankings_router,
    activity_router,
    newsletter_router,
    notifications_router,
)

app = FastAPI()

# CORS Middleware to allow requests from frontend (Hostinger)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-hostinger-domain.com"],  # Replace with your Hostinger domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all routers with appropriate prefixes and tags
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(nfts_router, prefix="/api", tags=["nfts"])
app.include_router(collections_router, prefix="/api", tags=["collections"])
app.include_router(bids_router, prefix="/api", tags=["bids"])
app.include_router(wallet_router, prefix="/api", tags=["wallet"])
app.include_router(blog_router, prefix="/api", tags=["blog"])
app.include_router(help_router, prefix="/api", tags=["help"])
app.include_router(dashboard_router, prefix="/api", tags=["dashboard"])
app.include_router(rankings_router, prefix="/api", tags=["rankings"])
app.include_router(activity_router, prefix="/api", tags=["activity"])
app.include_router(newsletter_router, prefix="/api", tags=["newsletter"])
app.include_router(notifications_router, prefix="/api", tags=["notifications"])

@app.get("/")
def read_root():
=======
from fastapi import FastAPI
from app.routes import (
    auth_router,
    nfts_router,
    collections_router,
    bids_router,
    wallet_router,
    blog_router,
    help_router,
    dashboard_router,
    rankings_router,
    activity_router,
    newsletter_router,
    notifications_router,
)

app = FastAPI()

# Include all routers with appropriate prefixes and tags
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(nfts_router, prefix="/api", tags=["nfts"])
app.include_router(collections_router, prefix="/api", tags=["collections"])
app.include_router(bids_router, prefix="/api", tags=["bids"])
app.include_router(wallet_router, prefix="/api", tags=["wallet"])
app.include_router(blog_router, prefix="/api", tags=["blog"])
app.include_router(help_router, prefix="/api", tags=["help"])
app.include_router(dashboard_router, prefix="/api", tags=["dashboard"])
app.include_router(rankings_router, prefix="/api", tags=["rankings"])
app.include_router(activity_router, prefix="/api", tags=["activity"])
app.include_router(newsletter_router, prefix="/api", tags=["newsletter"])
app.include_router(notifications_router, prefix="/api", tags=["notifications"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Fonto Python Backend"}
