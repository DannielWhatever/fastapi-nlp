from fastapi import FastAPI
from app.api.v1.nlp.endpoints import router as autocomplete_router

app = FastAPI()


app.include_router(autocomplete_router, prefix="/api/v1", tags=["autocomplete"])