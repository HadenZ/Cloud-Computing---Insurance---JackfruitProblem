from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_policy
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Policy Management Service")

# ✅ Add this CORS middleware block
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://159.223.171.199:23332"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes_policy.router, prefix="/api")


