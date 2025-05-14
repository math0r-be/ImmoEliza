# Point d'entrée FastAPI : crée l'app et inclut les routes
from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="ImmoEliza API")
app.include_router(router)
