from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import routes_documents
from app.db.database import Base, engine

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Policy Document Service")

from fastapi.middleware.cors import CORSMiddleware
# ✅ Add this CORS middleware block
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://159.223.171.199:23332"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)   

# Mount the directory with generated PDFs to be served under the '/documents' path.
app.mount("/documents", StaticFiles(directory="generated_documents"), name="documents")

# Include your API routes
app.include_router(routes_documents.router, prefix="/api")

# Optional root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Policy Document Service"}