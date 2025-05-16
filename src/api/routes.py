from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import PropertyFeatures
from .model import predict_price

app = FastAPI()

# Configuration CORS pour autoriser toutes les origines
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()
app.include_router(router)

@router.post("/predict")
def predict(data: PropertyFeatures):
    features = data.dict()
    price = predict_price(features)
    return {"predicted_price": price}
