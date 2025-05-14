from fastapi import APIRouter
from .schemas import PropertyFeatures
from .model import predict_price

router = APIRouter()

@router.post("/predict")
def predict(data: PropertyFeatures):
    features = data.dict()
    price = predict_price(features)
    return {"predicted_price": price}
