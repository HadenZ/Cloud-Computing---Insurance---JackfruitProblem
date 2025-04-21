from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as quote_router
from app.db import Base, engine

# Create tables (only once at startup)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Quotation Service API",
    description="Handles travel and health insurance quote generation.",
    version="1.0.0"
)

# ✅ Add this CORS middleware block
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://159.223.171.199:23332"],  # Your Streamlit frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes
app.include_router(quote_router)
