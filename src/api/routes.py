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
async def predict(features: PropertyFeatures):
    try:
        # Conversion explicite des types
        input_data = features.dict()
        prediction = predict_price(input_data)
        return {"predicted_price": round(float(prediction), 2)}
    except Exception as e:
        return {"error": str(e), "status_code": 500}
