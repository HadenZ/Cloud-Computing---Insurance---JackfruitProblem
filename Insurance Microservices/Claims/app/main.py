from fastapi import FastAPI
from app.api import routes_claims
from app.db.database import Base, engine

# Create database tables (if they don't exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Claims Processing Service")

from fastapi.middleware.cors import CORSMiddleware
# ✅ Add this CORS middleware block
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://159.223.171.199:23332"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_claims.router, prefix="/api")

# Optionally, add a root endpoint for a welcome message
@app.get("/")
def read_root():
    return {"message": "Welcome to the Claims Processing Service"}
