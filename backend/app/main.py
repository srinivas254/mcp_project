from fastapi import FastAPI 
from app.routers.primary import router as primary_router

app = FastAPI()
app.include_router(primary_router)
