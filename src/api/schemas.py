# Définit les schémas de validation des entrées/sorties avec Pydantic
from pydantic import BaseModel, Field

class PropertyFeatures(BaseModel):
    bedroomCount: int = Field(..., gt=0, example=2)
    bathroomCount: int = Field(..., gt=0, example=1)
    habitableSurface: float = Field(..., gt=0.0, example=100.0)
    landSurface: float = Field(..., gt=0.0, example=200.0)
    facadeCount: int = Field(..., gt=0, example=2)
    terraceSurface: float = Field(..., ge=0.0, example=15.0)
    hasSwimmingPool: bool = Field(..., example=False)
    hasTerrace: bool = Field(..., example=True)
    buildingConstructionYear: int = Field(..., gt=1800, le=2025, example=2010)
    postCode: int = Field(..., gt=999, lt=10000, example=1000)
    epcScore_encoded: int = Field(..., ge=0, le=8, example=4, 
        description="Encoded EPC: 0=A++,1=A+,2=A,3=B,4=C,5=D,6=E,7=F,8=G")
